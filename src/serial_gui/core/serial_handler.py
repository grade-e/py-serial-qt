import serial
import serial.tools.list_ports


class SerialHandler:
    def __init__(self):
        self.ser = serial.Serial()

    def list_ports(self):
        return [p.device for p in serial.tools.list_ports.comports()]

    def open(self, port, baudrate):
        self.ser.port = port
        self.ser.baudrate = baudrate
        self.ser.open()

    def close(self):
        if self.ser.is_open:
            self.ser.close()

    def is_open(self):
        return self.ser.is_open

    def send_bytes(self, data: bytes):
        self.ser.write(data)

    def read_bytes(self) -> bytes:
        return self.ser.read_all() if self.ser.in_waiting else b""

    def in_waiting(self) -> int:
        return self.ser.in_waiting
