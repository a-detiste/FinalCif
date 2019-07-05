# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\GitHub\FinalCif\./gui\finalcif_gui.ui'
#
# Created by: PyQt5 UI code generator 5.12.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_FinalCifWindow(object):
    def setupUi(self, FinalCifWindow):
        FinalCifWindow.setObjectName("FinalCifWindow")
        FinalCifWindow.resize(1400, 800)
        self.Mainwidget = QtWidgets.QWidget(FinalCifWindow)
        self.Mainwidget.setObjectName("Mainwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.Mainwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.RecentComboBox = QtWidgets.QComboBox(self.Mainwidget)
        self.RecentComboBox.setObjectName("RecentComboBox")
        self.RecentComboBox.addItem("")
        self.gridLayout.addWidget(self.RecentComboBox, 1, 1, 1, 1)
        self.EquipmentGroupBox = QtWidgets.QGroupBox(self.Mainwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(3)
        sizePolicy.setHeightForWidth(self.EquipmentGroupBox.sizePolicy().hasHeightForWidth())
        self.EquipmentGroupBox.setSizePolicy(sizePolicy)
        self.EquipmentGroupBox.setObjectName("EquipmentGroupBox")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.EquipmentGroupBox)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.EquipmentTemplatesStackedWidget = QtWidgets.QStackedWidget(self.EquipmentGroupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.EquipmentTemplatesStackedWidget.sizePolicy().hasHeightForWidth())
        self.EquipmentTemplatesStackedWidget.setSizePolicy(sizePolicy)
        self.EquipmentTemplatesStackedWidget.setObjectName("EquipmentTemplatesStackedWidget")
        self.EquipmentSelectPage = QtWidgets.QWidget()
        self.EquipmentSelectPage.setObjectName("EquipmentSelectPage")
        self.TemplatesGridLayout = QtWidgets.QGridLayout(self.EquipmentSelectPage)
        self.TemplatesGridLayout.setObjectName("TemplatesGridLayout")
        self.EditEquipmentTemplateButton = QtWidgets.QPushButton(self.EquipmentSelectPage)
        self.EditEquipmentTemplateButton.setObjectName("EditEquipmentTemplateButton")
        self.TemplatesGridLayout.addWidget(self.EditEquipmentTemplateButton, 1, 1, 1, 1)
        self.NewEquipmentTemplateButton = QtWidgets.QPushButton(self.EquipmentSelectPage)
        self.NewEquipmentTemplateButton.setObjectName("NewEquipmentTemplateButton")
        self.TemplatesGridLayout.addWidget(self.NewEquipmentTemplateButton, 1, 0, 1, 1)
        self.EquipmentTemplatesListWidget = QtWidgets.QListWidget(self.EquipmentSelectPage)
        self.EquipmentTemplatesListWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.EquipmentTemplatesListWidget.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.EquipmentTemplatesListWidget.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.EquipmentTemplatesListWidget.setObjectName("EquipmentTemplatesListWidget")
        self.TemplatesGridLayout.addWidget(self.EquipmentTemplatesListWidget, 0, 0, 1, 2)
        self.EquipmentTemplatesStackedWidget.addWidget(self.EquipmentSelectPage)
        self.EquipmentEditPage = QtWidgets.QWidget()
        self.EquipmentEditPage.setObjectName("EquipmentEditPage")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.EquipmentEditPage)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.DeleteEquipmentButton = QtWidgets.QPushButton(self.EquipmentEditPage)
        self.DeleteEquipmentButton.setObjectName("DeleteEquipmentButton")
        self.gridLayout_2.addWidget(self.DeleteEquipmentButton, 1, 1, 1, 1)
        self.SaveEquipmentButton = QtWidgets.QPushButton(self.EquipmentEditPage)
        self.SaveEquipmentButton.setObjectName("SaveEquipmentButton")
        self.gridLayout_2.addWidget(self.SaveEquipmentButton, 1, 2, 1, 1)
        self.CancelEquipmentButton = QtWidgets.QPushButton(self.EquipmentEditPage)
        self.CancelEquipmentButton.setObjectName("CancelEquipmentButton")
        self.gridLayout_2.addWidget(self.CancelEquipmentButton, 1, 3, 1, 1)
        self.EquipmentEditTableWidget = QtWidgets.QTableWidget(self.EquipmentEditPage)
        self.EquipmentEditTableWidget.setAutoScroll(False)
        self.EquipmentEditTableWidget.setEditTriggers(QtWidgets.QAbstractItemView.AllEditTriggers)
        self.EquipmentEditTableWidget.setAlternatingRowColors(False)
        self.EquipmentEditTableWidget.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.EquipmentEditTableWidget.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.EquipmentEditTableWidget.setVerticalScrollMode(QtWidgets.QAbstractItemView.ScrollPerPixel)
        self.EquipmentEditTableWidget.setHorizontalScrollMode(QtWidgets.QAbstractItemView.ScrollPerPixel)
        self.EquipmentEditTableWidget.setRowCount(1)
        self.EquipmentEditTableWidget.setObjectName("EquipmentEditTableWidget")
        self.EquipmentEditTableWidget.setColumnCount(2)
        item = QtWidgets.QTableWidgetItem()
        self.EquipmentEditTableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.EquipmentEditTableWidget.setHorizontalHeaderItem(1, item)
        self.EquipmentEditTableWidget.horizontalHeader().setDefaultSectionSize(170)
        self.EquipmentEditTableWidget.horizontalHeader().setMinimumSectionSize(90)
        self.EquipmentEditTableWidget.horizontalHeader().setStretchLastSection(True)
        self.EquipmentEditTableWidget.verticalHeader().setDefaultSectionSize(23)
        self.gridLayout_2.addWidget(self.EquipmentEditTableWidget, 0, 1, 1, 3)
        self.EquipmentTemplatesStackedWidget.addWidget(self.EquipmentEditPage)
        self.gridLayout_3.addWidget(self.EquipmentTemplatesStackedWidget, 0, 0, 1, 1)
        self.gridLayout.addWidget(self.EquipmentGroupBox, 5, 1, 1, 1)
        self.SelectCifFileGroupBox = QtWidgets.QGroupBox(self.Mainwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.SelectCifFileGroupBox.sizePolicy().hasHeightForWidth())
        self.SelectCifFileGroupBox.setSizePolicy(sizePolicy)
        self.SelectCifFileGroupBox.setObjectName("SelectCifFileGroupBox")
        self.CifFileGridLayout = QtWidgets.QGridLayout(self.SelectCifFileGroupBox)
        self.CifFileGridLayout.setObjectName("CifFileGridLayout")
        self.SelectCif_LineEdit = QtWidgets.QLineEdit(self.SelectCifFileGroupBox)
        self.SelectCif_LineEdit.setObjectName("SelectCif_LineEdit")
        self.CifFileGridLayout.addWidget(self.SelectCif_LineEdit, 0, 0, 1, 1)
        self.SelectCif_PushButton = QtWidgets.QPushButton(self.SelectCifFileGroupBox)
        self.SelectCif_PushButton.setObjectName("SelectCif_PushButton")
        self.CifFileGridLayout.addWidget(self.SelectCif_PushButton, 0, 1, 1, 1)
        self.gridLayout.addWidget(self.SelectCifFileGroupBox, 0, 1, 1, 1)
        self.CifDataItemsGroupBox = QtWidgets.QGroupBox(self.Mainwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(5)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.CifDataItemsGroupBox.sizePolicy().hasHeightForWidth())
        self.CifDataItemsGroupBox.setSizePolicy(sizePolicy)
        self.CifDataItemsGroupBox.setObjectName("CifDataItemsGroupBox")
        self.CifTableGridLayout = QtWidgets.QGridLayout(self.CifDataItemsGroupBox)
        self.CifTableGridLayout.setObjectName("CifTableGridLayout")
        spacerItem = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.CifTableGridLayout.addItem(spacerItem, 1, 1, 1, 1)
        self.CheckcifButton = QtWidgets.QPushButton(self.CifDataItemsGroupBox)
        self.CheckcifButton.setObjectName("CheckcifButton")
        self.CifTableGridLayout.addWidget(self.CheckcifButton, 2, 1, 1, 1)
        self.SaveFullReportButton = QtWidgets.QPushButton(self.CifDataItemsGroupBox)
        self.SaveFullReportButton.setObjectName("SaveFullReportButton")
        self.CifTableGridLayout.addWidget(self.SaveFullReportButton, 2, 2, 1, 1)
        self.CifItemsTable = QtWidgets.QTableWidget(self.CifDataItemsGroupBox)
        self.CifItemsTable.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustIgnored)
        self.CifItemsTable.setEditTriggers(QtWidgets.QAbstractItemView.AllEditTriggers)
        self.CifItemsTable.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.CifItemsTable.setVerticalScrollMode(QtWidgets.QAbstractItemView.ScrollPerPixel)
        self.CifItemsTable.setHorizontalScrollMode(QtWidgets.QAbstractItemView.ScrollPerPixel)
        self.CifItemsTable.setShowGrid(True)
        self.CifItemsTable.setCornerButtonEnabled(False)
        self.CifItemsTable.setObjectName("CifItemsTable")
        self.CifItemsTable.setColumnCount(3)
        self.CifItemsTable.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.CifItemsTable.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.CifItemsTable.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.CifItemsTable.setHorizontalHeaderItem(2, item)
        self.CifItemsTable.horizontalHeader().setDefaultSectionSize(152)
        self.CifItemsTable.horizontalHeader().setHighlightSections(False)
        self.CifItemsTable.horizontalHeader().setMinimumSectionSize(80)
        self.CifItemsTable.verticalHeader().setDefaultSectionSize(25)
        self.CifItemsTable.verticalHeader().setHighlightSections(True)
        self.CifItemsTable.verticalHeader().setMinimumSectionSize(19)
        self.CifTableGridLayout.addWidget(self.CifItemsTable, 0, 0, 1, 3)
        self.SaveCifButton = QtWidgets.QPushButton(self.CifDataItemsGroupBox)
        self.SaveCifButton.setObjectName("SaveCifButton")
        self.CifTableGridLayout.addWidget(self.SaveCifButton, 2, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.CifTableGridLayout.addItem(spacerItem1, 3, 1, 1, 1)
        self.gridLayout.addWidget(self.CifDataItemsGroupBox, 0, 4, 10, 1)
        self.PropertiesGroupBox = QtWidgets.QGroupBox(self.Mainwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.PropertiesGroupBox.sizePolicy().hasHeightForWidth())
        self.PropertiesGroupBox.setSizePolicy(sizePolicy)
        self.PropertiesGroupBox.setObjectName("PropertiesGroupBox")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.PropertiesGroupBox)
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_4.setHorizontalSpacing(6)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.PropertiesTemplatesStackedWidget = QtWidgets.QStackedWidget(self.PropertiesGroupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(2)
        sizePolicy.setVerticalStretch(2)
        sizePolicy.setHeightForWidth(self.PropertiesTemplatesStackedWidget.sizePolicy().hasHeightForWidth())
        self.PropertiesTemplatesStackedWidget.setSizePolicy(sizePolicy)
        self.PropertiesTemplatesStackedWidget.setObjectName("PropertiesTemplatesStackedWidget")
        self.PropertiesSelectPage = QtWidgets.QWidget()
        self.PropertiesSelectPage.setObjectName("PropertiesSelectPage")
        self.TemplatesGridLayout_2 = QtWidgets.QGridLayout(self.PropertiesSelectPage)
        self.TemplatesGridLayout_2.setObjectName("TemplatesGridLayout_2")
        self.NewPropertyTemplateButton = QtWidgets.QPushButton(self.PropertiesSelectPage)
        self.NewPropertyTemplateButton.setObjectName("NewPropertyTemplateButton")
        self.TemplatesGridLayout_2.addWidget(self.NewPropertyTemplateButton, 1, 0, 1, 1)
        self.PropertiesTemplatesListWidget = QtWidgets.QListWidget(self.PropertiesSelectPage)
        self.PropertiesTemplatesListWidget.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.PropertiesTemplatesListWidget.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.PropertiesTemplatesListWidget.setObjectName("PropertiesTemplatesListWidget")
        self.TemplatesGridLayout_2.addWidget(self.PropertiesTemplatesListWidget, 0, 0, 1, 2)
        self.EditPropertiyTemplateButton = QtWidgets.QPushButton(self.PropertiesSelectPage)
        self.EditPropertiyTemplateButton.setObjectName("EditPropertiyTemplateButton")
        self.TemplatesGridLayout_2.addWidget(self.EditPropertiyTemplateButton, 1, 1, 1, 1)
        self.PropertiesTemplatesStackedWidget.addWidget(self.PropertiesSelectPage)
        self.PropertiesEditPage = QtWidgets.QWidget()
        self.PropertiesEditPage.setObjectName("PropertiesEditPage")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.PropertiesEditPage)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.CancelPropertiesButton = QtWidgets.QPushButton(self.PropertiesEditPage)
        self.CancelPropertiesButton.setMinimumSize(QtCore.QSize(110, 0))
        self.CancelPropertiesButton.setObjectName("CancelPropertiesButton")
        self.gridLayout_5.addWidget(self.CancelPropertiesButton, 2, 3, 1, 1)
        self.PropertiesEditTableWidget = QtWidgets.QTableWidget(self.PropertiesEditPage)
        self.PropertiesEditTableWidget.setAutoScroll(False)
        self.PropertiesEditTableWidget.setEditTriggers(QtWidgets.QAbstractItemView.AllEditTriggers)
        self.PropertiesEditTableWidget.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.PropertiesEditTableWidget.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.PropertiesEditTableWidget.setVerticalScrollMode(QtWidgets.QAbstractItemView.ScrollPerPixel)
        self.PropertiesEditTableWidget.setHorizontalScrollMode(QtWidgets.QAbstractItemView.ScrollPerPixel)
        self.PropertiesEditTableWidget.setRowCount(1)
        self.PropertiesEditTableWidget.setObjectName("PropertiesEditTableWidget")
        self.PropertiesEditTableWidget.setColumnCount(1)
        item = QtWidgets.QTableWidgetItem()
        self.PropertiesEditTableWidget.setHorizontalHeaderItem(0, item)
        self.PropertiesEditTableWidget.horizontalHeader().setVisible(False)
        self.PropertiesEditTableWidget.horizontalHeader().setDefaultSectionSize(170)
        self.PropertiesEditTableWidget.horizontalHeader().setMinimumSectionSize(90)
        self.PropertiesEditTableWidget.horizontalHeader().setStretchLastSection(True)
        self.PropertiesEditTableWidget.verticalHeader().setVisible(False)
        self.PropertiesEditTableWidget.verticalHeader().setDefaultSectionSize(23)
        self.gridLayout_5.addWidget(self.PropertiesEditTableWidget, 1, 0, 1, 4)
        self.cifKeywordLB = QtWidgets.QLabel(self.PropertiesEditPage)
        self.cifKeywordLB.setObjectName("cifKeywordLB")
        self.gridLayout_5.addWidget(self.cifKeywordLB, 0, 0, 1, 1)
        self.cifKeywordLE = QtWidgets.QLineEdit(self.PropertiesEditPage)
        self.cifKeywordLE.setObjectName("cifKeywordLE")
        self.gridLayout_5.addWidget(self.cifKeywordLE, 0, 1, 1, 3)
        self.SavePropertiesButton = QtWidgets.QPushButton(self.PropertiesEditPage)
        self.SavePropertiesButton.setMinimumSize(QtCore.QSize(110, 0))
        self.SavePropertiesButton.setObjectName("SavePropertiesButton")
        self.gridLayout_5.addWidget(self.SavePropertiesButton, 2, 2, 1, 1)
        self.DeletePropertiesButton = QtWidgets.QPushButton(self.PropertiesEditPage)
        self.DeletePropertiesButton.setMinimumSize(QtCore.QSize(110, 0))
        self.DeletePropertiesButton.setObjectName("DeletePropertiesButton")
        self.gridLayout_5.addWidget(self.DeletePropertiesButton, 2, 1, 1, 1)
        self.PropertiesTemplatesStackedWidget.addWidget(self.PropertiesEditPage)
        self.gridLayout_4.addWidget(self.PropertiesTemplatesStackedWidget, 0, 0, 1, 2)
        self.gridLayout.addWidget(self.PropertiesGroupBox, 6, 1, 4, 1)
        FinalCifWindow.setCentralWidget(self.Mainwidget)
        self.statusBar = QtWidgets.QStatusBar(FinalCifWindow)
        self.statusBar.setObjectName("statusBar")
        FinalCifWindow.setStatusBar(self.statusBar)
        self.actionSave_Report = QtWidgets.QAction(FinalCifWindow)
        self.actionSave_Report.setObjectName("actionSave_Report")
        self.actionSave_CIF_File = QtWidgets.QAction(FinalCifWindow)
        self.actionSave_CIF_File.setObjectName("actionSave_CIF_File")
        self.actionedit_templates = QtWidgets.QAction(FinalCifWindow)
        self.actionedit_templates.setObjectName("actionedit_templates")

        self.retranslateUi(FinalCifWindow)
        self.EquipmentTemplatesStackedWidget.setCurrentIndex(0)
        self.PropertiesTemplatesStackedWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(FinalCifWindow)
        FinalCifWindow.setTabOrder(self.SelectCif_LineEdit, self.EquipmentEditTableWidget)
        FinalCifWindow.setTabOrder(self.EquipmentEditTableWidget, self.cifKeywordLE)
        FinalCifWindow.setTabOrder(self.cifKeywordLE, self.PropertiesEditTableWidget)
        FinalCifWindow.setTabOrder(self.PropertiesEditTableWidget, self.CifItemsTable)
        FinalCifWindow.setTabOrder(self.CifItemsTable, self.SelectCif_PushButton)
        FinalCifWindow.setTabOrder(self.SelectCif_PushButton, self.SaveCifButton)
        FinalCifWindow.setTabOrder(self.SaveCifButton, self.NewPropertyTemplateButton)
        FinalCifWindow.setTabOrder(self.NewPropertyTemplateButton, self.PropertiesTemplatesListWidget)
        FinalCifWindow.setTabOrder(self.PropertiesTemplatesListWidget, self.EditPropertiyTemplateButton)
        FinalCifWindow.setTabOrder(self.EditPropertiyTemplateButton, self.EditEquipmentTemplateButton)
        FinalCifWindow.setTabOrder(self.EditEquipmentTemplateButton, self.CheckcifButton)
        FinalCifWindow.setTabOrder(self.CheckcifButton, self.SaveFullReportButton)
        FinalCifWindow.setTabOrder(self.SaveFullReportButton, self.NewEquipmentTemplateButton)
        FinalCifWindow.setTabOrder(self.NewEquipmentTemplateButton, self.EquipmentTemplatesListWidget)

    def retranslateUi(self, FinalCifWindow):
        _translate = QtCore.QCoreApplication.translate
        FinalCifWindow.setWindowTitle(_translate("FinalCifWindow", "FinalCif"))
        self.RecentComboBox.setItemText(0, _translate("FinalCifWindow", "Recent Files"))
        self.EquipmentGroupBox.setTitle(_translate("FinalCifWindow", "Equipment and Author Templates"))
        self.EditEquipmentTemplateButton.setText(_translate("FinalCifWindow", "Edit Template"))
        self.NewEquipmentTemplateButton.setText(_translate("FinalCifWindow", "New Template"))
        self.EquipmentTemplatesListWidget.setToolTip(_translate("FinalCifWindow", "<html><head/><body><p>A list of diffractometer Equipment like: D8 VENTURE</p></body></html>"))
        self.DeleteEquipmentButton.setText(_translate("FinalCifWindow", "Delete Template"))
        self.SaveEquipmentButton.setText(_translate("FinalCifWindow", "Save"))
        self.CancelEquipmentButton.setText(_translate("FinalCifWindow", "Cancel"))
        item = self.EquipmentEditTableWidget.horizontalHeaderItem(0)
        item.setText(_translate("FinalCifWindow", "key"))
        item = self.EquipmentEditTableWidget.horizontalHeaderItem(1)
        item.setText(_translate("FinalCifWindow", "value"))
        self.SelectCifFileGroupBox.setTitle(_translate("FinalCifWindow", "Cif file"))
        self.SelectCif_LineEdit.setPlaceholderText(_translate("FinalCifWindow", "Select a .cif file first."))
        self.SelectCif_PushButton.setText(_translate("FinalCifWindow", "Select File"))
        self.CifDataItemsGroupBox.setTitle(_translate("FinalCifWindow", "Missing CIF Items"))
        self.CheckcifButton.setText(_translate("FinalCifWindow", "CheckCif"))
        self.SaveFullReportButton.setText(_translate("FinalCifWindow", "Make Tables"))
        self.CifItemsTable.setSortingEnabled(False)
        item = self.CifItemsTable.horizontalHeaderItem(0)
        item.setText(_translate("FinalCifWindow", "CIF Value"))
        item = self.CifItemsTable.horizontalHeaderItem(1)
        item.setText(_translate("FinalCifWindow", "From Data Source"))
        item = self.CifItemsTable.horizontalHeaderItem(2)
        item.setText(_translate("FinalCifWindow", "Own Data"))
        self.SaveCifButton.setToolTip(_translate("FinalCifWindow", "Saves the cif file to name-final.cif"))
        self.SaveCifButton.setText(_translate("FinalCifWindow", "Save Cif File"))
        self.PropertiesGroupBox.setTitle(_translate("FinalCifWindow", "Properties Templates"))
        self.NewPropertyTemplateButton.setText(_translate("FinalCifWindow", "New Template"))
        self.PropertiesTemplatesListWidget.setToolTip(_translate("FinalCifWindow", "<html><head/><body><p>A list of common properties like colour: yellow, red, blue, ...</p></body></html>"))
        self.EditPropertiyTemplateButton.setText(_translate("FinalCifWindow", "Edit Template"))
        self.CancelPropertiesButton.setText(_translate("FinalCifWindow", "Cancel"))
        item = self.PropertiesEditTableWidget.horizontalHeaderItem(0)
        item.setText(_translate("FinalCifWindow", "possible values"))
        self.cifKeywordLB.setText(_translate("FinalCifWindow", "cif keyword"))
        self.SavePropertiesButton.setText(_translate("FinalCifWindow", "Save"))
        self.DeletePropertiesButton.setText(_translate("FinalCifWindow", "Delete Template"))
        self.actionSave_Report.setText(_translate("FinalCifWindow", "Save Report"))
        self.actionSave_CIF_File.setText(_translate("FinalCifWindow", "Save CIF File"))
        self.actionedit_templates.setText(_translate("FinalCifWindow", "edit templates"))


