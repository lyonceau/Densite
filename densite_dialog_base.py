# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'densite_dialog_base.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_DensiteDialogBase(object):
    def setupUi(self, DensiteDialogBase):
        DensiteDialogBase.setObjectName("DensiteDialogBase")
        DensiteDialogBase.setEnabled(True)
        DensiteDialogBase.resize(589, 766)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(DensiteDialogBase.sizePolicy().hasHeightForWidth())
        DensiteDialogBase.setSizePolicy(sizePolicy)
        DensiteDialogBase.setMaximumSize(QtCore.QSize(733, 800))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        font.setStrikeOut(False)
        DensiteDialogBase.setFont(font)
        DensiteDialogBase.setMouseTracking(False)
        DensiteDialogBase.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        DensiteDialogBase.setAcceptDrops(False)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../../../../../../../../../../.designer/backup/images/icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        DensiteDialogBase.setWindowIcon(icon)
        DensiteDialogBase.setLayoutDirection(QtCore.Qt.LeftToRight)
        DensiteDialogBase.setAutoFillBackground(False)
        DensiteDialogBase.setInputMethodHints(QtCore.Qt.ImhNone)
        DensiteDialogBase.setSizeGripEnabled(False)
        DensiteDialogBase.setModal(False)
        self.gridLayout_6 = QtWidgets.QGridLayout(DensiteDialogBase)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.textBrowser = QtWidgets.QTextBrowser(DensiteDialogBase)
        self.textBrowser.setEnabled(True)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        self.textBrowser.setFont(font)
        self.textBrowser.setAutoFormatting(QtWidgets.QTextEdit.AutoBulletList)
        self.textBrowser.setTabChangesFocus(False)
        self.textBrowser.setUndoRedoEnabled(False)
        self.textBrowser.setObjectName("textBrowser")
        self.gridLayout_6.addWidget(self.textBrowser, 1, 0, 1, 1)
        self.gridLayout_5 = QtWidgets.QGridLayout()
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.horizontalLayout_21 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_21.setObjectName("horizontalLayout_21")
        self.progressBar = QtWidgets.QProgressBar(DensiteDialogBase)
        self.progressBar.setEnabled(False)
        self.progressBar.setMinimumSize(QtCore.QSize(300, 10))
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.horizontalLayout_21.addWidget(self.progressBar)
        self.helpButton = QtWidgets.QPushButton(DensiteDialogBase)
        self.helpButton.setObjectName("helpButton")
        self.horizontalLayout_21.addWidget(self.helpButton)
        self.gridLayout_5.addLayout(self.horizontalLayout_21, 0, 0, 1, 1)
        self.gridLayout_6.addLayout(self.gridLayout_5, 2, 0, 1, 1)
        self.tabWidget = QtWidgets.QTabWidget(DensiteDialogBase)
        self.tabWidget.setObjectName("tabWidget")
        self.tab_importation = QtWidgets.QWidget()
        self.tab_importation.setObjectName("tab_importation")
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout(self.tab_importation)
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_2.addItem(spacerItem)
        self.horizontalLayout_14 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        spacerItem1 = QtWidgets.QSpacerItem(13, 55, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_14.addItem(spacerItem1)
        self.label_14 = QtWidgets.QLabel(self.tab_importation)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(50)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.label_14.setFont(font)
        self.label_14.setObjectName("label_14")
        self.horizontalLayout_14.addWidget(self.label_14)
        spacerItem2 = QtWidgets.QSpacerItem(13, 55, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_14.addItem(spacerItem2)
        self.verticalLayout_2.addLayout(self.horizontalLayout_14)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_2.addItem(spacerItem3)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_2.addItem(spacerItem4)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_9 = QtWidgets.QLabel(self.tab_importation)
        self.label_9.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_9.sizePolicy().hasHeightForWidth())
        self.label_9.setSizePolicy(sizePolicy)
        self.label_9.setObjectName("label_9")
        self.horizontalLayout.addWidget(self.label_9)
        self.lienCheminImport = QtWidgets.QLineEdit(self.tab_importation)
        self.lienCheminImport.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lienCheminImport.sizePolicy().hasHeightForWidth())
        self.lienCheminImport.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        self.lienCheminImport.setFont(font)
        self.lienCheminImport.setObjectName("lienCheminImport")
        self.horizontalLayout.addWidget(self.lienCheminImport)
        self.boutonCheminImport = QtWidgets.QPushButton(self.tab_importation)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.boutonCheminImport.sizePolicy().hasHeightForWidth())
        self.boutonCheminImport.setSizePolicy(sizePolicy)
        self.boutonCheminImport.setObjectName("boutonCheminImport")
        self.horizontalLayout.addWidget(self.boutonCheminImport)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem5)
        self.boutonImport = QtWidgets.QPushButton(self.tab_importation)
        self.boutonImport.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.boutonImport.sizePolicy().hasHeightForWidth())
        self.boutonImport.setSizePolicy(sizePolicy)
        self.boutonImport.setObjectName("boutonImport")
        self.horizontalLayout_2.addWidget(self.boutonImport)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem6)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.gridLayout_2.addLayout(self.verticalLayout_2, 0, 0, 1, 1)
        self.horizontalLayout_13.addLayout(self.gridLayout_2)
        self.tabWidget.addTab(self.tab_importation, "")
        self.tab_integration = QtWidgets.QWidget()
        self.tab_integration.setObjectName("tab_integration")
        self.horizontalLayout_18 = QtWidgets.QHBoxLayout(self.tab_integration)
        self.horizontalLayout_18.setObjectName("horizontalLayout_18")
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.horizontalLayout_16 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_16.setObjectName("horizontalLayout_16")
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_16.addItem(spacerItem7)
        self.boutonIntegrationCommune = QtWidgets.QPushButton(self.tab_integration)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.boutonIntegrationCommune.sizePolicy().hasHeightForWidth())
        self.boutonIntegrationCommune.setSizePolicy(sizePolicy)
        self.boutonIntegrationCommune.setObjectName("boutonIntegrationCommune")
        self.horizontalLayout_16.addWidget(self.boutonIntegrationCommune)
        spacerItem8 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_16.addItem(spacerItem8)
        self.gridLayout_3.addLayout(self.horizontalLayout_16, 7, 0, 1, 1)
        spacerItem9 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem9, 8, 0, 1, 1)
        self.horizontalLayout_15 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_15.setObjectName("horizontalLayout_15")
        self.label_16 = QtWidgets.QLabel(self.tab_integration)
        font = QtGui.QFont()
        font.setPointSize(7)
        font.setBold(True)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.label_16.setFont(font)
        self.label_16.setObjectName("label_16")
        self.horizontalLayout_15.addWidget(self.label_16)
        self.comboBox_tb_commune = QtWidgets.QComboBox(self.tab_integration)
        self.comboBox_tb_commune.setMinimumSize(QtCore.QSize(150, 0))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.comboBox_tb_commune.setFont(font)
        self.comboBox_tb_commune.setObjectName("comboBox_tb_commune")
        self.comboBox_tb_commune.addItem("")
        self.comboBox_tb_commune.setItemText(0, "")
        self.horizontalLayout_15.addWidget(self.comboBox_tb_commune)
        spacerItem10 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_15.addItem(spacerItem10)
        self.label_Commune_6 = QtWidgets.QLabel(self.tab_integration)
        font = QtGui.QFont()
        font.setPointSize(7)
        font.setBold(True)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.label_Commune_6.setFont(font)
        self.label_Commune_6.setObjectName("label_Commune_6")
        self.horizontalLayout_15.addWidget(self.label_Commune_6)
        self.comboBoxChampsNom = QtWidgets.QComboBox(self.tab_integration)
        self.comboBoxChampsNom.setEnabled(True)
        self.comboBoxChampsNom.setMinimumSize(QtCore.QSize(120, 0))
        self.comboBoxChampsNom.setSizeIncrement(QtCore.QSize(0, 0))
        self.comboBoxChampsNom.setBaseSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        self.comboBoxChampsNom.setFont(font)
        self.comboBoxChampsNom.setObjectName("comboBoxChampsNom")
        self.horizontalLayout_15.addWidget(self.comboBoxChampsNom)
        self.gridLayout_3.addLayout(self.horizontalLayout_15, 5, 0, 1, 1)
        spacerItem11 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem11, 1, 0, 1, 1)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        spacerItem12 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_3.addItem(spacerItem12)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        spacerItem13 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem13)
        self.label_10 = QtWidgets.QLabel(self.tab_integration)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(50)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.horizontalLayout_7.addWidget(self.label_10)
        spacerItem14 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem14)
        self.verticalLayout_3.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        spacerItem15 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_9.addItem(spacerItem15)
        self.boutonCreationTb = QtWidgets.QPushButton(self.tab_integration)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.boutonCreationTb.sizePolicy().hasHeightForWidth())
        self.boutonCreationTb.setSizePolicy(sizePolicy)
        self.boutonCreationTb.setObjectName("boutonCreationTb")
        self.horizontalLayout_9.addWidget(self.boutonCreationTb)
        spacerItem16 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_9.addItem(spacerItem16)
        self.verticalLayout_3.addLayout(self.horizontalLayout_9)
        spacerItem17 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_3.addItem(spacerItem17)
        self.line_3 = QtWidgets.QFrame(self.tab_integration)
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.verticalLayout_3.addWidget(self.line_3)
        self.line = QtWidgets.QFrame(self.tab_integration)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout_3.addWidget(self.line)
        self.line_2 = QtWidgets.QFrame(self.tab_integration)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.verticalLayout_3.addWidget(self.line_2)
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        spacerItem18 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_11.addItem(spacerItem18)
        self.RafraichirUi = QtWidgets.QPushButton(self.tab_integration)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.RafraichirUi.sizePolicy().hasHeightForWidth())
        self.RafraichirUi.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        self.RafraichirUi.setFont(font)
        self.RafraichirUi.setAutoDefault(True)
        self.RafraichirUi.setObjectName("RafraichirUi")
        self.horizontalLayout_11.addWidget(self.RafraichirUi)
        spacerItem19 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_11.addItem(spacerItem19)
        self.verticalLayout_3.addLayout(self.horizontalLayout_11)
        spacerItem20 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_3.addItem(spacerItem20)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_8 = QtWidgets.QLabel(self.tab_integration)
        font = QtGui.QFont()
        font.setPointSize(7)
        font.setBold(True)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_5.addWidget(self.label_8)
        self.comboBox_tb_OCS = QtWidgets.QComboBox(self.tab_integration)
        self.comboBox_tb_OCS.setMinimumSize(QtCore.QSize(150, 0))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.comboBox_tb_OCS.setFont(font)
        self.comboBox_tb_OCS.setIconSize(QtCore.QSize(16, 16))
        self.comboBox_tb_OCS.setObjectName("comboBox_tb_OCS")
        self.comboBox_tb_OCS.addItem("")
        self.comboBox_tb_OCS.setItemText(0, "")
        self.horizontalLayout_5.addWidget(self.comboBox_tb_OCS)
        spacerItem21 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem21)
        self.label_Commune = QtWidgets.QLabel(self.tab_integration)
        font = QtGui.QFont()
        font.setPointSize(7)
        font.setBold(True)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.label_Commune.setFont(font)
        self.label_Commune.setObjectName("label_Commune")
        self.horizontalLayout_5.addWidget(self.label_Commune)
        self.comboBoxChampsCode_12 = QtWidgets.QComboBox(self.tab_integration)
        self.comboBoxChampsCode_12.setEnabled(True)
        self.comboBoxChampsCode_12.setMinimumSize(QtCore.QSize(120, 0))
        self.comboBoxChampsCode_12.setSizeIncrement(QtCore.QSize(0, 0))
        self.comboBoxChampsCode_12.setBaseSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        self.comboBoxChampsCode_12.setFont(font)
        self.comboBoxChampsCode_12.setObjectName("comboBoxChampsCode_12")
        self.horizontalLayout_5.addWidget(self.comboBoxChampsCode_12)
        self.verticalLayout_3.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        spacerItem22 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem22)
        self.boutonIntegrationBd = QtWidgets.QPushButton(self.tab_integration)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.boutonIntegrationBd.sizePolicy().hasHeightForWidth())
        self.boutonIntegrationBd.setSizePolicy(sizePolicy)
        self.boutonIntegrationBd.setObjectName("boutonIntegrationBd")
        self.horizontalLayout_8.addWidget(self.boutonIntegrationBd)
        spacerItem23 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem23)
        self.verticalLayout_3.addLayout(self.horizontalLayout_8)
        self.gridLayout_3.addLayout(self.verticalLayout_3, 0, 0, 1, 1)
        self.line_6 = QtWidgets.QFrame(self.tab_integration)
        self.line_6.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_6.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_6.setObjectName("line_6")
        self.gridLayout_3.addWidget(self.line_6, 4, 0, 1, 1)
        self.line_5 = QtWidgets.QFrame(self.tab_integration)
        self.line_5.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        self.gridLayout_3.addWidget(self.line_5, 2, 0, 1, 1)
        self.line_4 = QtWidgets.QFrame(self.tab_integration)
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.gridLayout_3.addWidget(self.line_4, 3, 0, 1, 1)
        self.horizontalLayout_19 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_19.setObjectName("horizontalLayout_19")
        self.label_Commune_7 = QtWidgets.QLabel(self.tab_integration)
        font = QtGui.QFont()
        font.setPointSize(7)
        font.setBold(True)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.label_Commune_7.setFont(font)
        self.label_Commune_7.setObjectName("label_Commune_7")
        self.horizontalLayout_19.addWidget(self.label_Commune_7)
        self.comboBoxChampsInsee = QtWidgets.QComboBox(self.tab_integration)
        self.comboBoxChampsInsee.setEnabled(True)
        self.comboBoxChampsInsee.setMinimumSize(QtCore.QSize(120, 0))
        self.comboBoxChampsInsee.setSizeIncrement(QtCore.QSize(0, 0))
        self.comboBoxChampsInsee.setBaseSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        self.comboBoxChampsInsee.setFont(font)
        self.comboBoxChampsInsee.setObjectName("comboBoxChampsInsee")
        self.horizontalLayout_19.addWidget(self.comboBoxChampsInsee)
        spacerItem24 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_19.addItem(spacerItem24)
        self.label_19 = QtWidgets.QLabel(self.tab_integration)
        font = QtGui.QFont()
        font.setPointSize(7)
        font.setBold(True)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.label_19.setFont(font)
        self.label_19.setObjectName("label_19")
        self.horizontalLayout_19.addWidget(self.label_19)
        self.comboBoxChampsCodeDept = QtWidgets.QComboBox(self.tab_integration)
        self.comboBoxChampsCodeDept.setMinimumSize(QtCore.QSize(120, 0))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        self.comboBoxChampsCodeDept.setFont(font)
        self.comboBoxChampsCodeDept.setObjectName("comboBoxChampsCodeDept")
        self.comboBoxChampsCodeDept.addItem("")
        self.comboBoxChampsCodeDept.setItemText(0, "")
        self.horizontalLayout_19.addWidget(self.comboBoxChampsCodeDept)
        self.gridLayout_3.addLayout(self.horizontalLayout_19, 6, 0, 1, 1)
        self.horizontalLayout_18.addLayout(self.gridLayout_3)
        self.tabWidget.addTab(self.tab_integration, "")
        self.tab_stat = QtWidgets.QWidget()
        self.tab_stat.setObjectName("tab_stat")
        self.gridLayout_13 = QtWidgets.QGridLayout(self.tab_stat)
        self.gridLayout_13.setObjectName("gridLayout_13")
        self.line_8 = QtWidgets.QFrame(self.tab_stat)
        self.line_8.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_8.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_8.setObjectName("line_8")
        self.gridLayout_13.addWidget(self.line_8, 2, 0, 1, 1)
        self.line_7 = QtWidgets.QFrame(self.tab_stat)
        self.line_7.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_7.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_7.setObjectName("line_7")
        self.gridLayout_13.addWidget(self.line_7, 3, 0, 1, 1)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout_17 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_17.setObjectName("horizontalLayout_17")
        spacerItem25 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_17.addItem(spacerItem25)
        self.gridLayout.addLayout(self.horizontalLayout_17, 0, 0, 1, 1)
        self.horizontalLayout_3.addLayout(self.gridLayout)
        self.gridLayout_10 = QtWidgets.QGridLayout()
        self.gridLayout_10.setObjectName("gridLayout_10")
        spacerItem26 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_10.addItem(spacerItem26, 0, 0, 1, 1)
        spacerItem27 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_10.addItem(spacerItem27, 1, 0, 1, 1)
        self.horizontalLayout_3.addLayout(self.gridLayout_10)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout_25 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_25.setObjectName("horizontalLayout_25")
        self.rafraichirUi_barre_recherche = QtWidgets.QPushButton(self.tab_stat)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.rafraichirUi_barre_recherche.sizePolicy().hasHeightForWidth())
        self.rafraichirUi_barre_recherche.setSizePolicy(sizePolicy)
        self.rafraichirUi_barre_recherche.setObjectName("rafraichirUi_barre_recherche")
        self.horizontalLayout_25.addWidget(self.rafraichirUi_barre_recherche)
        self.verticalLayout_4.addLayout(self.horizontalLayout_25)
        self.label_2 = QtWidgets.QLabel(self.tab_stat)
        font = QtGui.QFont()
        font.setPointSize(7)
        font.setBold(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_4.addWidget(self.label_2)
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.comboBox_Stat = QtWidgets.QComboBox(self.tab_stat)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        self.comboBox_Stat.setFont(font)
        self.comboBox_Stat.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.comboBox_Stat.setToolTip("")
        self.comboBox_Stat.setStatusTip("")
        self.comboBox_Stat.setWhatsThis("")
        self.comboBox_Stat.setAccessibleName("")
        self.comboBox_Stat.setAccessibleDescription("")
        self.comboBox_Stat.setStyleSheet("")
        self.comboBox_Stat.setInputMethodHints(QtCore.Qt.ImhPreferUppercase)
        self.comboBox_Stat.setEditable(True)
        self.comboBox_Stat.setDuplicatesEnabled(False)
        self.comboBox_Stat.setObjectName("comboBox_Stat")
        self.horizontalLayout_10.addWidget(self.comboBox_Stat)
        self.verticalLayout_4.addLayout(self.horizontalLayout_10)
        self.tableWidget_ChoixFinal_Stat = QtWidgets.QTableWidget(self.tab_stat)
        self.tableWidget_ChoixFinal_Stat.setMinimumSize(QtCore.QSize(0, 0))
        self.tableWidget_ChoixFinal_Stat.setMaximumSize(QtCore.QSize(220, 16777215))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.tableWidget_ChoixFinal_Stat.setFont(font)
        self.tableWidget_ChoixFinal_Stat.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableWidget_ChoixFinal_Stat.setRowCount(0)
        self.tableWidget_ChoixFinal_Stat.setColumnCount(1)
        self.tableWidget_ChoixFinal_Stat.setObjectName("tableWidget_ChoixFinal_Stat")
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_ChoixFinal_Stat.setHorizontalHeaderItem(0, item)
        self.verticalLayout_4.addWidget(self.tableWidget_ChoixFinal_Stat)
        self.horizontalLayout_26 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_26.setObjectName("horizontalLayout_26")
        spacerItem28 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_26.addItem(spacerItem28)
        self.rafraichirUi_ToutSupprimer = QtWidgets.QPushButton(self.tab_stat)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.rafraichirUi_ToutSupprimer.sizePolicy().hasHeightForWidth())
        self.rafraichirUi_ToutSupprimer.setSizePolicy(sizePolicy)
        self.rafraichirUi_ToutSupprimer.setMaximumSize(QtCore.QSize(120, 200))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        self.rafraichirUi_ToutSupprimer.setFont(font)
        self.rafraichirUi_ToutSupprimer.setObjectName("rafraichirUi_ToutSupprimer")
        self.horizontalLayout_26.addWidget(self.rafraichirUi_ToutSupprimer)
        spacerItem29 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_26.addItem(spacerItem29)
        self.verticalLayout_4.addLayout(self.horizontalLayout_26)
        self.horizontalLayout_3.addLayout(self.verticalLayout_4)
        self.gridLayout_12 = QtWidgets.QGridLayout()
        self.gridLayout_12.setObjectName("gridLayout_12")
        spacerItem30 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_12.addItem(spacerItem30, 1, 0, 1, 1)
        spacerItem31 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_12.addItem(spacerItem31, 6, 0, 1, 1)
        spacerItem32 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_12.addItem(spacerItem32, 7, 0, 1, 1)
        spacerItem33 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_12.addItem(spacerItem33, 0, 0, 1, 1)
        spacerItem34 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_12.addItem(spacerItem34, 5, 0, 1, 1)
        self.horizontalLayout_3.addLayout(self.gridLayout_12)
        self.gridLayout_11 = QtWidgets.QGridLayout()
        self.gridLayout_11.setObjectName("gridLayout_11")
        self.horizontalLayout_23 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_23.setObjectName("horizontalLayout_23")
        spacerItem35 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_23.addItem(spacerItem35)
        self.gridLayout_11.addLayout(self.horizontalLayout_23, 0, 0, 1, 1)
        self.horizontalLayout_3.addLayout(self.gridLayout_11)
        self.gridLayout_4 = QtWidgets.QGridLayout()
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.horizontalLayout_3.addLayout(self.gridLayout_4)
        self.gridLayout_13.addLayout(self.horizontalLayout_3, 0, 0, 1, 1)
        self.horizontalLayout_34 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_34.setObjectName("horizontalLayout_34")
        spacerItem36 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_34.addItem(spacerItem36)
        self.exportStat = QtWidgets.QPushButton(self.tab_stat)
        self.exportStat.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.exportStat.sizePolicy().hasHeightForWidth())
        self.exportStat.setSizePolicy(sizePolicy)
        self.exportStat.setObjectName("exportStat")
        self.horizontalLayout_34.addWidget(self.exportStat)
        spacerItem37 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_34.addItem(spacerItem37)
        self.gridLayout_13.addLayout(self.horizontalLayout_34, 4, 0, 1, 1)
        self.line_9 = QtWidgets.QFrame(self.tab_stat)
        self.line_9.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_9.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_9.setObjectName("line_9")
        self.gridLayout_13.addWidget(self.line_9, 1, 0, 1, 1)
        self.tabWidget.addTab(self.tab_stat, "")
        self.gridLayout_6.addWidget(self.tabWidget, 0, 0, 1, 1)

        self.retranslateUi(DensiteDialogBase)
        self.tabWidget.setCurrentIndex(0)
        self.comboBoxChampsNom.setCurrentIndex(-1)
        self.comboBoxChampsCode_12.setCurrentIndex(-1)
        self.comboBoxChampsInsee.setCurrentIndex(-1)
        QtCore.QMetaObject.connectSlotsByName(DensiteDialogBase)
        DensiteDialogBase.setTabOrder(self.textBrowser, self.tabWidget)
        DensiteDialogBase.setTabOrder(self.tabWidget, self.lienCheminImport)
        DensiteDialogBase.setTabOrder(self.lienCheminImport, self.boutonCheminImport)
        DensiteDialogBase.setTabOrder(self.boutonCheminImport, self.boutonImport)
        DensiteDialogBase.setTabOrder(self.boutonImport, self.helpButton)
        DensiteDialogBase.setTabOrder(self.helpButton, self.boutonIntegrationBd)

    def retranslateUi(self, DensiteDialogBase):
        _translate = QtCore.QCoreApplication.translate
        DensiteDialogBase.setWindowTitle(_translate("DensiteDialogBase", "Densité d\'occupation des sols"))
        self.progressBar.setFormat(_translate("DensiteDialogBase", "%p% progression"))
        self.helpButton.setText(_translate("DensiteDialogBase", "About - Help"))
        self.label_14.setText(_translate("DensiteDialogBase", "Indiquez simplément le repertoire dans lequel se trouve les fichiers"))
        self.label_9.setText(_translate("DensiteDialogBase", "Dossier"))
        self.lienCheminImport.setPlaceholderText(_translate("DensiteDialogBase", "Lien pour importer"))
        self.boutonCheminImport.setText(_translate("DensiteDialogBase", ". . ."))
        self.boutonImport.setText(_translate("DensiteDialogBase", "Importer"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_importation), _translate("DensiteDialogBase", "1. IMPORTER DANS QGIS"))
        self.boutonIntegrationCommune.setText(_translate("DensiteDialogBase", "INTEGRATION COMMUNE"))
        self.label_16.setText(_translate("DensiteDialogBase", "<html><head/><body><p align=\"justify\"><span style=\" font-family:\'Sans Serif\';\">Shp Commune</span><span style=\" font-family:\'Sans Serif\'; font-size:10pt; color:#ff0000;\"> *</span></p></body></html>"))
        self.label_Commune_6.setText(_translate("DensiteDialogBase", "<html><head/><body><p align=\"justify\"><span style=\" font-family:\'Sans Serif\';\">Champs Nom </span><span style=\" font-family:\'Sans Serif\'; font-size:10pt; color:#ff0000;\">*</span></p></body></html>"))
        self.label_10.setText(_translate("DensiteDialogBase", "A executer uniquement pour la prémière fois."))
        self.boutonCreationTb.setText(_translate("DensiteDialogBase", "CREATION TABLE"))
        self.RafraichirUi.setText(_translate("DensiteDialogBase", "Rafraichir"))
        self.label_8.setText(_translate("DensiteDialogBase", "<html><head/><body><p align=\"justify\"><span style=\" font-family:\'Sans Serif\';\">Shp OCS</span><span style=\" font-family:\'Sans Serif\'; font-size:10pt; color:#ff0000;\"> *</span></p></body></html>"))
        self.label_Commune.setText(_translate("DensiteDialogBase", "<html><head/><body><p align=\"justify\"><span style=\" font-family:\'Sans Serif\';\">Champs Code</span><span style=\" font-family:\'Sans Serif\'; font-size:10pt; color:#ff0000;\"> *</span></p></body></html>"))
        self.boutonIntegrationBd.setText(_translate("DensiteDialogBase", "INTEGRATION OCS"))
        self.label_Commune_7.setText(_translate("DensiteDialogBase", "<html><head/><body><p><span style=\" font-family:\'Sans Serif\';\">Champs INSEE </span><span style=\" font-family:\'Sans Serif\'; font-size:10pt; color:#ff0000;\">*</span></p></body></html>"))
        self.label_19.setText(_translate("DensiteDialogBase", "<html><head/><body><p><span style=\" font-family:\'Sans Serif\';\">Champs Code DEPT</span><span style=\" font-family:\'Sans Serif\'; font-size:10pt; color:#ff0000;\"> *</span></p></body></html>"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_integration), _translate("DensiteDialogBase", "2. INTEGRATION BD"))
        self.rafraichirUi_barre_recherche.setText(_translate("DensiteDialogBase", "Rafraichir"))
        self.label_2.setText(_translate("DensiteDialogBase", "Barre de recherche rapide"))
        item = self.tableWidget_ChoixFinal_Stat.horizontalHeaderItem(0)
        item.setText(_translate("DensiteDialogBase", "COMMUNES"))
        self.rafraichirUi_ToutSupprimer.setText(_translate("DensiteDialogBase", "   Tout supprimer   "))
        self.exportStat.setText(_translate("DensiteDialogBase", "GÉNÉRER"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_stat), _translate("DensiteDialogBase", "3. STATISTIQUES"))
