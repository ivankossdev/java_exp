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
            tm = datetime.datetime.now()
            S0 = int(tm.second % 10)
            S1 = int(tm.second / 10)
            M0 = int(tm.minute % 10)
            M1 = int(tm.minute / 10)
            H0 = int(tm.hour % 10)
            H1 = int(tm.hour / 10)
            self.signal.emit(f'{H1}{H0}:{M1}{M0}:{S1}{S0}')
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
            self.signal.emit(self._open_port.read(7).decode())
            self._open_port.reset_input_buffer()

    def write(self, message):
        self._open_port.write(message.encode())

    def close_port(self):
        self.signal.disconnect()
        self._open_port.close()
