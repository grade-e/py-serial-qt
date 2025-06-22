from PyQt5.QtWidgets import QApplication
from serial_gui import SerialCommGUI
import sys

if __name__ == "__main__":
    app = QApplication(sys.argv)
    gui = SerialCommGUI()
    gui.show()
    sys.exit(app.exec_())
