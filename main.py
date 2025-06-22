# main.py (루트)
import sys, os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "src"))

from serial_gui.gui.serial_gui import SerialCommGUI
from PyQt5.QtWidgets import QApplication


def main():
    app = QApplication(sys.argv)
    gui = SerialCommGUI()
    gui.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
