# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\GitHub\FinalCif\gui\author.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_AuthorsForm(object):
    def setupUi(self, AuthorsForm):
        AuthorsForm.setObjectName("AuthorsForm")
        self.verticalLayout = QtWidgets.QVBoxLayout(AuthorsForm)
        self.verticalLayout.setObjectName("verticalLayout")
        self.verticalLayout_24 = QtWidgets.QVBoxLayout()
        self.verticalLayout_24.setObjectName("verticalLayout_24")
        self.label_20 = QtWidgets.QLabel(AuthorsForm)
        self.label_20.setObjectName("label_20")
        self.verticalLayout_24.addWidget(self.label_20)
        self.formLayout_6 = QtWidgets.QFormLayout()
        self.formLayout_6.setObjectName("formLayout_6")
        self.label_22 = QtWidgets.QLabel(AuthorsForm)
        self.label_22.setOpenExternalLinks(True)
        self.label_22.setObjectName("label_22")
        self.formLayout_6.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_22)
        self.FullNameLineEdit = QtWidgets.QLineEdit(AuthorsForm)
        self.FullNameLineEdit.setObjectName("FullNameLineEdit")
        self.formLayout_6.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.FullNameLineEdit)
        self.label_21 = QtWidgets.QLabel(AuthorsForm)
        self.label_21.setObjectName("label_21")
        self.formLayout_6.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_21)
        self.label_16 = QtWidgets.QLabel(AuthorsForm)
        self.label_16.setObjectName("label_16")
        self.formLayout_6.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_16)
        self.EMailLineEdit = QtWidgets.QLineEdit(AuthorsForm)
        self.EMailLineEdit.setObjectName("EMailLineEdit")
        self.formLayout_6.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.EMailLineEdit)
        self.label_18 = QtWidgets.QLabel(AuthorsForm)
        self.label_18.setObjectName("label_18")
        self.formLayout_6.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_18)
        self.FootNoteLineEdit = QtWidgets.QLineEdit(AuthorsForm)
        self.FootNoteLineEdit.setObjectName("FootNoteLineEdit")
        self.formLayout_6.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.FootNoteLineEdit)
        self.label_34 = QtWidgets.QLabel(AuthorsForm)
        self.label_34.setObjectName("label_34")
        self.formLayout_6.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.label_34)
        self.ORCIDLineEdit = QtWidgets.QLineEdit(AuthorsForm)
        self.ORCIDLineEdit.setObjectName("ORCIDLineEdit")
        self.formLayout_6.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.ORCIDLineEdit)
        self.label_13 = QtWidgets.QLabel(AuthorsForm)
        self.label_13.setObjectName("label_13")
        self.formLayout_6.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.label_13)
        self.PhoneLineEdit = QtWidgets.QLineEdit(AuthorsForm)
        self.PhoneLineEdit.setObjectName("PhoneLineEdit")
        self.formLayout_6.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.PhoneLineEdit)
        self.ContactAuthorCheckBox = QtWidgets.QCheckBox(AuthorsForm)
        self.ContactAuthorCheckBox.setObjectName("ContactAuthorCheckBox")
        self.formLayout_6.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.ContactAuthorCheckBox)
        self.AddressTextedit = QtWidgets.QTextEdit(AuthorsForm)
        self.AddressTextedit.setObjectName("AddressTextedit")
        self.formLayout_6.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.AddressTextedit)
        self.verticalLayout_24.addLayout(self.formLayout_6)
        self.verticalLayout.addLayout(self.verticalLayout_24)

        self.retranslateUi(AuthorsForm)
        QtCore.QMetaObject.connectSlotsByName(AuthorsForm)

    def retranslateUi(self, AuthorsForm):
        _translate = QtCore.QCoreApplication.translate
        AuthorsForm.setWindowTitle(_translate("AuthorsForm", "Form"))
        self.label_20.setText(_translate("AuthorsForm", "Details about the authors of a manuscript submitted for publication."))
        self.label_22.setText(_translate("AuthorsForm", "Full Name"))
        self.label_21.setText(_translate("AuthorsForm", "Adresss"))
        self.label_16.setText(_translate("AuthorsForm", "e-mail"))
        self.label_18.setText(_translate("AuthorsForm", "footnote"))
        self.label_34.setText(_translate("AuthorsForm", "ORCID"))
        self.label_13.setText(_translate("AuthorsForm", "phone number"))
        self.ContactAuthorCheckBox.setText(_translate("AuthorsForm", "This is a contact author"))
