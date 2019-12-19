from PyQt5 import QtCore, QtWidgets
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QMainWindow

from src import config
from src.widgets import terminal_widget, file_explorer_widget, menu_bar_widget
from src.widgets.markup_editor import markup_editor_widget


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)

        self.init_ui()

    def init_ui(self):
        self.resize(config.UI_RESOLUTION[0], config.UI_RESOLUTION[1])
        self.setWindowTitle('Markup Project ALPHA')
        self.setWindowIcon(QIcon('logo.svg'))

        self.setObjectName("MainWindow")
        self.setAutoFillBackground(False)

        # Main window layout
        self.main_window_layout = QtWidgets.QWidget(self)
        self.main_window_layout.setObjectName("MainWindowLayout")
        self.setCentralWidget(self.main_window_layout)

        # Menu bar
        self.menu_bar_widget = menu_bar_widget.MenuBar()
        self.menu_bar_widget.setup_ui(self)

        # File explorer
        self.file_explorer_widget = file_explorer_widget.FileExplorer()
        self.file_explorer_widget.setup_ui(self)

        # Markup editor
        self.markup_editor_widget = markup_editor_widget.MarkupEditor()
        self.markup_editor_widget.setup_ui(self)

        # Terminal
        self.terminal_widget = terminal_widget.Terminal()
        self.terminal_widget.setup_ui(self)

        # Finalization
        self.retranslate_ui()
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslate_ui(self):
        _translate = QtCore.QCoreApplication.translate

        self.menu_bar_widget.retranslate_ui()
        self.file_explorer_widget.retranslate_ui()
        self.markup_editor_widget.retranslate_ui()
        self.terminal_widget.retranslate_ui()
