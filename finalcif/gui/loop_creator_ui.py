# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/Users/daniel/Documents/GitHub/FinalCif/finalcif/gui/loop_creator_ui.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_LoopCreator(object):
    def setupUi(self, LoopCreator):
        LoopCreator.setObjectName("LoopCreator")
        LoopCreator.resize(800, 600)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(LoopCreator)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_2 = QtWidgets.QLabel(LoopCreator)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(LoopCreator)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.searchLineEdit = QtWidgets.QLineEdit(LoopCreator)
        self.searchLineEdit.setObjectName("searchLineEdit")
        self.horizontalLayout.addWidget(self.searchLineEdit)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.availableKeysListWidget = QtWidgets.QListWidget(LoopCreator)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.availableKeysListWidget.setFont(font)
        self.availableKeysListWidget.setObjectName("availableKeysListWidget")
        self.verticalLayout_2.addWidget(self.availableKeysListWidget)
        self.horizontalLayout_2.addLayout(self.verticalLayout_2)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setContentsMargins(0, -1, -1, -1)
        self.verticalLayout.setObjectName("verticalLayout")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.leftPushButton = QtWidgets.QPushButton(LoopCreator)
        self.leftPushButton.setObjectName("leftPushButton")
        self.verticalLayout.addWidget(self.leftPushButton)
        self.rightPushButton = QtWidgets.QPushButton(LoopCreator)
        self.rightPushButton.setObjectName("rightPushButton")
        self.verticalLayout.addWidget(self.rightPushButton)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.horizontalLayout_2.addLayout(self.verticalLayout)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_3 = QtWidgets.QLabel(LoopCreator)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_3.addWidget(self.label_3)
        self.label_4 = QtWidgets.QLabel(LoopCreator)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_3.addWidget(self.label_4)
        self.selectedKeysListWidget = QtWidgets.QListWidget(LoopCreator)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.selectedKeysListWidget.setFont(font)
        self.selectedKeysListWidget.setObjectName("selectedKeysListWidget")
        self.verticalLayout_3.addWidget(self.selectedKeysListWidget)
        self.SaveLoopPushButton = QtWidgets.QPushButton(LoopCreator)
        self.SaveLoopPushButton.setObjectName("SaveLoopPushButton")
        self.verticalLayout_3.addWidget(self.SaveLoopPushButton)
        self.horizontalLayout_2.addLayout(self.verticalLayout_3)

        self.retranslateUi(LoopCreator)
        QtCore.QMetaObject.connectSlotsByName(LoopCreator)

    def retranslateUi(self, LoopCreator):
        _translate = QtCore.QCoreApplication.translate
        LoopCreator.setWindowTitle(_translate("LoopCreator", "LoopCreator"))
        self.label_2.setText(_translate("LoopCreator", "<html><head/><body><p><span style=\" font-size:18pt;\">Available CIF keywords</span></p></body></html>"))
        self.label.setText(_translate("LoopCreator", "Search a Key"))
        self.leftPushButton.setText(_translate("LoopCreator", "<--"))
        self.rightPushButton.setText(_translate("LoopCreator", "-->"))
        self.label_3.setText(_translate("LoopCreator", "<html><head/><body><p><span style=\" font-size:18pt;\">New Loop Header</span></p></body></html>"))
        self.label_4.setText(_translate("LoopCreator", "Add CIF keys in order to create a new loop"))
        self.SaveLoopPushButton.setText(_translate("LoopCreator", "Save new Loop"))
