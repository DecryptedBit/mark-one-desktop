import os
import sys

import PyQt5
from PyQt5 import QtCore
from PyQt5.QtCore import QSettings
from PyQt5.QtWidgets import QApplication

from src import widget_manager
from src.widgets.MainWindow import MainWindow
from src.handlers import settings_handler, command_handler, converter_handler


PyQt5.QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True)

widget_manager.settings = QSettings("DeBit", "MarkI-Desktop")

converter_handler.initialize()
command_handler.initialize()
settings_handler.initialize()

# Setup the UI
os.environ["QT_AUTO_SCREEN_SCALE_FACTOR"] = "1"
app = QApplication(sys.argv)

widget_manager.main_window = MainWindow()

widget_manager.main_window.show()
sys.exit(app.exec_())