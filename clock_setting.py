# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'clock_setting.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(312, 160)
        Form.setMinimumSize(QtCore.QSize(312, 160))
        Form.setMaximumSize(QtCore.QSize(312, 160))
        self.timeDisplay = QtWidgets.QTextEdit(Form)
        self.timeDisplay.setEnabled(True)
        self.timeDisplay.setGeometry(QtCore.QRect(10, 10, 211, 71))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.timeDisplay.setFont(font)
        self.timeDisplay.setReadOnly(True)
        self.timeDisplay.setObjectName("timeDisplay")
        self.buttonConnect = QtWidgets.QPushButton(Form)
        self.buttonConnect.setEnabled(False)
        self.buttonConnect.setGeometry(QtCore.QRect(230, 40, 71, 23))
        self.buttonConnect.setObjectName("buttonConnect")
        self.comPortBox = QtWidgets.QComboBox(Form)
        self.comPortBox.setGeometry(QtCore.QRect(230, 10, 69, 22))
        self.comPortBox.setObjectName("comPortBox")
        self.buttonAply = QtWidgets.QPushButton(Form)
        self.buttonAply.setEnabled(False)
        self.buttonAply.setGeometry(QtCore.QRect(230, 70, 71, 23))
        self.buttonAply.setObjectName("buttonAply")
        self.groupBox = QtWidgets.QGroupBox(Form)
        self.groupBox.setGeometry(QtCore.QRect(10, 90, 291, 61))
        self.groupBox.setObjectName("groupBox")
        self.buttonLed_1 = QtWidgets.QPushButton(self.groupBox)
        self.buttonLed_1.setGeometry(QtCore.QRect(10, 20, 41, 23))
        self.buttonLed_1.setObjectName("buttonLed_1")
        self.buttonLed_2 = QtWidgets.QPushButton(self.groupBox)
        self.buttonLed_2.setGeometry(QtCore.QRect(60, 20, 41, 23))
        self.buttonLed_2.setObjectName("buttonLed_2")
        self.buttonLed_3 = QtWidgets.QPushButton(self.groupBox)
        self.buttonLed_3.setGeometry(QtCore.QRect(110, 20, 41, 23))
        self.buttonLed_3.setObjectName("buttonLed_3")
        self.buttonLed_4 = QtWidgets.QPushButton(self.groupBox)
        self.buttonLed_4.setGeometry(QtCore.QRect(160, 20, 41, 23))
        self.buttonLed_4.setObjectName("buttonLed_4")
        self.buttonLed_Off = QtWidgets.QPushButton(self.groupBox)
        self.buttonLed_Off.setGeometry(QtCore.QRect(210, 20, 71, 23))
        self.buttonLed_Off.setObjectName("buttonLed_Off")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "STM32 Clock"))
        self.timeDisplay.setPlaceholderText(_translate("Form", "12:59:59"))
        self.buttonConnect.setText(_translate("Form", "Connect"))
        self.buttonAply.setText(_translate("Form", "aply"))
        self.groupBox.setTitle(_translate("Form", "Led Control"))
        self.buttonLed_1.setText(_translate("Form", "led 1"))
        self.buttonLed_2.setText(_translate("Form", "led 2"))
        self.buttonLed_3.setText(_translate("Form", "led 3"))
        self.buttonLed_4.setText(_translate("Form", "led 4"))
        self.buttonLed_Off.setText(_translate("Form", "led off"))
