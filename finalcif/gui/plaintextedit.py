from contextlib import suppress

from PyQt5.QtCore import pyqtSignal, Qt, QObject, QEvent, QSize
from PyQt5.QtGui import QTextOption, QFontMetrics, QContextMenuEvent
from PyQt5.QtWidgets import QPlainTextEdit, QFrame, QApplication, QAbstractScrollArea

with suppress(ImportError):
    from finalcif.gui.custom_classes import MyCifTable


class MyQPlainTextEdit(QPlainTextEdit):
    """
    A special plaintextedit with convenient methods to set the background color and other things.
    """
    templateRequested = pyqtSignal(int)

    def __init__(self, parent=None, minheight: int = 80, *args, **kwargs):
        """
        Plaintext edit field for most of the table cells.
        :param parent:
        :param minheight: minimum height of the widget.
        """
        super().__init__(parent, *args, **kwargs)
        self.setParent(parent)
        self.cif_key = ''
        self.parent: 'MyCifTable' = parent
        self.setFocusPolicy(Qt.StrongFocus)
        self.setFrameShape(QFrame.NoFrame)
        self.setTabChangesFocus(True)
        self.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.setWordWrapMode(QTextOption.WordWrap)
        self.fontmetric = QFontMetrics(self.document().defaultFont())
        self.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.textChanged.connect(lambda: self.parent.resizeRowsToContents())

    def __str__(self):
        return self.toPlainText()

    def contextMenuEvent(self, event: QContextMenuEvent):
        menu = self.createStandardContextMenu(event.pos())
        action_copy_vhead = menu.addAction("Copy CIF Keyword")
        deleterow = menu.addAction("Delete Row")
        menu.addSeparator()
        action_template = menu.addAction("Text Template")
        action_copy_vhead.triggered.connect(self.copy_vhead_item)
        action_template.triggered.connect(self._on_create_template)
        deleterow.triggered.connect(self._delete_row)
        choosed_action = menu.exec(event.globalPos())

    def _on_create_template(self):
        self.templateRequested.emit(self.row)

    def _delete_row(self):
        self.parent.delete_row(self.row)

    def copy_vhead_item(self, row):
        """
        Copies the content of a field.
        """
        if hasattr(self.parent, 'vheaderitems'):
            clipboard = QApplication.clipboard()
            clipboard.setText(self.cif_key)

    @property
    def row(self) -> int:
        return self.parent.vheaderitems.index(self.cif_key)

    def setBackground(self, color):
        """
        Set background color of the text field.
        """
        self.setStyleSheet("background-color: {};".format(str(color.name())))
        # No idea why tis does not work
        # pal = self.palette()
        # pal.setColor(QPalette.Base, color)
        # self.setPalette(pal)

    def setUneditable(self):
        self.setReadOnly(True)

    def setText(self, text: str, color=None):
        """
        Set text of a Plaintextfield with lines wrapped at newline characters.
        """
        if color:
            self.setBackground(color)
        txtlst = text.split(r'\n')
        # special treatment for text fields in order to get line breaks:
        for txt in txtlst:
            self.setPlainText(txt)

    def eventFilter(self, widget: QObject, event: QEvent):
        """
        Event filter to ignore wheel events in comboboxes to prevent accidental changes to them.
        """
        if event.type() == QEvent.Wheel and widget and not widget.hasFocus():
            event.ignore()
            return True
        return QObject.eventFilter(self, widget, event)

    def getText(self):
        return self.toPlainText()

    def sizeHint(self) -> QSize:
        """Text field sizes are scaled to text length"""
        rect = self.fontmetric.boundingRect(self.contentsRect(), Qt.TextWordWrap, self.toPlainText())
        size = QSize(100, rect.height() + 14)
        if size.height() > 300:
            # Prevent extreme height for long text:
            size = QSize(100, 300)
        return size
