"""
SerialCommGUI
-------------

A PyQt5-based GUI tool for serial communication using hexadecimal packets.
- Send and receive packets in hex (space-separated)
- Display TX (blue) and RX (green) logs
- Auto-corrects input formats
"""

__version__ = "0.1.0"
__author__ = "Jinwoo Sung"
__all__ = ["serial_gui"]

from .main import main
from serial_gui import SerialCommGUI
