# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '../ui_files/Main_window.ui'
#
# Created: Fri Dec 19 19:55:20 2014
#      by: pyside-uic 0.2.15 running on PySide 1.2.1
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(900, 600)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(900, 600))
        MainWindow.setMaximumSize(QtCore.QSize(900, 600))
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.tabWidget = QtGui.QTabWidget(self.centralwidget)
        self.tabWidget.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.tabWidget.setSizeIncrement(QtCore.QSize(0, 0))
        self.tabWidget.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtGui.QWidget()
        self.tab.setObjectName("tab")
        self.horizontalLayout_7 = QtGui.QHBoxLayout(self.tab)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setSizeConstraint(QtGui.QLayout.SetMaximumSize)
        self.verticalLayout.setObjectName("verticalLayout")
        self.groupBox = QtGui.QGroupBox(self.tab)
        font = QtGui.QFont()
        font.setWeight(50)
        font.setBold(False)
        self.groupBox.setFont(font)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout_3 = QtGui.QGridLayout(self.groupBox)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.gridLayout_2 = QtGui.QGridLayout()
        self.gridLayout_2.setSizeConstraint(QtGui.QLayout.SetMaximumSize)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.PushBtn = QtGui.QRadioButton(self.groupBox)
        self.PushBtn.setCheckable(True)
        self.PushBtn.setChecked(True)
        self.PushBtn.setAutoExclusive(True)
        self.PushBtn.setObjectName("PushBtn")
        self.gridLayout_2.addWidget(self.PushBtn, 0, 0, 1, 1)
        self.volume_label = QtGui.QLabel(self.groupBox)
        self.volume_label.setObjectName("volume_label")
        self.gridLayout_2.addWidget(self.volume_label, 0, 2, 1, 1)
        self.verticalLayout_4 = QtGui.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.gridLayout_2.addLayout(self.verticalLayout_4, 2, 2, 1, 1)
        self.volume_prompt = QtGui.QLineEdit(self.groupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.volume_prompt.sizePolicy().hasHeightForWidth())
        self.volume_prompt.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.volume_prompt.setFont(font)
        self.volume_prompt.setInputMethodHints(QtCore.Qt.ImhNone)
        self.volume_prompt.setText("")
        self.volume_prompt.setObjectName("volume_prompt")
        self.gridLayout_2.addWidget(self.volume_prompt, 1, 2, 1, 1)
        self.PullBtn = QtGui.QRadioButton(self.groupBox)
        self.PullBtn.setCheckable(True)
        self.PullBtn.setAutoExclusive(True)
        self.PullBtn.setObjectName("PullBtn")
        self.gridLayout_2.addWidget(self.PullBtn, 1, 0, 1, 1)
        self.gridLayout_3.addLayout(self.gridLayout_2, 1, 0, 1, 1)
        self.volume_button = QtGui.QPushButton(self.groupBox)
        self.volume_button.setEnabled(False)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.volume_button.sizePolicy().hasHeightForWidth())
        self.volume_button.setSizePolicy(sizePolicy)
        self.volume_button.setMinimumSize(QtCore.QSize(100, 0))
        self.volume_button.setMaximumSize(QtCore.QSize(100, 16777215))
        self.volume_button.setObjectName("volume_button")
        self.gridLayout_3.addWidget(self.volume_button, 1, 2, 1, 1)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem, 1, 1, 1, 1)
        self.verticalLayout.addWidget(self.groupBox)
        self.groupBox_2 = QtGui.QGroupBox(self.tab)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_2.sizePolicy().hasHeightForWidth())
        self.groupBox_2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.groupBox_2.setFont(font)
        self.groupBox_2.setObjectName("groupBox_2")
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.groupBox_2)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.speed_slider = QtGui.QSlider(self.groupBox_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.speed_slider.sizePolicy().hasHeightForWidth())
        self.speed_slider.setSizePolicy(sizePolicy)
        self.speed_slider.setMaximumSize(QtCore.QSize(11111, 16777215))
        self.speed_slider.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.speed_slider.setMinimum(1)
        self.speed_slider.setMaximum(40)
        self.speed_slider.setProperty("value", 10)
        self.speed_slider.setOrientation(QtCore.Qt.Horizontal)
        self.speed_slider.setObjectName("speed_slider")
        self.horizontalLayout_2.addWidget(self.speed_slider)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem1 = QtGui.QSpacerItem(100, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.horizontalLayout_2.addLayout(self.horizontalLayout)
        self.lcdNumber = QtGui.QLCDNumber(self.groupBox_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lcdNumber.sizePolicy().hasHeightForWidth())
        self.lcdNumber.setSizePolicy(sizePolicy)
        self.lcdNumber.setInputMethodHints(QtCore.Qt.ImhNone)
        self.lcdNumber.setSmallDecimalPoint(False)
        self.lcdNumber.setNumDigits(5)
        self.lcdNumber.setDigitCount(5)
        self.lcdNumber.setObjectName("lcdNumber")
        self.horizontalLayout_2.addWidget(self.lcdNumber)
        self.verticalLayout.addWidget(self.groupBox_2)
        self.groupBox_4 = QtGui.QGroupBox(self.tab)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.groupBox_4.setFont(font)
        self.groupBox_4.setObjectName("groupBox_4")
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.groupBox_4)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.output_btn = QtGui.QRadioButton(self.groupBox_4)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.output_btn.sizePolicy().hasHeightForWidth())
        self.output_btn.setSizePolicy(sizePolicy)
        self.output_btn.setCheckable(True)
        self.output_btn.setChecked(True)
        self.output_btn.setAutoExclusive(True)
        self.output_btn.setObjectName("output_btn")
        self.verticalLayout_2.addWidget(self.output_btn)
        self.input_btn = QtGui.QRadioButton(self.groupBox_4)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.input_btn.sizePolicy().hasHeightForWidth())
        self.input_btn.setSizePolicy(sizePolicy)
        self.input_btn.setCheckable(True)
        self.input_btn.setAutoExclusive(True)
        self.input_btn.setObjectName("input_btn")
        self.verticalLayout_2.addWidget(self.input_btn)
        self.bypass_btn = QtGui.QRadioButton(self.groupBox_4)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.bypass_btn.sizePolicy().hasHeightForWidth())
        self.bypass_btn.setSizePolicy(sizePolicy)
        self.bypass_btn.setCheckable(True)
        self.bypass_btn.setAutoExclusive(True)
        self.bypass_btn.setObjectName("bypass_btn")
        self.verticalLayout_2.addWidget(self.bypass_btn)
        self.verticalLayout_3.addLayout(self.verticalLayout_2)
        self.verticalLayout.addWidget(self.groupBox_4)
        self.groupBox_3 = QtGui.QGroupBox(self.tab)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.groupBox_3.setFont(font)
        self.groupBox_3.setObjectName("groupBox_3")
        self.horizontalLayout_4 = QtGui.QHBoxLayout(self.groupBox_3)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.gridLayout_4 = QtGui.QGridLayout()
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.quick_combobox = QtGui.QComboBox(self.groupBox_3)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.quick_combobox.sizePolicy().hasHeightForWidth())
        self.quick_combobox.setSizePolicy(sizePolicy)
        self.quick_combobox.setMaximumSize(QtCore.QSize(300, 16777215))
        self.quick_combobox.setObjectName("quick_combobox")
        self.quick_combobox.addItem("")
        self.quick_combobox.addItem("")
        self.quick_combobox.addItem("")
        self.quick_combobox.addItem("")
        self.gridLayout_4.addWidget(self.quick_combobox, 0, 0, 1, 1)
        spacerItem2 = QtGui.QSpacerItem(50, 20, QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum)
        self.gridLayout_4.addItem(spacerItem2, 0, 2, 1, 1)
        spacerItem3 = QtGui.QSpacerItem(20, 10, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        self.gridLayout_4.addItem(spacerItem3, 1, 2, 1, 1)
        self.address_combobox = QtGui.QComboBox(self.groupBox_3)
        self.address_combobox.setObjectName("address_combobox")
        self.address_combobox.addItem("")
        self.address_combobox.addItem("")
        self.address_combobox.addItem("")
        self.address_combobox.addItem("")
        self.address_combobox.addItem("")
        self.address_combobox.addItem("")
        self.address_combobox.addItem("")
        self.address_combobox.addItem("")
        self.address_combobox.addItem("")
        self.address_combobox.addItem("")
        self.address_combobox.addItem("")
        self.address_combobox.addItem("")
        self.address_combobox.addItem("")
        self.address_combobox.addItem("")
        self.address_combobox.addItem("")
        self.address_combobox.addItem("")
        self.gridLayout_4.addWidget(self.address_combobox, 2, 3, 1, 1)
        self.make_it_so = QtGui.QPushButton(self.groupBox_3)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.make_it_so.sizePolicy().hasHeightForWidth())
        self.make_it_so.setSizePolicy(sizePolicy)
        self.make_it_so.setMaximumSize(QtCore.QSize(100, 16777215))
        self.make_it_so.setBaseSize(QtCore.QSize(0, 0))
        self.make_it_so.setObjectName("make_it_so")
        self.gridLayout_4.addWidget(self.make_it_so, 0, 3, 1, 1)
        self.label_2 = QtGui.QLabel(self.groupBox_3)
        self.label_2.setObjectName("label_2")
        self.gridLayout_4.addWidget(self.label_2, 2, 0, 1, 1)
        self.horizontalLayout_4.addLayout(self.gridLayout_4)
        self.verticalLayout.addWidget(self.groupBox_3)
        self.horizontalLayout_7.addLayout(self.verticalLayout)
        self.horizontalLayout_6 = QtGui.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.horizontalLayout_7.addLayout(self.horizontalLayout_6)
        self.graphicsView = QtGui.QGraphicsView(self.tab)
        self.graphicsView.setObjectName("graphicsView")
        self.horizontalLayout_7.addWidget(self.graphicsView)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.horizontalLayout_9 = QtGui.QHBoxLayout(self.tab_2)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.horizontalLayout_8 = QtGui.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.groupBox_6 = QtGui.QGroupBox(self.tab_2)
        self.groupBox_6.setObjectName("groupBox_6")
        self.verticalLayout_6 = QtGui.QVBoxLayout(self.groupBox_6)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.textEdit = QtGui.QTextEdit(self.groupBox_6)
        self.textEdit.setFrameShape(QtGui.QFrame.WinPanel)
        self.textEdit.setObjectName("textEdit")
        self.verticalLayout_6.addWidget(self.textEdit)
        self.verticalLayout_5 = QtGui.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.run_script_btn = QtGui.QPushButton(self.groupBox_6)
        self.run_script_btn.setObjectName("run_script_btn")
        self.horizontalLayout_3.addWidget(self.run_script_btn)
        self.clear_editor_btn = QtGui.QPushButton(self.groupBox_6)
        self.clear_editor_btn.setObjectName("clear_editor_btn")
        self.horizontalLayout_3.addWidget(self.clear_editor_btn)
        spacerItem4 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem4)
        self.back_interactive_btn = QtGui.QPushButton(self.groupBox_6)
        self.back_interactive_btn.setObjectName("back_interactive_btn")
        self.horizontalLayout_3.addWidget(self.back_interactive_btn)
        self.verticalLayout_5.addLayout(self.horizontalLayout_3)
        self.verticalLayout_6.addLayout(self.verticalLayout_5)
        self.horizontalLayout_8.addWidget(self.groupBox_6)
        self.horizontalLayout_9.addLayout(self.horizontalLayout_8)
        self.tabWidget.addTab(self.tab_2, "")
        self.gridLayout.addWidget(self.tabWidget, 0, 0, 1, 1)
        self.command_label = QtGui.QLabel(self.centralwidget)
        self.command_label.setText("")
        self.command_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.command_label.setObjectName("command_label")
        self.gridLayout.addWidget(self.command_label, 1, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar = QtGui.QMenuBar()
        self.menubar.setGeometry(QtCore.QRect(0, 0, 900, 22))
        self.menubar.setObjectName("menubar")
        self.menuScript = QtGui.QMenu(self.menubar)
        self.menuScript.setObjectName("menuScript")
        self.menuScript_2 = QtGui.QMenu(self.menuScript)
        self.menuScript_2.setObjectName("menuScript_2")
        self.menuConnect = QtGui.QMenu(self.menubar)
        self.menuConnect.setObjectName("menuConnect")
        self.menuOutput_Valve = QtGui.QMenu(self.menuConnect)
        self.menuOutput_Valve.setObjectName("menuOutput_Valve")
        self.menuHelp = QtGui.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        self.menuView = QtGui.QMenu(self.menubar)
        self.menuView.setObjectName("menuView")
        MainWindow.setMenuBar(self.menubar)
        self.actionNew_2 = QtGui.QAction(MainWindow)
        self.actionNew_2.setObjectName("actionNew_2")
        self.actionOpen = QtGui.QAction(MainWindow)
        self.actionOpen.setObjectName("actionOpen")
        self.actionSave = QtGui.QAction(MainWindow)
        self.actionSave.setObjectName("actionSave")
        self.actionSaveAs = QtGui.QAction(MainWindow)
        self.actionSaveAs.setObjectName("actionSaveAs")
        self.actionNew_Device = QtGui.QAction(MainWindow)
        self.actionNew_Device.setObjectName("actionNew_Device")
        self.actionAbout = QtGui.QAction(MainWindow)
        self.actionAbout.setMenuRole(QtGui.QAction.NoRole)
        self.actionAbout.setObjectName("actionAbout")
        self.actionCommands = QtGui.QAction(MainWindow)
        self.actionCommands.setObjectName("actionCommands")
        self.actionReports = QtGui.QAction(MainWindow)
        self.actionReports.setObjectName("actionReports")
        self.actionHistory = QtGui.QAction(MainWindow)
        self.actionHistory.setObjectName("actionHistory")
        self.actionNew = QtGui.QAction(MainWindow)
        self.actionNew.setShortcutContext(QtCore.Qt.WidgetShortcut)
        self.actionNew.setObjectName("actionNew")
        self.actionClose = QtGui.QAction(MainWindow)
        self.actionClose.setObjectName("actionClose")
        self.action50_micro = QtGui.QAction(MainWindow)
        self.action50_micro.setObjectName("action50_micro")
        self.action100_micro = QtGui.QAction(MainWindow)
        self.action100_micro.setObjectName("action100_micro")
        self.action250_micro = QtGui.QAction(MainWindow)
        self.action250_micro.setObjectName("action250_micro")
        self.action500_micro = QtGui.QAction(MainWindow)
        self.action500_micro.setObjectName("action500_micro")
        self.action1000 = QtGui.QAction(MainWindow)
        self.action1000.setObjectName("action1000")
        self.action5000_micro = QtGui.QAction(MainWindow)
        self.action5000_micro.setObjectName("action5000_micro")
        self.actionSyringe_Size = QtGui.QAction(MainWindow)
        self.actionSyringe_Size.setObjectName("actionSyringe_Size")
        self.actionPump_Parameters = QtGui.QAction(MainWindow)
        self.actionPump_Parameters.setObjectName("actionPump_Parameters")
        self.actionLeft_Valve = QtGui.QAction(MainWindow)
        self.actionLeft_Valve.setCheckable(False)
        self.actionLeft_Valve.setChecked(False)
        self.actionLeft_Valve.setObjectName("actionLeft_Valve")
        self.actionRight_Valve = QtGui.QAction(MainWindow)
        self.actionRight_Valve.setCheckable(False)
        self.actionRight_Valve.setObjectName("actionRight_Valve")
        self.actionClose_2 = QtGui.QAction(MainWindow)
        self.actionClose_2.setMenuRole(QtGui.QAction.QuitRole)
        self.actionClose_2.setObjectName("actionClose_2")
        self.actionLicense = QtGui.QAction(MainWindow)
        self.actionLicense.setObjectName("actionLicense")
        self.menuScript_2.addAction(self.actionOpen)
        self.menuScript_2.addAction(self.actionSave)
        self.menuScript_2.addAction(self.actionSaveAs)
        self.menuScript.addAction(self.menuScript_2.menuAction())
        self.menuScript.addAction(self.actionClose_2)
        self.menuOutput_Valve.addAction(self.actionLeft_Valve)
        self.menuOutput_Valve.addAction(self.actionRight_Valve)
        self.menuConnect.addAction(self.actionNew_Device)
        self.menuConnect.addAction(self.actionSyringe_Size)
        self.menuConnect.addAction(self.actionPump_Parameters)
        self.menuConnect.addAction(self.menuOutput_Valve.menuAction())
        self.menuHelp.addAction(self.actionCommands)
        self.menuHelp.addAction(self.actionAbout)
        self.menuHelp.addAction(self.actionLicense)
        self.menuView.addAction(self.actionReports)
        self.menuView.addAction(self.actionHistory)
        self.menubar.addAction(self.menuScript.menuAction())
        self.menubar.addAction(self.menuView.menuAction())
        self.menubar.addAction(self.menuConnect.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        self.quick_combobox.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "MainWindow", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setTitle(QtGui.QApplication.translate("MainWindow", "Fluid Transport", None, QtGui.QApplication.UnicodeUTF8))
        self.PushBtn.setText(QtGui.QApplication.translate("MainWindow", "Push Fluid", None, QtGui.QApplication.UnicodeUTF8))
        self.volume_label.setText(QtGui.QApplication.translate("MainWindow", "Volume to transport ", None, QtGui.QApplication.UnicodeUTF8))
        self.volume_prompt.setToolTip(QtGui.QApplication.translate("MainWindow", "Press <ENTER> to apply", None, QtGui.QApplication.UnicodeUTF8))
        self.volume_prompt.setStatusTip(QtGui.QApplication.translate("MainWindow", "Enter volume to transport", None, QtGui.QApplication.UnicodeUTF8))
        self.volume_prompt.setPlaceholderText(QtGui.QApplication.translate("MainWindow", "Volume [μL]", None, QtGui.QApplication.UnicodeUTF8))
        self.PullBtn.setText(QtGui.QApplication.translate("MainWindow", "Draw Fluid", None, QtGui.QApplication.UnicodeUTF8))
        self.volume_button.setText(QtGui.QApplication.translate("MainWindow", "Do it", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_2.setTitle(QtGui.QApplication.translate("MainWindow", "Plunger Speed", None, QtGui.QApplication.UnicodeUTF8))
        self.speed_slider.setStatusTip(QtGui.QApplication.translate("MainWindow", "Change the speed of the plunger [max value: 1]", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_4.setTitle(QtGui.QApplication.translate("MainWindow", "Valve Position", None, QtGui.QApplication.UnicodeUTF8))
        self.output_btn.setText(QtGui.QApplication.translate("MainWindow", "Output", None, QtGui.QApplication.UnicodeUTF8))
        self.input_btn.setText(QtGui.QApplication.translate("MainWindow", "Input", None, QtGui.QApplication.UnicodeUTF8))
        self.bypass_btn.setText(QtGui.QApplication.translate("MainWindow", "Bypass", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_3.setTitle(QtGui.QApplication.translate("MainWindow", "QuickCommands", None, QtGui.QApplication.UnicodeUTF8))
        self.quick_combobox.setStatusTip(QtGui.QApplication.translate("MainWindow", "Quick Commnads - Press \"Do it\" to apply", None, QtGui.QApplication.UnicodeUTF8))
        self.quick_combobox.setItemText(0, QtGui.QApplication.translate("MainWindow", "Push it All", None, QtGui.QApplication.UnicodeUTF8))
        self.quick_combobox.setItemText(1, QtGui.QApplication.translate("MainWindow", "Draw it All", None, QtGui.QApplication.UnicodeUTF8))
        self.quick_combobox.setItemText(2, QtGui.QApplication.translate("MainWindow", "Halt Execution", None, QtGui.QApplication.UnicodeUTF8))
        self.quick_combobox.setItemText(3, QtGui.QApplication.translate("MainWindow", "Apply GUI Values", None, QtGui.QApplication.UnicodeUTF8))
        self.address_combobox.setItemText(0, QtGui.QApplication.translate("MainWindow", "0", None, QtGui.QApplication.UnicodeUTF8))
        self.address_combobox.setItemText(1, QtGui.QApplication.translate("MainWindow", "1", None, QtGui.QApplication.UnicodeUTF8))
        self.address_combobox.setItemText(2, QtGui.QApplication.translate("MainWindow", "2", None, QtGui.QApplication.UnicodeUTF8))
        self.address_combobox.setItemText(3, QtGui.QApplication.translate("MainWindow", "3", None, QtGui.QApplication.UnicodeUTF8))
        self.address_combobox.setItemText(4, QtGui.QApplication.translate("MainWindow", "4", None, QtGui.QApplication.UnicodeUTF8))
        self.address_combobox.setItemText(5, QtGui.QApplication.translate("MainWindow", "5", None, QtGui.QApplication.UnicodeUTF8))
        self.address_combobox.setItemText(6, QtGui.QApplication.translate("MainWindow", "6", None, QtGui.QApplication.UnicodeUTF8))
        self.address_combobox.setItemText(7, QtGui.QApplication.translate("MainWindow", "7", None, QtGui.QApplication.UnicodeUTF8))
        self.address_combobox.setItemText(8, QtGui.QApplication.translate("MainWindow", "8", None, QtGui.QApplication.UnicodeUTF8))
        self.address_combobox.setItemText(9, QtGui.QApplication.translate("MainWindow", "9", None, QtGui.QApplication.UnicodeUTF8))
        self.address_combobox.setItemText(10, QtGui.QApplication.translate("MainWindow", "A", None, QtGui.QApplication.UnicodeUTF8))
        self.address_combobox.setItemText(11, QtGui.QApplication.translate("MainWindow", "B", None, QtGui.QApplication.UnicodeUTF8))
        self.address_combobox.setItemText(12, QtGui.QApplication.translate("MainWindow", "C", None, QtGui.QApplication.UnicodeUTF8))
        self.address_combobox.setItemText(13, QtGui.QApplication.translate("MainWindow", "D", None, QtGui.QApplication.UnicodeUTF8))
        self.address_combobox.setItemText(14, QtGui.QApplication.translate("MainWindow", "E", None, QtGui.QApplication.UnicodeUTF8))
        self.address_combobox.setItemText(15, QtGui.QApplication.translate("MainWindow", "F", None, QtGui.QApplication.UnicodeUTF8))
        self.make_it_so.setText(QtGui.QApplication.translate("MainWindow", "Do it", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("MainWindow", "Pump Address", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QtGui.QApplication.translate("MainWindow", "Tab 1", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_6.setTitle(QtGui.QApplication.translate("MainWindow", "Editor", None, QtGui.QApplication.UnicodeUTF8))
        self.textEdit.setHtml(QtGui.QApplication.translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'.Helvetica Neue DeskInterface\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'.Lucida Grande UI\';\">pump.initialize_pump(output = \'left\')</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'.Lucida Grande UI\';\"># This is the Example Script </span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'.Lucida Grande UI\';\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'.Lucida Grande UI\';\">pump.property_set(\'speed\', \'5\')</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'.Lucida Grande UI\';\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'.Lucida Grande UI\';\">pump.send_Command(\'A3000\')</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'.Lucida Grande UI\';\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'.Lucida Grande UI\';\">pump.send_Command(\'A0\')</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'.Lucida Grande UI\';\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'.Lucida Grande UI\';\">pump.property_set(\'speed\', \'1\')</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'.Lucida Grande UI\';\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'.Lucida Grande UI\';\">pump.send_Command(\'A3000\')</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'.Lucida Grande UI\';\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'.Lucida Grande UI\';\">pump.send_Command(\'A0\')</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.run_script_btn.setText(QtGui.QApplication.translate("MainWindow", "Run Script", None, QtGui.QApplication.UnicodeUTF8))
        self.clear_editor_btn.setText(QtGui.QApplication.translate("MainWindow", "Clear Editor", None, QtGui.QApplication.UnicodeUTF8))
        self.back_interactive_btn.setText(QtGui.QApplication.translate("MainWindow", "Back to \n"
"Interactive", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QtGui.QApplication.translate("MainWindow", "Tab 2", None, QtGui.QApplication.UnicodeUTF8))
        self.menuScript.setTitle(QtGui.QApplication.translate("MainWindow", "Actions", None, QtGui.QApplication.UnicodeUTF8))
        self.menuScript_2.setTitle(QtGui.QApplication.translate("MainWindow", "Script", None, QtGui.QApplication.UnicodeUTF8))
        self.menuConnect.setTitle(QtGui.QApplication.translate("MainWindow", "Configure", None, QtGui.QApplication.UnicodeUTF8))
        self.menuOutput_Valve.setTitle(QtGui.QApplication.translate("MainWindow", "Output Valve", None, QtGui.QApplication.UnicodeUTF8))
        self.menuHelp.setTitle(QtGui.QApplication.translate("MainWindow", "Help", None, QtGui.QApplication.UnicodeUTF8))
        self.menuView.setTitle(QtGui.QApplication.translate("MainWindow", "View", None, QtGui.QApplication.UnicodeUTF8))
        self.actionNew_2.setText(QtGui.QApplication.translate("MainWindow", "New", None, QtGui.QApplication.UnicodeUTF8))
        self.actionOpen.setText(QtGui.QApplication.translate("MainWindow", "Open", None, QtGui.QApplication.UnicodeUTF8))
        self.actionOpen.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+O", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSave.setText(QtGui.QApplication.translate("MainWindow", "Save", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSave.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+S", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSaveAs.setText(QtGui.QApplication.translate("MainWindow", "Save as...", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSaveAs.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+Shift+S", None, QtGui.QApplication.UnicodeUTF8))
        self.actionNew_Device.setText(QtGui.QApplication.translate("MainWindow", "Port...", None, QtGui.QApplication.UnicodeUTF8))
        self.actionNew_Device.setWhatsThis(QtGui.QApplication.translate("MainWindow", "Configure the current pump", None, QtGui.QApplication.UnicodeUTF8))
        self.actionNew_Device.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+P", None, QtGui.QApplication.UnicodeUTF8))
        self.actionAbout.setText(QtGui.QApplication.translate("MainWindow", "About", None, QtGui.QApplication.UnicodeUTF8))
        self.actionCommands.setText(QtGui.QApplication.translate("MainWindow", "Editor Help", None, QtGui.QApplication.UnicodeUTF8))
        self.actionReports.setText(QtGui.QApplication.translate("MainWindow", "Reports...", None, QtGui.QApplication.UnicodeUTF8))
        self.actionReports.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+R", None, QtGui.QApplication.UnicodeUTF8))
        self.actionHistory.setText(QtGui.QApplication.translate("MainWindow", "History...", None, QtGui.QApplication.UnicodeUTF8))
        self.actionHistory.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+K", None, QtGui.QApplication.UnicodeUTF8))
        self.actionNew.setText(QtGui.QApplication.translate("MainWindow", "New", None, QtGui.QApplication.UnicodeUTF8))
        self.actionNew.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+N", None, QtGui.QApplication.UnicodeUTF8))
        self.actionClose.setText(QtGui.QApplication.translate("MainWindow", "Close", None, QtGui.QApplication.UnicodeUTF8))
        self.actionClose.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+W", None, QtGui.QApplication.UnicodeUTF8))
        self.action50_micro.setText(QtGui.QApplication.translate("MainWindow", "50 micro", None, QtGui.QApplication.UnicodeUTF8))
        self.action100_micro.setText(QtGui.QApplication.translate("MainWindow", "100 micro", None, QtGui.QApplication.UnicodeUTF8))
        self.action250_micro.setText(QtGui.QApplication.translate("MainWindow", "250 micro", None, QtGui.QApplication.UnicodeUTF8))
        self.action500_micro.setText(QtGui.QApplication.translate("MainWindow", "500 micro", None, QtGui.QApplication.UnicodeUTF8))
        self.action1000.setText(QtGui.QApplication.translate("MainWindow", "1000 micro", None, QtGui.QApplication.UnicodeUTF8))
        self.action5000_micro.setText(QtGui.QApplication.translate("MainWindow", "5000 micro", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSyringe_Size.setText(QtGui.QApplication.translate("MainWindow", "Syringe Size...", None, QtGui.QApplication.UnicodeUTF8))
        self.actionPump_Parameters.setText(QtGui.QApplication.translate("MainWindow", "Pump Parameters...", None, QtGui.QApplication.UnicodeUTF8))
        self.actionLeft_Valve.setText(QtGui.QApplication.translate("MainWindow", "Left Valve", None, QtGui.QApplication.UnicodeUTF8))
        self.actionRight_Valve.setText(QtGui.QApplication.translate("MainWindow", "Right Valve", None, QtGui.QApplication.UnicodeUTF8))
        self.actionClose_2.setText(QtGui.QApplication.translate("MainWindow", "Close", None, QtGui.QApplication.UnicodeUTF8))
        self.actionLicense.setText(QtGui.QApplication.translate("MainWindow", "License", None, QtGui.QApplication.UnicodeUTF8))

