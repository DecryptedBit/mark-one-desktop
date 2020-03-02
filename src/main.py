import os
import sys

from PyQt5 import QtCore
from PyQt5.QtWidgets import QApplication
from src import main_window
from src.handlers import file_handler, settings_handler, command_handler, converter_handler


def initialize():
    converter_handler.initialize()
    command_handler.initialize()
    file_handler.initialize()
    settings_handler.initialize()


if __name__ == "__main__":
    # Setup the UI
    os.environ["QT_AUTO_SCREEN_SCALE_FACTOR"] = "1"
    app = QApplication(sys.argv)
    app.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling)
    # app.setStyle("Fusion")

    window = main_window.MainWindow()

    initialize()

    window.show()
    sys.exit(app.exec_())
