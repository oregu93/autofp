# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'order.ui'
#
# Created: Thu Mar 31 14:55:52 2016
#      by: PyQt4 UI code generator 4.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Order(object):
    def setupUi(self, Order):
        Order.setObjectName(_fromUtf8("Order"))
        Order.resize(584, 556)
        Order.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        Order.setStyleSheet(_fromUtf8(""))
        Order.setSizeGripEnabled(False)
        Order.setModal(False)
        self.tabWidget = QtGui.QTabWidget(Order)
        self.tabWidget.setGeometry(QtCore.QRect(0, 20, 591, 500))
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.table = QtGui.QTableWidget(self.tab)
        self.table.setGeometry(QtCore.QRect(0, 0, 441, 471))
        self.table.setMinimumSize(QtCore.QSize(441, 450))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.table.setFont(font)
        self.table.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.table.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.table.setStyleSheet(_fromUtf8(""))
        self.table.setLineWidth(5)
        self.table.setMidLineWidth(-8)
        self.table.setAutoScrollMargin(50)
        self.table.setAlternatingRowColors(True)
        self.table.setRowCount(0)
        self.table.setColumnCount(2)
        self.table.setObjectName(_fromUtf8("table"))
        self.buttonBox = QtGui.QDialogButtonBox(self.tab)
        self.buttonBox.setGeometry(QtCore.QRect(490, 370, 81, 241))
        self.buttonBox.setOrientation(QtCore.Qt.Vertical)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.button_up = QtGui.QPushButton(self.tab)
        self.button_up.setGeometry(QtCore.QRect(490, 90, 75, 61))
        self.button_up.setObjectName(_fromUtf8("button_up"))
        self.button_down = QtGui.QPushButton(self.tab)
        self.button_down.setGeometry(QtCore.QRect(490, 210, 75, 61))
        self.button_down.setObjectName(_fromUtf8("button_down"))
        self.buttonreset = QtGui.QPushButton(self.tab)
        self.buttonreset.setGeometry(QtCore.QRect(490, 430, 81, 21))
        self.buttonreset.setObjectName(_fromUtf8("buttonreset"))
        self.button_configure_s = QtGui.QPushButton(self.tab)
        self.button_configure_s.setGeometry(QtCore.QRect(490, 330, 82, 25))
        self.button_configure_s.setObjectName(_fromUtf8("button_configure_s"))
        self.tabWidget.addTab(self.tab, _fromUtf8(""))
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName(_fromUtf8("tab_2"))
        self.text_asylim = QtGui.QLineEdit(self.tab_2)
        self.text_asylim.setGeometry(QtCore.QRect(90, 30, 113, 20))
        self.text_asylim.setObjectName(_fromUtf8("text_asylim"))
        self.label = QtGui.QLabel(self.tab_2)
        self.label.setGeometry(QtCore.QRect(10, 30, 71, 21))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("SimSun-ExtB"))
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(self.tab_2)
        self.label_2.setGeometry(QtCore.QRect(10, 70, 71, 21))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("SimSun-ExtB"))
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.spinbox_eps = QtGui.QSpinBox(self.tab_2)
        self.spinbox_eps.setGeometry(QtCore.QRect(90, 70, 111, 22))
        self.spinbox_eps.setMinimum(1)
        self.spinbox_eps.setMaximum(100)
        self.spinbox_eps.setProperty("value", 10)
        self.spinbox_eps.setObjectName(_fromUtf8("spinbox_eps"))
        self.tabWidget_2 = QtGui.QTabWidget(self.tab_2)
        self.tabWidget_2.setGeometry(QtCore.QRect(10, 120, 541, 351))
        self.tabWidget_2.setObjectName(_fromUtf8("tabWidget_2"))
        self.tab_5 = QtGui.QWidget()
        self.tab_5.setObjectName(_fromUtf8("tab_5"))
        self.text_fp2k_path = QtGui.QTextEdit(self.tab_5)
        self.text_fp2k_path.setEnabled(False)
        self.text_fp2k_path.setGeometry(QtCore.QRect(90, 27, 401, 21))
        self.text_fp2k_path.setObjectName(_fromUtf8("text_fp2k_path"))
        self.label_3 = QtGui.QLabel(self.tab_5)
        self.label_3.setGeometry(QtCore.QRect(10, 30, 81, 16))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.text_origin_path = QtGui.QTextEdit(self.tab_5)
        self.text_origin_path.setEnabled(False)
        self.text_origin_path.setGeometry(QtCore.QRect(90, 60, 401, 21))
        self.text_origin_path.setObjectName(_fromUtf8("text_origin_path"))
        self.label_5 = QtGui.QLabel(self.tab_5)
        self.label_5.setGeometry(QtCore.QRect(5, 65, 80, 12))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.button_configure = QtGui.QPushButton(self.tab_5)
        self.button_configure.setGeometry(QtCore.QRect(410, 110, 82, 25))
        self.button_configure.setObjectName(_fromUtf8("button_configure"))
        self.tabWidget_2.addTab(self.tab_5, _fromUtf8(""))
        self.label_4 = QtGui.QLabel(self.tab_2)
        self.label_4.setGeometry(QtCore.QRect(300, 33, 54, 12))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.spinbox_ncy = QtGui.QSpinBox(self.tab_2)
        self.spinbox_ncy.setGeometry(QtCore.QRect(340, 30, 111, 22))
        self.spinbox_ncy.setMinimum(0)
        self.spinbox_ncy.setMaximum(100000)
        self.spinbox_ncy.setProperty("value", 10)
        self.spinbox_ncy.setObjectName(_fromUtf8("spinbox_ncy"))
        self.tabWidget.addTab(self.tab_2, _fromUtf8(""))
        self.tab_3 = QtGui.QWidget()
        self.tab_3.setEnabled(True)
        self.tab_3.setObjectName(_fromUtf8("tab_3"))
        self.tab_widget = QtGui.QTabWidget(self.tab_3)
        self.tab_widget.setEnabled(True)
        self.tab_widget.setGeometry(QtCore.QRect(10, 20, 571, 271))
        self.tab_widget.setObjectName(_fromUtf8("tab_widget"))
        self.tab_4 = QtGui.QWidget()
        self.tab_4.setObjectName(_fromUtf8("tab_4"))
        self.checkBox_hkl = QtGui.QCheckBox(self.tab_4)
        self.checkBox_hkl.setEnabled(False)
        self.checkBox_hkl.setGeometry(QtCore.QRect(30, 40, 151, 21))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Segoe UI"))
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.checkBox_hkl.setFont(font)
        self.checkBox_hkl.setObjectName(_fromUtf8("checkBox_hkl"))
        self.checkBox_cif = QtGui.QCheckBox(self.tab_4)
        self.checkBox_cif.setEnabled(True)
        self.checkBox_cif.setGeometry(QtCore.QRect(30, 80, 151, 21))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Segoe UI"))
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.checkBox_cif.setFont(font)
        self.checkBox_cif.setObjectName(_fromUtf8("checkBox_cif"))
        self.checkBox_fou = QtGui.QCheckBox(self.tab_4)
        self.checkBox_fou.setEnabled(False)
        self.checkBox_fou.setGeometry(QtCore.QRect(30, 120, 151, 21))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Segoe UI"))
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.checkBox_fou.setFont(font)
        self.checkBox_fou.setObjectName(_fromUtf8("checkBox_fou"))
        self.tab_widget.addTab(self.tab_4, _fromUtf8(""))
        self.tabWidget.addTab(self.tab_3, _fromUtf8(""))
        self.button_save = QtGui.QPushButton(Order)
        self.button_save.setGeometry(QtCore.QRect(460, 530, 111, 21))
        self.button_save.setInputMethodHints(QtCore.Qt.ImhDialableCharactersOnly|QtCore.Qt.ImhDigitsOnly|QtCore.Qt.ImhEmailCharactersOnly|QtCore.Qt.ImhFormattedNumbersOnly|QtCore.Qt.ImhLowercaseOnly|QtCore.Qt.ImhUppercaseOnly|QtCore.Qt.ImhUrlCharactersOnly)
        self.button_save.setObjectName(_fromUtf8("button_save"))

        self.retranslateUi(Order)
        self.tabWidget.setCurrentIndex(0)
        self.tabWidget_2.setCurrentIndex(0)
        self.tab_widget.setCurrentIndex(0)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), Order.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), Order.reject)
        QtCore.QMetaObject.connectSlotsByName(Order)

    def retranslateUi(self, Order):
        Order.setWindowTitle(_translate("Order", "Setting", None))
        self.button_up.setText(_translate("Order", "Up", None))
        self.button_down.setText(_translate("Order", "Down", None))
        self.buttonreset.setText(_translate("Order", "Reset", None))
        self.button_configure_s.setText(_translate("Order", "configure", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Order", "Strategy", None))
        self.text_asylim.setToolTip(_translate("Order", "<html><head/><body><p><span style=\" color:#000000;\">defined by &quot;Asylim in *.PCR&quot;</span></p></body></html>", None))
        self.text_asylim.setText(_translate("Order", "60", None))
        self.label.setText(_translate("Order", "Asylim:", None))
        self.label_2.setText(_translate("Order", "eps %:", None))
        self.spinbox_eps.setToolTip(_translate("Order", "<html><head/><body><p align=\"justify\"><span style=\" color:#000000;\">Convergence tolerance for &quot; Cycle = 0 Mode&quot;</span></p><p align=\"justify\"><span style=\" color:#000000;\">in Cycle=0 Mode</span></p><p align=\"justify\"><span style=\" color:#000000;\">if Rwp(end)-Rwp(start)&lt;eps:</span></p><p align=\"justify\"><span style=\" color:#000000;\">exit refinement loop </span></p></body></html>", None))
        self.spinbox_eps.setWhatsThis(_translate("Order", "<html><head/><body><p><span style=\" font-size:16pt;\">Convergence tolerance for &quot; Cycle = 0 Mode&quot;</span></p><p><span style=\" font-size:16pt;\">in Cycle=0 Mode</span></p><p><span style=\" font-size:16pt;\">if Rwp(end)-Rwp(start)&lt;eps:</span></p><p><span style=\" font-size:16pt;\">    exit refinement loop </span></p></body></html>", None))
        self.text_fp2k_path.setToolTip(_translate("Order", "<html><head/><body><p>the path of fp2k.exe</p></body></html>", None))
        self.text_fp2k_path.setHtml(_translate("Order", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">./fp2k.exe</p></body></html>", None))
        self.label_3.setText(_translate("Order", "fp2k path:", None))
        self.text_origin_path.setToolTip(_translate("Order", "<html><head/><body><p>the path of fp2k.exe</p></body></html>", None))
        self.text_origin_path.setHtml(_translate("Order", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">origin.exe</p></body></html>", None))
        self.label_5.setText(_translate("Order", "Origin path:", None))
        self.button_configure.setText(_translate("Order", "configure", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_5), _translate("Order", "system", None))
        self.label_4.setText(_translate("Order", "NCY", None))
        self.spinbox_ncy.setToolTip(_translate("Order", "<html><head/><body><p><span style=\" color:#000000;\">defined by &quot;NCY in PCR&quot;</span></p><p><span style=\" color:#000000;\">It means that fp2k run NCY times each time</span></p></body></html>", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("Order", "Parameters", None))
        self.checkBox_hkl.setText(_translate("Order", "Hkl", None))
        self.checkBox_cif.setText(_translate("Order", "Cif", None))
        self.checkBox_fou.setText(_translate("Order", "Fou", None))
        self.tab_widget.setTabText(self.tab_widget.indexOf(self.tab_4), _translate("Order", "output", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("Order", "Output", None))
        self.button_save.setText(_translate("Order", "reload setting", None))

