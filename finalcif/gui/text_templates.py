# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/Users/daniel/Documents/GitHub/FinalCif/finalcif/gui/text_templates.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_TextTemplatesWidget(object):
    def setupUi(self, TextTemplatesWidget):
        TextTemplatesWidget.setObjectName("TextTemplatesWidget")
        TextTemplatesWidget.resize(883, 610)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(TextTemplatesWidget)
        self.verticalLayout_3.setContentsMargins(6, 6, 6, 6)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(6, -1, -1, 6)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.cifKeyLabel = QtWidgets.QLabel(TextTemplatesWidget)
        self.cifKeyLabel.setObjectName("cifKeyLabel")
        self.horizontalLayout.addWidget(self.cifKeyLabel)
        self.cifKeyLineEdit = QtWidgets.QLineEdit(TextTemplatesWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(40)
        sizePolicy.setHeightForWidth(self.cifKeyLineEdit.sizePolicy().hasHeightForWidth())
        self.cifKeyLineEdit.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.cifKeyLineEdit.setFont(font)
        self.cifKeyLineEdit.setText("")
        self.cifKeyLineEdit.setReadOnly(True)
        self.cifKeyLineEdit.setObjectName("cifKeyLineEdit")
        self.horizontalLayout.addWidget(self.cifKeyLineEdit)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        self.TemplatesListGroupBox = QtWidgets.QGroupBox(TextTemplatesWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(50)
        sizePolicy.setHeightForWidth(self.TemplatesListGroupBox.sizePolicy().hasHeightForWidth())
        self.TemplatesListGroupBox.setSizePolicy(sizePolicy)
        self.TemplatesListGroupBox.setObjectName("TemplatesListGroupBox")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.TemplatesListGroupBox)
        self.verticalLayout.setContentsMargins(-1, 6, -1, 6)
        self.verticalLayout.setObjectName("verticalLayout")
        self.templatesListWidget = QtWidgets.QListWidget(self.TemplatesListGroupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(60)
        sizePolicy.setHeightForWidth(self.templatesListWidget.sizePolicy().hasHeightForWidth())
        self.templatesListWidget.setSizePolicy(sizePolicy)
        self.templatesListWidget.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.templatesListWidget.setFrameShadow(QtWidgets.QFrame.Plain)
        self.templatesListWidget.setLineWidth(0)
        self.templatesListWidget.setAutoScroll(False)
        self.templatesListWidget.setSelectionMode(QtWidgets.QAbstractItemView.NoSelection)
        self.templatesListWidget.setVerticalScrollMode(QtWidgets.QAbstractItemView.ScrollPerPixel)
        self.templatesListWidget.setHorizontalScrollMode(QtWidgets.QAbstractItemView.ScrollPerPixel)
        self.templatesListWidget.setResizeMode(QtWidgets.QListView.Adjust)
        self.templatesListWidget.setObjectName("templatesListWidget")
        self.verticalLayout.addWidget(self.templatesListWidget)
        self.verticalLayout_3.addWidget(self.TemplatesListGroupBox)
        spacerItem1 = QtWidgets.QSpacerItem(20, 3, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_3.addItem(spacerItem1)
        self.combinedTestGroupBox = QtWidgets.QGroupBox(TextTemplatesWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(40)
        sizePolicy.setHeightForWidth(self.combinedTestGroupBox.sizePolicy().hasHeightForWidth())
        self.combinedTestGroupBox.setSizePolicy(sizePolicy)
        self.combinedTestGroupBox.setObjectName("combinedTestGroupBox")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.combinedTestGroupBox)
        self.verticalLayout_4.setContentsMargins(12, 6, 12, 6)
        self.verticalLayout_4.setSpacing(6)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.combinedTestGroupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.plainTextEdit.sizePolicy().hasHeightForWidth())
        self.plainTextEdit.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.plainTextEdit.setFont(font)
        self.plainTextEdit.setFrameShadow(QtWidgets.QFrame.Plain)
        self.plainTextEdit.setLineWidth(0)
        self.plainTextEdit.setBackgroundVisible(False)
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.verticalLayout_4.addWidget(self.plainTextEdit)
        self.verticalLayout_3.addWidget(self.combinedTestGroupBox)
        self.applaTextHorizontalLayout = QtWidgets.QHBoxLayout()
        self.applaTextHorizontalLayout.setObjectName("applaTextHorizontalLayout")
        self.applyTextPushButton = QtWidgets.QPushButton(TextTemplatesWidget)
        self.applyTextPushButton.setObjectName("applyTextPushButton")
        self.applaTextHorizontalLayout.addWidget(self.applyTextPushButton)
        self.cancelTextPushButton = QtWidgets.QPushButton(TextTemplatesWidget)
        self.cancelTextPushButton.setObjectName("cancelTextPushButton")
        self.applaTextHorizontalLayout.addWidget(self.cancelTextPushButton)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.applaTextHorizontalLayout.addItem(spacerItem2)
        self.savePushButton = QtWidgets.QPushButton(TextTemplatesWidget)
        self.savePushButton.setObjectName("savePushButton")
        self.applaTextHorizontalLayout.addWidget(self.savePushButton)
        self.importPushButton = QtWidgets.QPushButton(TextTemplatesWidget)
        self.importPushButton.setObjectName("importPushButton")
        self.applaTextHorizontalLayout.addWidget(self.importPushButton)
        self.exportTextPushButton = QtWidgets.QPushButton(TextTemplatesWidget)
        self.exportTextPushButton.setObjectName("exportTextPushButton")
        self.applaTextHorizontalLayout.addWidget(self.exportTextPushButton)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.applaTextHorizontalLayout.addItem(spacerItem3)
        self.deletePushButton = QtWidgets.QPushButton(TextTemplatesWidget)
        self.deletePushButton.setObjectName("deletePushButton")
        self.applaTextHorizontalLayout.addWidget(self.deletePushButton)
        self.verticalLayout_3.addLayout(self.applaTextHorizontalLayout)

        self.retranslateUi(TextTemplatesWidget)
        QtCore.QMetaObject.connectSlotsByName(TextTemplatesWidget)

    def retranslateUi(self, TextTemplatesWidget):
        _translate = QtCore.QCoreApplication.translate
        TextTemplatesWidget.setWindowTitle(_translate("TextTemplatesWidget", "TextTemplatesWidget"))
        self.cifKeyLabel.setText(_translate("TextTemplatesWidget", "CIF key:"))
        self.TemplatesListGroupBox.setTitle(_translate("TextTemplatesWidget", "Select template(s)"))
        self.combinedTestGroupBox.setTitle(_translate("TextTemplatesWidget", "Combined text"))
        self.plainTextEdit.setPlaceholderText(_translate("TextTemplatesWidget", "The text of the selected templates is added here in the order of selection."))
        self.applyTextPushButton.setText(_translate("TextTemplatesWidget", "Apply Text"))
        self.cancelTextPushButton.setText(_translate("TextTemplatesWidget", "Cancel"))
        self.savePushButton.setText(_translate("TextTemplatesWidget", "Save as Template"))
        self.importPushButton.setText(_translate("TextTemplatesWidget", "Import Template"))
        self.exportTextPushButton.setText(_translate("TextTemplatesWidget", "Export to CIF"))
        self.deletePushButton.setText(_translate("TextTemplatesWidget", "Delete Template"))
