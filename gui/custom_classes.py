from PyQt5.QtCore import QEvent, QObject, Qt
from PyQt5.QtGui import QPalette, QResizeEvent
from PyQt5.QtWidgets import QAbstractScrollArea, QComboBox, QFrame, QPlainTextEdit, QSizePolicy, QTableWidget, \
    QTableWidgetItem, QWidget, QHeaderView

from cif.cif_file_io import retranslate_delimiter


class ItemTextMixin:

    # def __init__(self, parent: QWidget = None):
    #    super().__init__(parent)

    def text(self, row: int, column: int) -> str:
        """
        Returns the text inside a table cell.
        """
        try:
            txt = self.item(row, column).text()
        except AttributeError:
            txt = None
        if not txt:
            try:
                txt = self.item(row, column).data(0)
            except AttributeError:
                txt = None
        if not txt:
            try:
                # for QPlaintextWidgets:
                txt = self.cellWidget(row, column).toPlainText()
            except AttributeError:
                txt = None
        if not txt:
            # for comboboxes:
            try:
                txt = self.cellWidget(row, column).currentText()
            except AttributeError:
                txt = None
        return txt


class MyCifTable(QTableWidget, ItemTextMixin):

    def __init__(self, parent: QWidget = None):
        super().__init__(parent)
        self.parent = parent
        self.installEventFilter(self)
        self.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

    def eventFilter(self, widget: QObject, event: QEvent):
        """
        Event filter for tab down on third column.
        """
        if event.type() == QEvent.KeyRelease and event.key() == Qt.Key_Backtab:
            row = self.currentRow()
            if row > 0:
                self.setCurrentCell(row - 1, 2)
            return True
        if event.type() == QEvent.KeyRelease and event.key() == Qt.Key_Tab:
            row = self.currentRow()
            self.setCurrentCell(row, 2)
            return True
        return QObject.eventFilter(self, widget, event)

    def adjustToContents(self):
        pass


class MyQPlainTextEdit(QPlainTextEdit):
    """
    A special plaintextedit with convenient methods to set the background color and other things.
    """

    def __init__(self, parent=None):
        super().__init__(parent)
        self.parent = parent
        self.setFocusPolicy(Qt.StrongFocus)
        self.setFrameShape(QFrame.NoFrame)
        self.setTabChangesFocus(True)
        self.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        #self.textChanged.connect(self.myresize)
        # self.parent.adjustToContents()

    def setColor(self, color):
        pal = self.palette()
        pal.setColor(QPalette.Base, color)
        self.setPalette(pal)

    def set_uneditable(self):
        self.setReadOnly(True)

    def onTextChanged(self):
        size = self.document().size().toSize()
        self.setFixedHeight(size.height() + 30)

    def resizeEvent(self, event: QResizeEvent):
        self.parent.adjustToContents()
        super().resizeEvent(event)


class MyComboBox(QComboBox):
    """
    A special QComboBox with convenient methods to set the background color and other things.
    """

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setFocusPolicy(Qt.StrongFocus)
        self.setSizeAdjustPolicy(QComboBox.AdjustToMinimumContentsLength)
        self.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        self.setEditable(True)  # only editable as new template
        self.installEventFilter(self)

    def eventFilter(self, widget: QObject, event: QEvent):
        """
        Event filter to ignore wheel events in comboboxes to prevent accidental changes to them.
        """
        if event.type() == QEvent.Wheel and widget and not widget.hasFocus():
            event.ignore()
            return True
        return QObject.eventFilter(self, widget, event)

    def set_uneditable(self):
        self.setFlags(self.flags() ^ Qt.ItemIsEditable)


class MyTableWidgetItem(QTableWidgetItem):

    def __init__(self, parent=None):
        super().__init__(parent)

    def set_uneditable(self):
        self.setFlags(self.flags() ^ Qt.ItemIsEditable)


class MyEQTableWidget(QTableWidget, ItemTextMixin):
    """
    A table widget for the equipment list.
    """

    def __init__(self, parent=None):
        super().__init__(parent)
        #self.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        #self.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

    def eventFilter(self, widget: QObject, event: QEvent):
        """
        TODO: Filter to make enter key do a newline. not working. maght have to be in the parent class.
        :param widget:
        :param event:
        :return:
        """
        # print('event')
        # event.type() == QEvent.KeyPress and
        if event.type() == QEvent.KeyPress and event.key() == Qt.Key_Enter:
            print('foo')
            # row = self.currentRow()
            # self.setCurrentCell(row, 2)
            # return True
        return QObject.eventFilter(self, widget, event)

    def add_equipment_row(self, key: str = '', value: str = ''):
        """
        Add a new row with content to the table (Equipment or Property).
        """
        if not isinstance(value, str):
            return
        if not isinstance(key, str):
            return
        # Create a empty row at bottom of table
        row_num = self.rowCount()
        self.insertRow(row_num)
        item_key = MyTableWidgetItem(key)
        self.setItem(row_num, 0, item_key)
        # if len(value) > 38:
        tab_item = MyQPlainTextEdit(self)
        tab_item.setFrameShape(0)
        tab_item.setPlainText(retranslate_delimiter(value))
        self.setCellWidget(row_num, 1, tab_item)

    def adjustToContents(self):
        print('adjust')
        self.resizeRowsToContents()
