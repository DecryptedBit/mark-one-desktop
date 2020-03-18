import os
import sys

import PyQt5
from PyQt5 import QtCore, Qt
from PyQt5.QtWidgets import QApplication
from src.widgets import MainWindow
from src.handlers import settings_handler, command_handler, converter_handler

PyQt5.QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True)


if __name__ == "__main__":
    # Setup the UI
    os.environ["QT_AUTO_SCREEN_SCALE_FACTOR"] = "1"
    app = QApplication(sys.argv)

    window = MainWindow.MainWindow()

    converter_handler.initialize()
    command_handler.initialize()
    settings_handler.initialize()

    window.show()
    sys.exit(app.exec_())
