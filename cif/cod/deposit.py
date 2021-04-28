import io
from typing import Union

import requests

from cif.cif_file_io import CifContainer
from gui.finalcif_gui import Ui_FinalCifWindow
from tools.settings import FinalCifSettings

"""
TODO: These warnings contain too much unneeded words:

Depositing structure 'cif' into TESTCOD:
cif-deposit.pl: Connection to authentication database - OK
cif-deposit.pl: User authentication - OK
cif-deposit.pl: File upload - OK
cif-deposit.pl: Connection to structure database - OK
cif-deposit.pl: Check for duplicates - OK
cif-deposit.pl: cod-tools/scripts/cif_cod_check: - data_cu_BruecknerJK_153F40_0m: WARNING, data item '_journal_name_full' was not found.
cod-tools/scripts/cif_cod_check: - data_cu_BruecknerJK_153F40_0m: WARNING, data item '_publ_section_title' was not found.
cod-tools/scripts/cif_cod_check: - data_cu_BruecknerJK_153F40_0m: WARNING, neither data item '_journal_year' nor data item '_journal_volume' was found.
cod-tools/scripts/cif_cod_check: - data_cu_BruecknerJK_153F40_0m: WARNING, neither data item '_journal_page_first' nor data item '_journal_article_reference' was found.
cod-tools/scripts/cif_cod_check: -: NOTE, 4 WARNING(s) encountered.

What does that mean?:

cif-deposit.pl: cifvalues: -(51793): ERROR, stray CIF values at the beginning of the input file

"""

