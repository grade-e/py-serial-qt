from PyQt5.QtWidgets import QComboBox
import serial.tools.list_ports


class PortComboBox(QComboBox):
    def showPopup(self):
        self.clear()
        ports = serial.tools.list_ports.comports()
        self.addItems([p.device for p in ports])
        super().showPopup()
