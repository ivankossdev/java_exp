import datetime
import serial
import PyQt5
from PyQt5.QtCore import QThread
from PyQt5.QtWidgets import QMainWindow

class TimeHandler(QThread):
    signal = PyQt5.QtCore.pyqtSignal(str)

    def __init__(self, parent=QMainWindow):
        super(TimeHandler, self).__init__(parent)

    def run(self):
        while True:
            self.tm = datetime.datetime.now()
            self.S0 = int(self.tm.second % 10)
            self.S1 = int(self.tm.second / 10)
            self.M0 = int(self.tm.minute % 10)
            self.M1 = int(self.tm.minute / 10)
            self.H0 = int(self.tm.hour % 10)
            self.H1 = int(self.tm.hour / 10)
            self.signal.emit(f'{self.H1}{self.H0}:{self.M1}{self.M0}:{self.S1}{self.S0}')
            QThread.sleep(1)


class STM_Board_Ports(QThread):
    signal = PyQt5.QtCore.pyqtSignal(list)

    def __init__(self, parent=QMainWindow):
        super(STM_Board_Ports, self).__init__(parent)
        self.com_ports = []

    def run(self):
        while True:
            for port in [f"COM{x + 1}" for x in range(0, 256)]:
                try:
                    s = serial.Serial(port)
                    s.close()
                    self.com_ports.append(port)
                except (OSError, serial.SerialException):
                    pass
            if len(self.com_ports) > 0:
                self.signal.emit(self.com_ports)
                break
            QThread.sleep(1)


class STM_Read_Port(QThread):
    signal = PyQt5.QtCore.pyqtSignal(str)

    def __init__(self, parent=QMainWindow):
        super(STM_Read_Port, self).__init__(parent)
        self._open_port = None
        self.port = None

    def run(self):
        self._open_port = serial.Serial(self.port)
        while True:
            self.signal.emit(self._open_port.read(8).decode())
            QThread.sleep(1)

    def close_port(self):
        self._open_port.close()

