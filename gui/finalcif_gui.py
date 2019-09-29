# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/Users/daniel/GitHub/FinalCif/./gui/finalcif_gui.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_FinalCifWindow(object):
    def setupUi(self, FinalCifWindow):
        FinalCifWindow.setObjectName("FinalCifWindow")
        FinalCifWindow.resize(1400, 800)
        self.Mainwidget = QtWidgets.QWidget(FinalCifWindow)
        self.Mainwidget.setObjectName("Mainwidget")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.Mainwidget)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.splitter = QtWidgets.QSplitter(self.Mainwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.splitter.sizePolicy().hasHeightForWidth())
        self.splitter.setSizePolicy(sizePolicy)
        self.splitter.setStyleSheet("QSplitter::handle {\n"
"    background-color: rgb(200, 200, 200);\n"
"    margin: 0px 0px;\n"
"}")
        self.splitter.setLineWidth(0)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setHandleWidth(3)
        self.splitter.setObjectName("splitter")
        self.LeftFrame = QtWidgets.QFrame(self.splitter)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(6)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.LeftFrame.sizePolicy().hasHeightForWidth())
        self.LeftFrame.setSizePolicy(sizePolicy)
        self.LeftFrame.setMinimumSize(QtCore.QSize(0, 0))
        self.LeftFrame.setBaseSize(QtCore.QSize(0, 0))
        self.LeftFrame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.LeftFrame.setFrameShadow(QtWidgets.QFrame.Plain)
        self.LeftFrame.setLineWidth(0)
        self.LeftFrame.setObjectName("LeftFrame")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.LeftFrame)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, -1)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.SelectCifFileGroupBox = QtWidgets.QGroupBox(self.LeftFrame)
        self.SelectCifFileGroupBox.setObjectName("SelectCifFileGroupBox")
        self.CifFileGridLayout = QtWidgets.QGridLayout(self.SelectCifFileGroupBox)
        self.CifFileGridLayout.setHorizontalSpacing(4)
        self.CifFileGridLayout.setVerticalSpacing(8)
        self.CifFileGridLayout.setObjectName("CifFileGridLayout")
        self.SelectCif_PushButton = QtWidgets.QPushButton(self.SelectCifFileGroupBox)
        self.SelectCif_PushButton.setObjectName("SelectCif_PushButton")
        self.CifFileGridLayout.addWidget(self.SelectCif_PushButton, 0, 1, 1, 1)
        self.SelectCif_LineEdit = QtWidgets.QLineEdit(self.SelectCifFileGroupBox)
        self.SelectCif_LineEdit.setObjectName("SelectCif_LineEdit")
        self.CifFileGridLayout.addWidget(self.SelectCif_LineEdit, 0, 0, 1, 1)
        self.RecentComboBox = QtWidgets.QComboBox(self.SelectCifFileGroupBox)
        self.RecentComboBox.setObjectName("RecentComboBox")
        self.RecentComboBox.addItem("")
        self.CifFileGridLayout.addWidget(self.RecentComboBox, 1, 0, 1, 2)
        self.verticalLayout_5.addWidget(self.SelectCifFileGroupBox)
        self.EquipmentGroupBox = QtWidgets.QGroupBox(self.LeftFrame)
        self.EquipmentGroupBox.setObjectName("EquipmentGroupBox")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.EquipmentGroupBox)
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 1)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.EquipmentTemplatesStackedWidget = QtWidgets.QStackedWidget(self.EquipmentGroupBox)
        self.EquipmentTemplatesStackedWidget.setObjectName("EquipmentTemplatesStackedWidget")
        self.EquipmentSelectPage = QtWidgets.QWidget()
        self.EquipmentSelectPage.setObjectName("EquipmentSelectPage")
        self.TemplatesGridLayout = QtWidgets.QGridLayout(self.EquipmentSelectPage)
        self.TemplatesGridLayout.setObjectName("TemplatesGridLayout")
        self.EquipmentTemplatesListWidget = QtWidgets.QListWidget(self.EquipmentSelectPage)
        self.EquipmentTemplatesListWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.EquipmentTemplatesListWidget.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.EquipmentTemplatesListWidget.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.EquipmentTemplatesListWidget.setObjectName("EquipmentTemplatesListWidget")
        self.TemplatesGridLayout.addWidget(self.EquipmentTemplatesListWidget, 0, 0, 1, 3)
        self.NewEquipmentTemplateButton = QtWidgets.QPushButton(self.EquipmentSelectPage)
        self.NewEquipmentTemplateButton.setObjectName("NewEquipmentTemplateButton")
        self.TemplatesGridLayout.addWidget(self.NewEquipmentTemplateButton, 1, 0, 1, 1)
        self.EditEquipmentTemplateButton = QtWidgets.QPushButton(self.EquipmentSelectPage)
        self.EditEquipmentTemplateButton.setObjectName("EditEquipmentTemplateButton")
        self.TemplatesGridLayout.addWidget(self.EditEquipmentTemplateButton, 1, 1, 1, 1)
        self.ImportEquipmentTemplateButton = QtWidgets.QPushButton(self.EquipmentSelectPage)
        self.ImportEquipmentTemplateButton.setObjectName("ImportEquipmentTemplateButton")
        self.TemplatesGridLayout.addWidget(self.ImportEquipmentTemplateButton, 1, 2, 1, 1)
        self.EquipmentTemplatesStackedWidget.addWidget(self.EquipmentSelectPage)
        self.EquipmentEditPage = QtWidgets.QWidget()
        self.EquipmentEditPage.setObjectName("EquipmentEditPage")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.EquipmentEditPage)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.EquipmentEditTableWidget = MyEQTableWidget(self.EquipmentEditPage)
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
        self.EquipmentEditTableWidget.horizontalHeader().setCascadingSectionResizes(True)
        self.EquipmentEditTableWidget.horizontalHeader().setDefaultSectionSize(210)
        self.EquipmentEditTableWidget.horizontalHeader().setMinimumSectionSize(100)
        self.EquipmentEditTableWidget.horizontalHeader().setSortIndicatorShown(True)
        self.EquipmentEditTableWidget.horizontalHeader().setStretchLastSection(True)
        self.EquipmentEditTableWidget.verticalHeader().setVisible(False)
        self.EquipmentEditTableWidget.verticalHeader().setDefaultSectionSize(30)
        self.gridLayout_2.addWidget(self.EquipmentEditTableWidget, 0, 1, 1, 4)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.DeleteEquipmentButton = QtWidgets.QPushButton(self.EquipmentEditPage)
        self.DeleteEquipmentButton.setObjectName("DeleteEquipmentButton")
        self.horizontalLayout_5.addWidget(self.DeleteEquipmentButton)
        self.SaveEquipmentButton = QtWidgets.QPushButton(self.EquipmentEditPage)
        self.SaveEquipmentButton.setObjectName("SaveEquipmentButton")
        self.horizontalLayout_5.addWidget(self.SaveEquipmentButton)
        self.CancelEquipmentButton = QtWidgets.QPushButton(self.EquipmentEditPage)
        self.CancelEquipmentButton.setObjectName("CancelEquipmentButton")
        self.horizontalLayout_5.addWidget(self.CancelEquipmentButton)
        self.ExportEquipmentButton = QtWidgets.QPushButton(self.EquipmentEditPage)
        self.ExportEquipmentButton.setObjectName("ExportEquipmentButton")
        self.horizontalLayout_5.addWidget(self.ExportEquipmentButton)
        self.gridLayout_2.addLayout(self.horizontalLayout_5, 2, 1, 1, 4)
        self.EquipmentTemplatesStackedWidget.addWidget(self.EquipmentEditPage)
        self.verticalLayout_7.addWidget(self.EquipmentTemplatesStackedWidget)
        self.verticalLayout_5.addWidget(self.EquipmentGroupBox)
        self.PropertiesGroupBox = QtWidgets.QGroupBox(self.LeftFrame)
        self.PropertiesGroupBox.setObjectName("PropertiesGroupBox")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.PropertiesGroupBox)
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 1)
        self.verticalLayout_6.setSpacing(6)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.PropertiesTemplatesStackedWidget = QtWidgets.QStackedWidget(self.PropertiesGroupBox)
        self.PropertiesTemplatesStackedWidget.setObjectName("PropertiesTemplatesStackedWidget")
        self.PropertiesSelectPage = QtWidgets.QWidget()
        self.PropertiesSelectPage.setObjectName("PropertiesSelectPage")
        self.TemplatesGridLayout_2 = QtWidgets.QGridLayout(self.PropertiesSelectPage)
        self.TemplatesGridLayout_2.setObjectName("TemplatesGridLayout_2")
        self.NewPropertyTemplateButton = QtWidgets.QPushButton(self.PropertiesSelectPage)
        self.NewPropertyTemplateButton.setObjectName("NewPropertyTemplateButton")
        self.TemplatesGridLayout_2.addWidget(self.NewPropertyTemplateButton, 1, 0, 1, 1)
        self.EditPropertyTemplateButton = QtWidgets.QPushButton(self.PropertiesSelectPage)
        self.EditPropertyTemplateButton.setObjectName("EditPropertyTemplateButton")
        self.TemplatesGridLayout_2.addWidget(self.EditPropertyTemplateButton, 1, 1, 1, 1)
        self.ImportPropertyTemplateButton = QtWidgets.QPushButton(self.PropertiesSelectPage)
        self.ImportPropertyTemplateButton.setObjectName("ImportPropertyTemplateButton")
        self.TemplatesGridLayout_2.addWidget(self.ImportPropertyTemplateButton, 1, 2, 1, 1)
        self.PropertiesTemplatesListWidget = QtWidgets.QListWidget(self.PropertiesSelectPage)
        self.PropertiesTemplatesListWidget.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.PropertiesTemplatesListWidget.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.PropertiesTemplatesListWidget.setObjectName("PropertiesTemplatesListWidget")
        self.TemplatesGridLayout_2.addWidget(self.PropertiesTemplatesListWidget, 0, 0, 1, 3)
        self.PropertiesTemplatesStackedWidget.addWidget(self.PropertiesSelectPage)
        self.PropertiesEditPage = QtWidgets.QWidget()
        self.PropertiesEditPage.setObjectName("PropertiesEditPage")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.PropertiesEditPage)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.DeletePropertiesButton = QtWidgets.QPushButton(self.PropertiesEditPage)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.DeletePropertiesButton.sizePolicy().hasHeightForWidth())
        self.DeletePropertiesButton.setSizePolicy(sizePolicy)
        self.DeletePropertiesButton.setObjectName("DeletePropertiesButton")
        self.horizontalLayout.addWidget(self.DeletePropertiesButton)
        self.SavePropertiesButton = QtWidgets.QPushButton(self.PropertiesEditPage)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.SavePropertiesButton.sizePolicy().hasHeightForWidth())
        self.SavePropertiesButton.setSizePolicy(sizePolicy)
        self.SavePropertiesButton.setObjectName("SavePropertiesButton")
        self.horizontalLayout.addWidget(self.SavePropertiesButton)
        self.CancelPropertiesButton = QtWidgets.QPushButton(self.PropertiesEditPage)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.CancelPropertiesButton.sizePolicy().hasHeightForWidth())
        self.CancelPropertiesButton.setSizePolicy(sizePolicy)
        self.CancelPropertiesButton.setObjectName("CancelPropertiesButton")
        self.horizontalLayout.addWidget(self.CancelPropertiesButton)
        self.ExportPropertyButton = QtWidgets.QPushButton(self.PropertiesEditPage)
        self.ExportPropertyButton.setObjectName("ExportPropertyButton")
        self.horizontalLayout.addWidget(self.ExportPropertyButton)
        self.gridLayout_5.addLayout(self.horizontalLayout, 2, 0, 2, 6)
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
        self.PropertiesEditTableWidget.verticalHeader().setDefaultSectionSize(30)
        self.gridLayout_5.addWidget(self.PropertiesEditTableWidget, 1, 0, 1, 6)
        self.cifKeywordLB = QtWidgets.QLabel(self.PropertiesEditPage)
        self.cifKeywordLB.setObjectName("cifKeywordLB")
        self.gridLayout_5.addWidget(self.cifKeywordLB, 0, 0, 1, 1)
        self.cifKeywordLineEdit = QtWidgets.QLineEdit(self.PropertiesEditPage)
        self.cifKeywordLineEdit.setObjectName("cifKeywordLineEdit")
        self.gridLayout_5.addWidget(self.cifKeywordLineEdit, 0, 1, 1, 5)
        self.PropertiesTemplatesStackedWidget.addWidget(self.PropertiesEditPage)
        self.verticalLayout_6.addWidget(self.PropertiesTemplatesStackedWidget)
        self.verticalLayout_5.addWidget(self.PropertiesGroupBox)
        self.CifDataItemsFrame = QtWidgets.QFrame(self.splitter)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(9)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.CifDataItemsFrame.sizePolicy().hasHeightForWidth())
        self.CifDataItemsFrame.setSizePolicy(sizePolicy)
        self.CifDataItemsFrame.setMinimumSize(QtCore.QSize(0, 0))
        self.CifDataItemsFrame.setBaseSize(QtCore.QSize(0, 0))
        self.CifDataItemsFrame.setObjectName("CifDataItemsFrame")
        self.CifTableGridLayout = QtWidgets.QGridLayout(self.CifDataItemsFrame)
        self.CifTableGridLayout.setContentsMargins(0, 0, 0, 0)
        self.CifTableGridLayout.setObjectName("CifTableGridLayout")
        self.MainStackedWidget = QtWidgets.QStackedWidget(self.CifDataItemsFrame)
        self.MainStackedWidget.setObjectName("MainStackedWidget")
        self.page_MainTable = QtWidgets.QWidget()
        self.page_MainTable.setObjectName("page_MainTable")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.page_MainTable)
        self.verticalLayout.setObjectName("verticalLayout")
        self.CifItemsTable = MyCifTable(self.page_MainTable)
        self.CifItemsTable.setAutoScroll(False)
        self.CifItemsTable.setEditTriggers(QtWidgets.QAbstractItemView.AllEditTriggers)
        self.CifItemsTable.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.CifItemsTable.setVerticalScrollMode(QtWidgets.QAbstractItemView.ScrollPerPixel)
        self.CifItemsTable.setHorizontalScrollMode(QtWidgets.QAbstractItemView.ScrollPerPixel)
        self.CifItemsTable.setShowGrid(True)
        self.CifItemsTable.setWordWrap(True)
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
        self.CifItemsTable.verticalHeader().setMinimumSectionSize(20)
        self.verticalLayout.addWidget(self.CifItemsTable)
        self.ButtonsHorizontalLayout = QtWidgets.QHBoxLayout()
        self.ButtonsHorizontalLayout.setObjectName("ButtonsHorizontalLayout")
        self.groupBox = QtWidgets.QGroupBox(self.page_MainTable)
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.SaveCifButton = QtWidgets.QPushButton(self.groupBox)
        self.SaveCifButton.setObjectName("SaveCifButton")
        self.gridLayout_7.addWidget(self.SaveCifButton, 0, 0, 1, 1)
        self.ExploreDirButton = QtWidgets.QPushButton(self.groupBox)
        self.ExploreDirButton.setObjectName("ExploreDirButton")
        self.gridLayout_7.addWidget(self.ExploreDirButton, 1, 0, 1, 1)
        self.ButtonsHorizontalLayout.addWidget(self.groupBox)
        self.groupBox_checkcif = QtWidgets.QGroupBox(self.page_MainTable)
        self.groupBox_checkcif.setTitle("")
        self.groupBox_checkcif.setObjectName("groupBox_checkcif")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.groupBox_checkcif)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.CheckcifPDFOnlineButton = QtWidgets.QPushButton(self.groupBox_checkcif)
        self.CheckcifPDFOnlineButton.setObjectName("CheckcifPDFOnlineButton")
        self.gridLayout_6.addWidget(self.CheckcifPDFOnlineButton, 0, 1, 1, 1)
        self.CheckcifOnlineButton = QtWidgets.QPushButton(self.groupBox_checkcif)
        self.CheckcifOnlineButton.setObjectName("CheckcifOnlineButton")
        self.gridLayout_6.addWidget(self.CheckcifOnlineButton, 0, 0, 1, 1)
        self.CheckcifButton = QtWidgets.QPushButton(self.groupBox_checkcif)
        self.CheckcifButton.setObjectName("CheckcifButton")
        self.gridLayout_6.addWidget(self.CheckcifButton, 1, 0, 1, 1)
        self.structfactCheckBox = QtWidgets.QCheckBox(self.groupBox_checkcif)
        self.structfactCheckBox.setObjectName("structfactCheckBox")
        self.gridLayout_6.addWidget(self.structfactCheckBox, 1, 1, 1, 1)
        self.ButtonsHorizontalLayout.addWidget(self.groupBox_checkcif)
        self.groupBox_tables = QtWidgets.QGroupBox(self.page_MainTable)
        self.groupBox_tables.setTitle("")
        self.groupBox_tables.setObjectName("groupBox_tables")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.groupBox_tables)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.SaveFullReportButton = QtWidgets.QPushButton(self.groupBox_tables)
        self.SaveFullReportButton.setObjectName("SaveFullReportButton")
        self.verticalLayout_4.addWidget(self.SaveFullReportButton)
        self.HAtomsCheckBox = QtWidgets.QCheckBox(self.groupBox_tables)
        self.HAtomsCheckBox.setObjectName("HAtomsCheckBox")
        self.verticalLayout_4.addWidget(self.HAtomsCheckBox)
        self.ButtonsHorizontalLayout.addWidget(self.groupBox_tables)
        self.verticalLayout.addLayout(self.ButtonsHorizontalLayout)
        self.MainStackedWidget.addWidget(self.page_MainTable)
        self.page_checkcif = QtWidgets.QWidget()
        self.page_checkcif.setObjectName("page_checkcif")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.page_checkcif)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label = QtWidgets.QLabel(self.page_checkcif)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.CheckcifPlaintextEdit = QtWidgets.QPlainTextEdit(self.page_checkcif)
        self.CheckcifPlaintextEdit.setLineWrapMode(QtWidgets.QPlainTextEdit.NoWrap)
        self.CheckcifPlaintextEdit.setReadOnly(True)
        self.CheckcifPlaintextEdit.setPlainText("")
        self.CheckcifPlaintextEdit.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextSelectableByKeyboard|QtCore.Qt.TextSelectableByMouse)
        self.CheckcifPlaintextEdit.setObjectName("CheckcifPlaintextEdit")
        self.verticalLayout_2.addWidget(self.CheckcifPlaintextEdit)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.BacktoMainpushButton = QtWidgets.QPushButton(self.page_checkcif)
        self.BacktoMainpushButton.setObjectName("BacktoMainpushButton")
        self.horizontalLayout_2.addWidget(self.BacktoMainpushButton)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.MainStackedWidget.addWidget(self.page_checkcif)
        self.page_FinalCif = QtWidgets.QWidget()
        self.page_FinalCif.setObjectName("page_FinalCif")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.page_FinalCif)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.FinalCifFilePlainTextEdit = QtWidgets.QPlainTextEdit(self.page_FinalCif)
        self.FinalCifFilePlainTextEdit.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextSelectableByKeyboard|QtCore.Qt.TextSelectableByMouse)
        self.FinalCifFilePlainTextEdit.setObjectName("FinalCifFilePlainTextEdit")
        self.verticalLayout_3.addWidget(self.FinalCifFilePlainTextEdit)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem2)
        self.BackPushButton = QtWidgets.QPushButton(self.page_FinalCif)
        self.BackPushButton.setObjectName("BackPushButton")
        self.horizontalLayout_3.addWidget(self.BackPushButton)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem3)
        self.verticalLayout_3.addLayout(self.horizontalLayout_3)
        self.MainStackedWidget.addWidget(self.page_FinalCif)
        self.CifTableGridLayout.addWidget(self.MainStackedWidget, 0, 0, 1, 3)
        self.horizontalLayout_4.addWidget(self.splitter)
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
        self.MainStackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(FinalCifWindow)
        FinalCifWindow.setTabOrder(self.SelectCif_LineEdit, self.EquipmentEditTableWidget)
        FinalCifWindow.setTabOrder(self.EquipmentEditTableWidget, self.cifKeywordLineEdit)
        FinalCifWindow.setTabOrder(self.cifKeywordLineEdit, self.PropertiesEditTableWidget)
        FinalCifWindow.setTabOrder(self.PropertiesEditTableWidget, self.SelectCif_PushButton)
        FinalCifWindow.setTabOrder(self.SelectCif_PushButton, self.NewPropertyTemplateButton)
        FinalCifWindow.setTabOrder(self.NewPropertyTemplateButton, self.PropertiesTemplatesListWidget)
        FinalCifWindow.setTabOrder(self.PropertiesTemplatesListWidget, self.EditPropertyTemplateButton)
        FinalCifWindow.setTabOrder(self.EditPropertyTemplateButton, self.NewEquipmentTemplateButton)
        FinalCifWindow.setTabOrder(self.NewEquipmentTemplateButton, self.EquipmentTemplatesListWidget)

    def retranslateUi(self, FinalCifWindow):
        _translate = QtCore.QCoreApplication.translate
        FinalCifWindow.setWindowTitle(_translate("FinalCifWindow", "FinalCif"))
        self.SelectCifFileGroupBox.setTitle(_translate("FinalCifWindow", "Cif file"))
        self.SelectCif_PushButton.setText(_translate("FinalCifWindow", "Select File"))
        self.SelectCif_LineEdit.setPlaceholderText(_translate("FinalCifWindow", "Select a .cif file first."))
        self.RecentComboBox.setCurrentText(_translate("FinalCifWindow", "Recent Files"))
        self.RecentComboBox.setItemText(0, _translate("FinalCifWindow", "Recent Files"))
        self.EquipmentGroupBox.setTitle(_translate("FinalCifWindow", "Equipment and Author Templates"))
        self.EquipmentTemplatesListWidget.setToolTip(_translate("FinalCifWindow", "<html><head/><body><p>Each entry can have a list of key/value pairs. For example a Diffractometer model can have a list of features.</p></body></html>"))
        self.NewEquipmentTemplateButton.setText(_translate("FinalCifWindow", "New Template"))
        self.EditEquipmentTemplateButton.setText(_translate("FinalCifWindow", "Edit Template"))
        self.ImportEquipmentTemplateButton.setText(_translate("FinalCifWindow", "Import"))
        self.EquipmentEditTableWidget.setSortingEnabled(True)
        item = self.EquipmentEditTableWidget.horizontalHeaderItem(0)
        item.setText(_translate("FinalCifWindow", "key"))
        item = self.EquipmentEditTableWidget.horizontalHeaderItem(1)
        item.setText(_translate("FinalCifWindow", "value"))
        self.DeleteEquipmentButton.setText(_translate("FinalCifWindow", "Delete Template"))
        self.SaveEquipmentButton.setText(_translate("FinalCifWindow", "Save"))
        self.CancelEquipmentButton.setText(_translate("FinalCifWindow", "Cancel"))
        self.ExportEquipmentButton.setText(_translate("FinalCifWindow", "Export"))
        self.PropertiesGroupBox.setTitle(_translate("FinalCifWindow", "Property Templates"))
        self.NewPropertyTemplateButton.setText(_translate("FinalCifWindow", "New Template"))
        self.EditPropertyTemplateButton.setText(_translate("FinalCifWindow", "Edit Template"))
        self.ImportPropertyTemplateButton.setText(_translate("FinalCifWindow", "Import"))
        self.PropertiesTemplatesListWidget.setToolTip(_translate("FinalCifWindow", "<html><head/><body><p>A list of common properties like </p><p>_exptl_crystal_colour: yellow, red, blue, ...</p><p>Lists defined here will appear as dropdown menus in the main Table.</p></body></html>"))
        self.DeletePropertiesButton.setText(_translate("FinalCifWindow", "Delete Template"))
        self.SavePropertiesButton.setText(_translate("FinalCifWindow", "Save"))
        self.CancelPropertiesButton.setText(_translate("FinalCifWindow", "Cancel"))
        self.ExportPropertyButton.setText(_translate("FinalCifWindow", "Export"))
        self.cifKeywordLB.setText(_translate("FinalCifWindow", "cif keyword"))
        self.CifItemsTable.setSortingEnabled(False)
        item = self.CifItemsTable.horizontalHeaderItem(0)
        item.setText(_translate("FinalCifWindow", "CIF Value"))
        item = self.CifItemsTable.horizontalHeaderItem(1)
        item.setText(_translate("FinalCifWindow", "From Data Source"))
        item = self.CifItemsTable.horizontalHeaderItem(2)
        item.setText(_translate("FinalCifWindow", "Own Data"))
        self.SaveCifButton.setToolTip(_translate("FinalCifWindow", "Saves the cif file to name-final.cif"))
        self.SaveCifButton.setText(_translate("FinalCifWindow", "Save Cif File"))
        self.ExploreDirButton.setToolTip(_translate("FinalCifWindow", "Saves the cif file to name-final.cif"))
        self.ExploreDirButton.setText(_translate("FinalCifWindow", "Explore Directory"))
        self.CheckcifPDFOnlineButton.setText(_translate("FinalCifWindow", "Checkcif Online PDF"))
        self.CheckcifOnlineButton.setText(_translate("FinalCifWindow", "Checkcif Online HTML"))
        self.CheckcifButton.setText(_translate("FinalCifWindow", "CheckCif Offline"))
        self.structfactCheckBox.setText(_translate("FinalCifWindow", "without structure factors"))
        self.SaveFullReportButton.setText(_translate("FinalCifWindow", "Make Tables"))
        self.HAtomsCheckBox.setText(_translate("FinalCifWindow", "without H-Bonds"))
        self.label.setText(_translate("FinalCifWindow", "PLATON Checkcif output:"))
        self.BacktoMainpushButton.setText(_translate("FinalCifWindow", "Back to CIF Table"))
        self.BackPushButton.setText(_translate("FinalCifWindow", "Back to CIF Table"))
        self.actionSave_Report.setText(_translate("FinalCifWindow", "Save Report"))
        self.actionSave_CIF_File.setText(_translate("FinalCifWindow", "Save CIF File"))
        self.actionedit_templates.setText(_translate("FinalCifWindow", "edit templates"))
from gui.custom_classes import MyCifTable, MyEQTableWidget