class COD_Deposit():
    def __init__(self, ui: Ui_FinalCifWindow, cif: Union[CifContainer, None] = None):
        self.ui = ui
        self.settings = FinalCifSettings()
        self._cif = cif
        if not self.cif:
            self.ui.depositCIFpushButton.setDisabled(True)
        self._set_checkbox_states()
        self.ui.depositorUsernameLineEdit.textChanged.connect(self._set_username)
        self.ui.depositorPasswordLineEdit.textChanged.connect(self._set_password)
        self.ui.ContactAuthorsFullNamePersonalLineEdit.textChanged.connect(self._set_author_name)
        self.ui.ContactAuthorsFullNamePersonalLineEdit_2.textChanged.connect(self._set_author_name)
        self.ui.depositorsFullNameLineEdit.textChanged.connect(self._set_author_name)
        self.ui.ContactAuthorEmailAddressLineEdit.textChanged.connect(self._set_author_email)
        self.ui.ContactAuthorEmailAddressLineEdit_2.textChanged.connect(self._set_author_email)
        self.ui.depsoitorEMailAddressLineEdit.textChanged.connect(self._set_author_email)
        #
        self.ui.depositCIFpushButton.clicked.connect(self._prepare_deposit)
        # production url:
        # url = 'https://www.crystallography.net/cod-test/cgi-bin/cif-deposit.pl'
        # test_url:
        self.url = 'https://www.crystallography.net/cod-test/cgi-bin/cif-deposit.pl'
        username = self.settings.load_value_of_key('cod_username')
        if username:
            # self.username = username
            self.ui.depositorUsernameLineEdit.setText(username)
        else:
            self.username = ''
        self.password = ''
        self.author_name = ''
        self.author_email = ''
        # TODO: Make input field for this in personal page
        self.user_email = 'dkratzert@gmx.de'

    @property
    def cif(self) -> CifContainer:
        return self._cif

    @cif.setter
    def cif(self, obj):
        self.ui.depositCIFpushButton.setEnabled(True)
        self._cif = obj
        self.author_name = self._cif['_audit_contact_author_name']
        self.ui.ContactAuthorsFullNamePersonalLineEdit.setText(self.author_name)
        self.ui.ContactAuthorsFullNamePersonalLineEdit_2.setText(self.author_name)
        self.ui.depositorsFullNameLineEdit.setText(self.author_name)
        self.author_email = self._cif['_audit_contact_author_email']
        self.ui.ContactAuthorEmailAddressLineEdit.setText(self.author_email)
        self.ui.ContactAuthorEmailAddressLineEdit_2.setText(self.author_email)
        self.ui.depsoitorEMailAddressLineEdit.setText(self.author_email)

    def _set_checkbox_states(self):
        self.ui.prepublicationDepositCheckBox.clicked.connect(self._prepublication_was_toggled)
        self.ui.publishedDepositionCheckBox.clicked.connect(self._published_was_toggled)
        self.ui.personalDepositCheckBox.clicked.connect(self._personal_was_toggled)
        self.ui.personalDepositCheckBox.setChecked(True)
        self.deposition_type = 'personal'
        self.ui.depositionOptionsStackedWidget.setCurrentIndex(0)

    def _personal_was_toggled(self, state: bool):
        self.ui.prepublicationDepositCheckBox.setChecked(False)
        self.ui.publishedDepositionCheckBox.setChecked(False)
        if state:
            self.ui.depositionOptionsStackedWidget.setCurrentIndex(0)
            self.deposition_type = 'personal'
            self.reset_deposit_button_state_to_initial()

    def _prepublication_was_toggled(self, state: bool):
        self.ui.publishedDepositionCheckBox.setChecked(False)
        self.ui.personalDepositCheckBox.setChecked(False)
        if state:
            self.ui.depositionOptionsStackedWidget.setCurrentIndex(1)
            self.deposition_type = 'prepublication'
            self.reset_deposit_button_state_to_initial()

    def _published_was_toggled(self, state: bool):
        self.ui.prepublicationDepositCheckBox.setChecked(False)
        self.ui.personalDepositCheckBox.setChecked(False)
        if state:
            self.ui.depositionOptionsStackedWidget.setCurrentIndex(2)
            self.deposition_type = 'published'
            self.reset_deposit_button_state_to_initial()

    def deposition_type_to_int(self, deposition_type: str):
        if deposition_type == 'personal':
            return 0
        if deposition_type == 'prepublication':
            return 1
        if deposition_type == 'published':
            return 2
        # This is the output page:
        if deposition_type == 'deposit':
            return 3

    def cif_deposit(self):
        self.switch_to_page('deposit')
        if not self.cif:
            print('No cif opened!')
            return
        self.ui.depositOutputTextBrowser.setText('starting deposition...')
        print('starting deposition of ', self.cif.fileobj.name)
        # with open(self.cif.fileobj.absolute(), 'rb') as fileobj:
        data = {'username'       : self.username,
                # Path('/Users/daniel/cod_username.txt').read_text(encoding='ascii'),
                'password'       : self.password,
                # Path('/Users/daniel/cod_password.txt').read_text(encoding='ascii'),
                'user_email'     : self.user_email,  # 'dkratzert@gmx.de',
                'deposition_type': self.deposition_type,  # published prepublication, personal
                'output_mode'    : 'html',
                'progress'       : '1',  # must be 1 if supplied!
                'filename'       : self.cif.fileobj.name,
                }
        if self.deposition_type == 'published':
            if self.ui.replaceDepositCheckBox.isChecked():
                data.update({'replace': '1'})
            data.update({'message': self.ui.publishedLogPlainTextEdit.toPlainText()})
        if self.deposition_type == 'prepublication':
            # TODO: prepublication and replace is possible with the REST API. Is this intended?
            # data.update({'replace': '1'})
            data.update({'author_name': self.author_name})
            data.update({'author_email': self.author_email})
            data.update({'hold_period': self.ui.embargoTimeInMonthsLineEdit.text()})
        if self.deposition_type == 'personal':
            data.update({'author_name': self.author_name})
            data.update({'author_email': self.author_email})
        fileobj = io.StringIO(self.cif.cif_as_string(without_hkl=True))
        if self.ui.depositHKLcheckBox.isChecked():
            files = {'cif': fileobj, 'hkl': io.StringIO(self.cif.hkl_file)}
        else:
            files = {'cif': fileobj}
        print('making request')
        r = requests.post(self.url, files=files, data=data)
        # hooks={'response': self.log_response_text})
        print(r.text)
        self.ui.depositOutputTextBrowser.setText(r.text)
        self.set_deposit_button_to_try_again()
        return r

    def switch_to_page(self, deposition_type: str):
        self.reset_deposit_button_state_to_initial()
        self.ui.depositionOptionsStackedWidget.setCurrentIndex(self.deposition_type_to_int(deposition_type))

    def reset_deposit_button_state_to_initial(self):
        self.ui.depositCIFpushButton.disconnect()
        self.ui.depositOutputTextBrowser.clear()
        self.ui.depositCIFpushButton.setText("Deposit CIF")
        self.ui.depositCIFpushButton.clicked.connect(self._prepare_deposit)

    def set_deposit_button_to_try_again(self):
        self.ui.depositCIFpushButton.setText("Try Again")
        self.ui.depositCIFpushButton.disconnect()
        self.ui.depositCIFpushButton.clicked.connect(lambda: self.switch_to_page(self.deposition_type))

    def log_response_text(self, resp: requests.Response, *args, **kwargs):
        # logger.warning('Got response %r from %s', resp.text, resp.url)
        print(resp.text)

    def _set_username(self, text: str):
        self.settings.save_key_value('cod_username', text)
        self.username = text

    def _set_password(self, text: str):
        # Do not store this anywhere!
        self.password = text

    def _set_author_name(self, text: str):
        self.cif['_audit_contact_author_name'] = text
        self.author_name = text

    def _set_author_email(self, text: str):
        self.cif['_audit_contact_author_email'] = text
        self.author_email = text

    def _prepare_deposit(self):
        print("#### Depositiong in '{}' mode...".format(self.deposition_type))
        self.ui.depositOutputTextBrowser.clear()
        self.switch_to_page('deposit')
        if len(self.username) < 2:
            self.ui.depositOutputTextBrowser.setText('no username given')
            self.set_deposit_button_to_try_again()
            return
        if len(self.password) < 4:
            self.ui.depositOutputTextBrowser.setText('no password given')
            self.set_deposit_button_to_try_again()
            return
        r = self.cif_deposit()
        # print(r.text)


if __name__ == '__main__':
    # x = cif_deposit()
    # print(x.request.register_hook(log_response_text()))
    # print("Text from COD:", x.text, '##')
    # print(x.iter_content())
    # print(x.content)
    # print(x.headers)
    # pprint(x.request.headers)
    # pprint(x.request.body)
    # print(x.status_code)
    pass
