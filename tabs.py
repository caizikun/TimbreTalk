# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'tabs.ui'
#
# Created: Fri Oct 26 08:34:35 2012
#      by: PyQt4 UI code generator 4.9.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_TabWidget(object):
    def setupUi(self, TabWidget):
        TabWidget.setObjectName(_fromUtf8("TabWidget"))
        TabWidget.resize(351, 381)
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.groupBox = QtGui.QGroupBox(self.tab)
        self.groupBox.setGeometry(QtCore.QRect(10, 170, 331, 171))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.layoutWidget = QtGui.QWidget(self.groupBox)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 40, 311, 127))
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.verticalLayout_4 = QtGui.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_4.setMargin(0)
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.horizontalLayout_6 = QtGui.QHBoxLayout()
        self.horizontalLayout_6.setObjectName(_fromUtf8("horizontalLayout_6"))
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.InBuffered = QtGui.QRadioButton(self.layoutWidget)
        self.InBuffered.setObjectName(_fromUtf8("InBuffered"))
        self.horizontalLayout_3.addWidget(self.InBuffered)
        self.InRaw = QtGui.QRadioButton(self.layoutWidget)
        self.InRaw.setChecked(True)
        self.InRaw.setObjectName(_fromUtf8("InRaw"))
        self.horizontalLayout_3.addWidget(self.InRaw)
        self.InRawEcho = QtGui.QRadioButton(self.layoutWidget)
        self.InRawEcho.setObjectName(_fromUtf8("InRawEcho"))
        self.horizontalLayout_3.addWidget(self.InRawEcho)
        self.horizontalLayout_6.addLayout(self.horizontalLayout_3)
        self.InHex = QtGui.QCheckBox(self.layoutWidget)
        self.InHex.setObjectName(_fromUtf8("InHex"))
        self.horizontalLayout_6.addWidget(self.InHex)
        self.verticalLayout_4.addLayout(self.horizontalLayout_6)
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.LFnada = QtGui.QRadioButton(self.layoutWidget)
        self.LFnada.setChecked(True)
        self.LFnada.setObjectName(_fromUtf8("LFnada"))
        self.gridLayout.addWidget(self.LFnada, 1, 1, 1, 1)
        self.label_2 = QtGui.QLabel(self.layoutWidget)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)
        self.label_3 = QtGui.QLabel(self.layoutWidget)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout.addWidget(self.label_3, 1, 0, 1, 1)
        self.CRCR = QtGui.QRadioButton(self.layoutWidget)
        self.CRCR.setChecked(False)
        self.CRCR.setObjectName(_fromUtf8("CRCR"))
        self.gridLayout.addWidget(self.CRCR, 0, 3, 1, 1)
        self.CRnada = QtGui.QRadioButton(self.layoutWidget)
        self.CRnada.setObjectName(_fromUtf8("CRnada"))
        self.gridLayout.addWidget(self.CRnada, 0, 1, 1, 1)
        self.LFLF = QtGui.QRadioButton(self.layoutWidget)
        self.LFLF.setObjectName(_fromUtf8("LFLF"))
        self.gridLayout.addWidget(self.LFLF, 1, 2, 1, 1)
        self.LFCR = QtGui.QRadioButton(self.layoutWidget)
        self.LFCR.setObjectName(_fromUtf8("LFCR"))
        self.gridLayout.addWidget(self.LFCR, 1, 3, 1, 1)
        self.CRLF = QtGui.QRadioButton(self.layoutWidget)
        self.CRLF.setChecked(False)
        self.CRLF.setObjectName(_fromUtf8("CRLF"))
        self.gridLayout.addWidget(self.CRLF, 0, 2, 1, 1)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 0, 4, 1, 1)
        self.verticalLayout_4.addLayout(self.gridLayout)
        self.horizontalLayout_12 = QtGui.QHBoxLayout()
        self.horizontalLayout_12.setObjectName(_fromUtf8("horizontalLayout_12"))
        self.label_21 = QtGui.QLabel(self.layoutWidget)
        self.label_21.setObjectName(_fromUtf8("label_21"))
        self.horizontalLayout_12.addWidget(self.label_21)
        self.inputIgnore = QtGui.QComboBox(self.layoutWidget)
        self.inputIgnore.setObjectName(_fromUtf8("inputIgnore"))
        self.inputIgnore.addItem(_fromUtf8(""))
        self.inputIgnore.addItem(_fromUtf8(""))
        self.inputIgnore.addItem(_fromUtf8(""))
        self.inputIgnore.addItem(_fromUtf8(""))
        self.horizontalLayout_12.addWidget(self.inputIgnore)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_12.addItem(spacerItem1)
        self.verticalLayout_4.addLayout(self.horizontalLayout_12)
        self.groupBox_2 = QtGui.QGroupBox(self.tab)
        self.groupBox_2.setGeometry(QtCore.QRect(10, 0, 331, 171))
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.layoutWidget_2 = QtGui.QWidget(self.groupBox_2)
        self.layoutWidget_2.setGeometry(QtCore.QRect(10, 20, 251, 145))
        self.layoutWidget_2.setObjectName(_fromUtf8("layoutWidget_2"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.layoutWidget_2)
        self.verticalLayout_3.setMargin(0)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.Serial1 = QtGui.QRadioButton(self.layoutWidget_2)
        self.Serial1.setChecked(True)
        self.Serial1.setObjectName(_fromUtf8("Serial1"))
        self.horizontalLayout.addWidget(self.Serial1)
        self.SFP = QtGui.QRadioButton(self.layoutWidget_2)
        self.SFP.setObjectName(_fromUtf8("SFP"))
        self.horizontalLayout.addWidget(self.SFP)
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.LoopBack = QtGui.QCheckBox(self.layoutWidget_2)
        self.LoopBack.setObjectName(_fromUtf8("LoopBack"))
        self.horizontalLayout_2.addWidget(self.LoopBack)
        self.ProtocolDump = QtGui.QCheckBox(self.layoutWidget_2)
        self.ProtocolDump.setObjectName(_fromUtf8("ProtocolDump"))
        self.horizontalLayout_2.addWidget(self.ProtocolDump)
        self.verticalLayout_3.addLayout(self.horizontalLayout_2)
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.horizontalLayout_10 = QtGui.QHBoxLayout()
        self.horizontalLayout_10.setObjectName(_fromUtf8("horizontalLayout_10"))
        self.SerialPort = QtGui.QComboBox(self.layoutWidget_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.SerialPort.sizePolicy().hasHeightForWidth())
        self.SerialPort.setSizePolicy(sizePolicy)
        self.SerialPort.setObjectName(_fromUtf8("SerialPort"))
        self.SerialPort.addItem(_fromUtf8(""))
        self.horizontalLayout_10.addWidget(self.SerialPort)
        self.BaudRate = QtGui.QComboBox(self.layoutWidget_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.BaudRate.sizePolicy().hasHeightForWidth())
        self.BaudRate.setSizePolicy(sizePolicy)
        self.BaudRate.setAcceptDrops(False)
        self.BaudRate.setFrame(True)
        self.BaudRate.setObjectName(_fromUtf8("BaudRate"))
        self.BaudRate.addItem(_fromUtf8(""))
        self.BaudRate.addItem(_fromUtf8(""))
        self.BaudRate.addItem(_fromUtf8(""))
        self.BaudRate.addItem(_fromUtf8(""))
        self.BaudRate.addItem(_fromUtf8(""))
        self.BaudRate.addItem(_fromUtf8(""))
        self.BaudRate.addItem(_fromUtf8(""))
        self.BaudRate.addItem(_fromUtf8(""))
        self.BaudRate.addItem(_fromUtf8(""))
        self.horizontalLayout_10.addWidget(self.BaudRate)
        self.verticalLayout_2.addLayout(self.horizontalLayout_10)
        self.horizontalLayout_11 = QtGui.QHBoxLayout()
        self.horizontalLayout_11.setObjectName(_fromUtf8("horizontalLayout_11"))
        spacerItem3 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_11.addItem(spacerItem3)
        self.ResetRcvr = QtGui.QPushButton(self.layoutWidget_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ResetRcvr.sizePolicy().hasHeightForWidth())
        self.ResetRcvr.setSizePolicy(sizePolicy)
        self.ResetRcvr.setObjectName(_fromUtf8("ResetRcvr"))
        self.horizontalLayout_11.addWidget(self.ResetRcvr)
        self.Ping = QtGui.QPushButton(self.layoutWidget_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Ping.sizePolicy().hasHeightForWidth())
        self.Ping.setSizePolicy(sizePolicy)
        self.Ping.setObjectName(_fromUtf8("Ping"))
        self.horizontalLayout_11.addWidget(self.Ping)
        spacerItem4 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_11.addItem(spacerItem4)
        self.verticalLayout_2.addLayout(self.horizontalLayout_11)
        self.verticalLayout_3.addLayout(self.verticalLayout_2)
        TabWidget.addTab(self.tab, _fromUtf8(""))
        self.tab1 = QtGui.QWidget()
        self.tab1.setObjectName(_fromUtf8("tab1"))
        TabWidget.addTab(self.tab1, _fromUtf8(""))

        self.retranslateUi(TabWidget)
        TabWidget.setCurrentIndex(0)
        self.BaudRate.setCurrentIndex(5)
        QtCore.QMetaObject.connectSlotsByName(TabWidget)

    def retranslateUi(self, TabWidget):
        TabWidget.setWindowTitle(QtGui.QApplication.translate("TabWidget", "TabWidget", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setTitle(QtGui.QApplication.translate("TabWidget", "Input/Output", None, QtGui.QApplication.UnicodeUTF8))
        self.InBuffered.setText(QtGui.QApplication.translate("TabWidget", "Buffered", None, QtGui.QApplication.UnicodeUTF8))
        self.InRaw.setText(QtGui.QApplication.translate("TabWidget", "Raw", None, QtGui.QApplication.UnicodeUTF8))
        self.InRawEcho.setText(QtGui.QApplication.translate("TabWidget", "Raw+Echo", None, QtGui.QApplication.UnicodeUTF8))
        self.InHex.setText(QtGui.QApplication.translate("TabWidget", "+Hex", None, QtGui.QApplication.UnicodeUTF8))
        self.LFnada.setText(QtGui.QApplication.translate("TabWidget", "nada", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("TabWidget", "Output CR as:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("TabWidget", "Output LF as:", None, QtGui.QApplication.UnicodeUTF8))
        self.CRCR.setText(QtGui.QApplication.translate("TabWidget", "CR", None, QtGui.QApplication.UnicodeUTF8))
        self.CRnada.setText(QtGui.QApplication.translate("TabWidget", "nada", None, QtGui.QApplication.UnicodeUTF8))
        self.LFLF.setText(QtGui.QApplication.translate("TabWidget", "LF", None, QtGui.QApplication.UnicodeUTF8))
        self.LFCR.setText(QtGui.QApplication.translate("TabWidget", "CR", None, QtGui.QApplication.UnicodeUTF8))
        self.CRLF.setText(QtGui.QApplication.translate("TabWidget", "LF", None, QtGui.QApplication.UnicodeUTF8))
        self.label_21.setText(QtGui.QApplication.translate("TabWidget", "Input:", None, QtGui.QApplication.UnicodeUTF8))
        self.inputIgnore.setItemText(0, QtGui.QApplication.translate("TabWidget", "Passive", None, QtGui.QApplication.UnicodeUTF8))
        self.inputIgnore.setItemText(1, QtGui.QApplication.translate("TabWidget", "Ignore CR", None, QtGui.QApplication.UnicodeUTF8))
        self.inputIgnore.setItemText(2, QtGui.QApplication.translate("TabWidget", "Ignore LF", None, QtGui.QApplication.UnicodeUTF8))
        self.inputIgnore.setItemText(3, QtGui.QApplication.translate("TabWidget", "Ignore CRLF", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_2.setTitle(QtGui.QApplication.translate("TabWidget", "Port Settings", None, QtGui.QApplication.UnicodeUTF8))
        self.Serial1.setText(QtGui.QApplication.translate("TabWidget", "Serial", None, QtGui.QApplication.UnicodeUTF8))
        self.SFP.setText(QtGui.QApplication.translate("TabWidget", "SFP", None, QtGui.QApplication.UnicodeUTF8))
        self.LoopBack.setText(QtGui.QApplication.translate("TabWidget", "Loop back", None, QtGui.QApplication.UnicodeUTF8))
        self.ProtocolDump.setText(QtGui.QApplication.translate("TabWidget", "Protocol Dump", None, QtGui.QApplication.UnicodeUTF8))
        self.SerialPort.setItemText(0, QtGui.QApplication.translate("TabWidget", "(Select a Port)", None, QtGui.QApplication.UnicodeUTF8))
        self.BaudRate.setItemText(0, QtGui.QApplication.translate("TabWidget", "9600", None, QtGui.QApplication.UnicodeUTF8))
        self.BaudRate.setItemText(1, QtGui.QApplication.translate("TabWidget", "19200", None, QtGui.QApplication.UnicodeUTF8))
        self.BaudRate.setItemText(2, QtGui.QApplication.translate("TabWidget", "28800", None, QtGui.QApplication.UnicodeUTF8))
        self.BaudRate.setItemText(3, QtGui.QApplication.translate("TabWidget", "38400", None, QtGui.QApplication.UnicodeUTF8))
        self.BaudRate.setItemText(4, QtGui.QApplication.translate("TabWidget", "57600", None, QtGui.QApplication.UnicodeUTF8))
        self.BaudRate.setItemText(5, QtGui.QApplication.translate("TabWidget", "115200", None, QtGui.QApplication.UnicodeUTF8))
        self.BaudRate.setItemText(6, QtGui.QApplication.translate("TabWidget", "230400", None, QtGui.QApplication.UnicodeUTF8))
        self.BaudRate.setItemText(7, QtGui.QApplication.translate("TabWidget", "460800", None, QtGui.QApplication.UnicodeUTF8))
        self.BaudRate.setItemText(8, QtGui.QApplication.translate("TabWidget", "500000", None, QtGui.QApplication.UnicodeUTF8))
        self.ResetRcvr.setText(QtGui.QApplication.translate("TabWidget", "Reset Rcvr", None, QtGui.QApplication.UnicodeUTF8))
        self.Ping.setText(QtGui.QApplication.translate("TabWidget", "Ping", None, QtGui.QApplication.UnicodeUTF8))
        TabWidget.setTabText(TabWidget.indexOf(self.tab), QtGui.QApplication.translate("TabWidget", "Tab 1", None, QtGui.QApplication.UnicodeUTF8))
        TabWidget.setTabText(TabWidget.indexOf(self.tab1), QtGui.QApplication.translate("TabWidget", "Tab 2", None, QtGui.QApplication.UnicodeUTF8))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    TabWidget = QtGui.QTabWidget()
    ui = Ui_TabWidget()
    ui.setupUi(TabWidget)
    TabWidget.show()
    sys.exit(app.exec_())

