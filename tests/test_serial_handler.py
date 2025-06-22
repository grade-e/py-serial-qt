import pytest
from serial_gui.core.serial_handler import SerialHandler


class DummySerial:
    def __init__(self):
        self.is_open = False
        self.buffer = b""

    def open(self):
        self.is_open = True

    def close(self):
        self.is_open = False

    def write(self, data):
        self.buffer += data

    def read_all(self):
        data, self.buffer = self.buffer, b""
        return data

    @property
    def in_waiting(self):
        return len(self.buffer)


@pytest.fixture(autouse=True)
def patch_serial(monkeypatch):
    dummy = DummySerial()
    monkeypatch.setattr("serial_gui.core.serial_handler.serial.Serial", lambda: dummy)
    return dummy


def test_open_close(patch_serial):
    sh = SerialHandler()
    assert not sh.is_open()
    sh.open("COM1", 9600)
    assert sh.is_open()
    sh.close()
    assert not sh.is_open()


def test_send_and_read(patch_serial):
    sh = SerialHandler()
    sh.open("COM1", 9600)
    sh.send_bytes(b"\x01\x02")
    assert patch_serial.buffer == b"\x01\x02"
    out = sh.read_bytes()
    assert out == b"\x01\x02"
