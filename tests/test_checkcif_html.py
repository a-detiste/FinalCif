#   ----------------------------------------------------------------------------
#   "THE BEER-WARE LICENSE" (Revision 42):
#   Daniel Kratzert <dkratzert@gmx.de> wrote this file.  As long as you retain
#   this notice you can do whatever you want with this stuff. If we meet some day,
#   and you think this stuff is worth it, you can buy me a beer in return.
#   ----------------------------------------------------------------------------
import os
import time
import unittest
from pathlib import Path

from PyQt5.QtCore import Qt
from PyQt5.QtTest import QTest

from finalcif.appwindow import AppWindow
from finalcif.gui.custom_classes import COL_EDIT
from finalcif.tools.misc import strip_finalcif_of_name


class TestCheckCifHTML(unittest.TestCase):

    def setUp(self) -> None:
        if os.environ.get('NO_NETWORK'):
            self.skipTest('No network available.')
        os.chdir(Path(__file__).absolute().parent.parent)
        self.myapp = AppWindow(Path('tests/examples/work/cu_BruecknerJK_153F40_0m.cif').absolute(), unit_test=True)
        self.myapp.running_inside_unit_test = True
        self.myapp.hide()  # For full screen view
        self.resobj = Path('checkcif-' + strip_finalcif_of_name(self.myapp.cif.fileobj.stem) + '-finalcif.html')

    def tearDown(self) -> None:
        self.resobj.unlink(missing_ok=True)
        self.myapp.final_cif_file_name.unlink(missing_ok=True)
        Path('platon.out').unlink(missing_ok=True)
        Path('check.def').unlink(missing_ok=True)
        Path('cu_BruecknerJK_153F40_0m-finalcif.chk').unlink(missing_ok=True)
        Path('cu_BruecknerJK_153F40_0m-finalcif.gif').unlink(missing_ok=True)
        Path('cu_BruecknerJK_153F40_0m-finalcif.ins').unlink(missing_ok=True)
        Path('cu_BruecknerJK_153F40_0m-finalcif.lst').unlink(missing_ok=True)
        Path('checkcif-cu_BruecknerJK_153F40_0m-finalcif.html').unlink(missing_ok=True)
        Path('checkcif-cu_BruecknerJK_153F40_0m-finalcif.pdf').unlink(missing_ok=True)
        Path('checkpdf-cu_BruecknerJK_153F40_0m-finalcif.html').unlink(missing_ok=True)
        self.myapp.close()

    def equipment_click(self, field: str):
        self.myapp.ui.EquipmentTemplatesStackedWidget.setCurrentIndex(0)
        item = self.myapp.ui.EquipmentTemplatesListWidget.findItems(field, Qt.MatchStartsWith)[0]
        self.myapp.ui.EquipmentTemplatesListWidget.setCurrentItem(item)
        self.myapp.equipment.load_selected_equipment()

    @unittest.skip('temporary skip')
    def test_checkcif_html(self):
        """Runs a html checkcif without hkl and compares the result with the html file."""
        self.maxDiff = None
        self.equipment_click('D8 VENTURE')
        self.equipment_click('Crystallographer Details')
        self.myapp.ui.cif_main_table.setText(key='_chemical_absolute_configuration', txt='ad', column=COL_EDIT)
        # Remember: This test is without structure factors!
        self.myapp.ui.structfactCheckBox.setChecked(True)
        QTest.mouseClick(self.myapp.ui.CheckcifHTMLOnlineButton, Qt.LeftButton, Qt.NoModifier)
        time.sleep(5)
        # this is the file on github:
        html_as_it_is_expected = Path('checkcif-' + strip_finalcif_of_name(self.myapp.cif.fileobj.stem) + '-test.html')
        htmlfile = html_as_it_is_expected.read_text().splitlines()[28:-13]
        # this is the new downloadad file
        result = self.resobj.read_text().splitlines()[28:-13]
        self.assertEqual(htmlfile, result)
