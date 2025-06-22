from PyQt5.QtWidgets import *
from PyQt5.QtGui import QTextCharFormat, QTextCursor, QColor
from PyQt5.QtCore import QTimer
from core.serial_handler import SerialHandler

import re


def format_hex_string(data: bytes) -> str:
    return " ".join(f"{b:02X}" for b in data)


class SerialCommGUI(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Serial Packet Monitor")
        self.setMinimumSize(600, 400)

        self.serial = SerialHandler()
        self.timer = QTimer()
        self.timer.timeout.connect(self.read_data)

        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()

        port_layout = QHBoxLayout()
        self.port_combo = QComboBox()
        self.port_combo.addItems(self.serial.list_ports())
        self.baud_input = QLineEdit("115200")
        self.open_btn = QPushButton("Open")
        self.open_btn.clicked.connect(self.toggle_serial)

        port_layout.addWidget(QLabel("Port:"))
        port_layout.addWidget(self.port_combo)
        port_layout.addWidget(QLabel("Baud:"))
        port_layout.addWidget(self.baud_input)
        port_layout.addWidget(self.open_btn)

        self.log = QTextEdit()
        self.log.setReadOnly(True)

        input_layout = QHBoxLayout()
        self.input_line = QLineEdit()
        self.send_btn = QPushButton("Send")
        self.send_btn.clicked.connect(self.send_data)

        input_layout.addWidget(self.input_line)
        input_layout.addWidget(self.send_btn)

        layout.addLayout(port_layout)
        layout.addWidget(self.log)
        layout.addLayout(input_layout)
        self.setLayout(layout)

    def toggle_serial(self):
        if self.serial.is_open():
            self.serial.close()
            self.timer.stop()
            self.open_btn.setText("Open")
            self.log_append("Disconnected.", "gray")
        else:
            try:
                port = self.port_combo.currentText()
                baud = int(self.baud_input.text())
                self.serial.open(port, baud)
                self.timer.start(100)
                self.open_btn.setText("Close")
                self.log_append("Connected.", "gray")
            except Exception as e:
                self.log_append(f"Error: {e}", "red")

    def send_data(self):
        try:
            raw_input = self.input_line.text().strip()
            cleaned = re.sub(r"[^0-9a-fA-FxX]", " ", raw_input)
            cleaned = cleaned.replace("0x", "").replace("0X", "")
            parts = cleaned.strip().split()
            valid_hex = [
                p.zfill(2).upper()
                for p in parts
                if re.fullmatch(r"[0-9a-fA-F]{1,2}", p)
            ]
            if not valid_hex:
                self.log_append("[TX] No valid hex to send.", "orange")
                return
            bytes_data = bytes(int(b, 16) for b in valid_hex)
            self.serial.send_bytes(bytes_data)
            self.log_append(f"[TX] {' '.join(valid_hex)}", "blue")
        except Exception as e:
            self.log_append(f"Send error: {e}", "red")

    def read_data(self):
        try:
            data = self.serial.read_bytes()
            if data:
                self.log_append(f"[RX] {format_hex_string(data)}", "green")
        except Exception as e:
            self.log_append(f"Read error: {e}", "red")

    def log_append(self, message, color):
        cursor = self.log.textCursor()
        fmt = QTextCharFormat()
        fmt.setForeground(QColor(color))
        cursor.movePosition(QTextCursor.End)
        cursor.insertText(message + "\n", fmt)
        self.log.setTextCursor(cursor)
        self.log.ensureCursorVisible()
