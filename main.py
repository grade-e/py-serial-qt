# main.py (루트)
from serial_gui.gui.serial_gui import SerialCommGUI
from PyQt5.QtWidgets import QApplication
import sys


def main():
    app = QApplication(sys.argv)
    gui = SerialCommGUI()
    gui.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
