# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\_DEV\GitHub\FinalCif\finalcif\gui\new_key_dialog_ui.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_AddKeyWindow(object):
    def setupUi(self, AddKeyWindow):
        AddKeyWindow.setObjectName("AddKeyWindow")
        AddKeyWindow.resize(528, 445)
        self.centralwidget = QtWidgets.QWidget(AddKeyWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.searchLabel = QtWidgets.QLabel(self.centralwidget)
        self.searchLabel.setObjectName("searchLabel")
        self.horizontalLayout.addWidget(self.searchLabel)
        self.searchLineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.searchLineEdit.setObjectName("searchLineEdit")
        self.horizontalLayout.addWidget(self.searchLineEdit)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.keysListWidget = QtWidgets.QListWidget(self.centralwidget)
        self.keysListWidget.setProperty("showDropIndicator", False)
        self.keysListWidget.setSelectionMode(QtWidgets.QAbstractItemView.MultiSelection)
        self.keysListWidget.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectItems)
        self.keysListWidget.setObjectName("keysListWidget")
        self.verticalLayout.addWidget(self.keysListWidget)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.addKeyPushButton = QtWidgets.QPushButton(self.centralwidget)
        self.addKeyPushButton.setObjectName("addKeyPushButton")
        self.horizontalLayout_2.addWidget(self.addKeyPushButton)
        self.cancelPushButton = QtWidgets.QPushButton(self.centralwidget)
        self.cancelPushButton.setObjectName("cancelPushButton")
        self.horizontalLayout_2.addWidget(self.cancelPushButton)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        AddKeyWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(AddKeyWindow)
        QtCore.QMetaObject.connectSlotsByName(AddKeyWindow)

    def retranslateUi(self, AddKeyWindow):
        _translate = QtCore.QCoreApplication.translate
        AddKeyWindow.setWindowTitle(_translate("AddKeyWindow", "MainWindow"))
        self.searchLabel.setText(_translate("AddKeyWindow", "Search"))
        self.addKeyPushButton.setText(_translate("AddKeyWindow", "Add Key(s)"))
        self.cancelPushButton.setText(_translate("AddKeyWindow", "Close"))
