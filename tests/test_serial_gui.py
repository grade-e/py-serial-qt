import pytest
from PyQt5.QtCore import Qt
from serial_gui.gui.serial_gui import SerialCommGUI, format_hex_string


@pytest.fixture
def gui(qtbot, monkeypatch):
    class Dummy:
        def __init__(self):
            self.opened = False
            self.sent = b""
            self.to_read = b""

        def list_ports(self):
            return ["COM1"]

        def open(self, port, baud):
            self.opened = True

        def close(self):
            self.opened = False

        def is_open(self):
            return self.opened

        def send_bytes(self, data):
            self.sent = data

        def read_bytes(self):
            out, self.to_read = self.to_read, b""
            return out

    dummy = Dummy()
    monkeypatch.setattr("serial_gui.gui.serial_gui.SerialHandler", lambda: dummy)
    w = SerialCommGUI()
    qtbot.addWidget(w)
    return w, dummy


def test_format_hex_string():
    assert format_hex_string(b"\x0a\xff\x10") == "0A FF 10"


def test_send_invalid_input(gui, qtbot):
    w, _ = gui
    w.input_line.setText("GG ZZ")
    qtbot.mouseClick(w.send_btn, Qt.LeftButton)
    assert "[TX] No valid hex to send." in w.log.toPlainText()


def test_send_valid_input(gui, qtbot):
    w, dummy = gui
    w.input_line.setText("0x1 aF")
    qtbot.mouseClick(w.send_btn, Qt.LeftButton)
    assert dummy.sent == b"\x01\xaf"
    assert "[TX] 01 AF" in w.log.toPlainText()


def test_receive_shows_in_log(gui, qtbot):
    w, dummy = gui
    qtbot.mouseClick(w.open_btn, Qt.LeftButton)
    dummy.to_read = b"\xab\xcd"
    w.read_data()
    assert "[RX] AB CD" in w.log.toPlainText()
