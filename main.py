import sys
import serial
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QMainWindow
from clock_setting import *
from thread_func import TimeHandler, STM_Board_Ports, STM_Read_Port

# pyuic5  clock_setting.ui -o clock_setting.py

class Clock(QMainWindow, Ui_Form):

    def __init__(self):
        super(Clock, self).__init__()
        self.setupUi(self)
        self.buttonConnect.clicked.connect(self.press_connect)
        self.button_SyncTime.clicked.connect(self.press_sync_time)
        self.buttonLed_1.clicked.connect(self.press_button_led_1)
        self.buttonLed_2.clicked.connect(self.press_button_led_2)
        self.buttonLed_3.clicked.connect(self.press_button_led_3)
        self.buttonLed_4.clicked.connect(self.press_button_led_4)
        self.buttonLed_Off.clicked.connect(self.press_button_led_off)
        self.button_Disconnect.clicked.connect(self.press_button_disconnect)
        self.button_Disconnect.setHidden(True)
        self.connected = False
        self.com = STM_Read_Port(self)
        self.tmh = TimeHandler(self)
        self.ports = STM_Board_Ports(self)
        self.start_prin_time_now()
        self.get_ports()

    def start_prin_time_now(self):
        self.tmh.signal.connect(self.print_time_now)
        self.tmh.start()

    @pyqtSlot(str)
    def print_time_now(self, t):
        self.timeDisplay.setText(t)

    def get_ports(self):
        self.ports.signal.connect(self.set_ports)
        self.ports.start()

    @pyqtSlot(list)
    def set_ports(self, ports):
        if len(ports) > 0:
            self.comPortBox.addItems(ports)
            self.buttonConnect.setEnabled(True)
            self.button_SyncTime.setEnabled(True)

    def closeEvent(self, event):
        self.tmh.signal.disconnect()
        self.ports.signal.disconnect()

    def press_connect(self):
        self.connected = True
        self.buttonConnect.setDisabled(True)
        self.comPortBox.setDisabled(True)
        self.button_Disconnect.setHidden(False)
        self.buttonConnect.setDisabled(True)
        self.com.port = self.comPortBox.currentText()
        self.com.signal.connect(self.print_time_now)
        self.com.start()

    def press_button_disconnect(self):
        self.buttonConnect.setEnabled(True)
        self.comPortBox.setEnabled(True)
        self.button_Disconnect.setHidden(True)
        self.connected = False
        self.com.signal.disconnect()

    def press_sync_time(self):
        if self.connected:
            self.start_prin_time_now()
            self.com.write(f"t{''.join(str(x) for x in self.timeDisplay.toPlainText().split(':'))}")


    def press_button_led_1(self):
        if self.connected:
            self.com.write("l1;____")

    def press_button_led_2(self):
        if self.connected:
            self.com.write("l2;____")

    def press_button_led_3(self):
        if self.connected:
            self.com.write("l3;____")

    def press_button_led_4(self):
        if self.connected:
            self.com.write("l4;____")

    def press_button_led_off(self):
        if self.connected:
            self.com.write("l0;____")

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    myapp = Clock()
    myapp.show()
    sys.exit(app.exec_())
