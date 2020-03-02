from PyQt5 import QtCore, QtWidgets
from PyQt5.QtCore import QSettings
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QMainWindow

from src import config
from src.handlers import file_handler
from src.widgets import console_widget, file_explorer_widget, menu_bar_widget
from src.widgets.markup_editor import markup_editor_widget


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)

        self.settings = QSettings("DeBit", "MarkI-Desktop")

        self.resize(config.UI_RESOLUTION[0], config.UI_RESOLUTION[1])
        self.setWindowTitle('MarkI ALPHA')
        self.setWindowIcon(QIcon('resources/logo.svg'))
        self.setAutoFillBackground(False)

        self.layout = QtWidgets.QGridLayout(self)
        self.setLayout(self.layout)

        # Menu bar
        self.menu_bar_widget = menu_bar_widget.MenuBarWidget(self)
        self.setMenuBar(self.menu_bar_widget)

        # File explorer
        self.file_explorer_dock_widget = QtWidgets.QDockWidget(self)
        self.file_explorer_dock_widget.setFeatures(QtWidgets.QDockWidget.AllDockWidgetFeatures)

        self.file_explorer_widget = file_explorer_widget.FileExplorer(self)
        self.file_explorer_dock_widget.setWindowTitle("File explorer")
        self.file_explorer_dock_widget.setWidget(self.file_explorer_widget)
        self.addDockWidget(QtCore.Qt.DockWidgetArea(1), self.file_explorer_dock_widget)

        # Markup editor
        self.markup_editor_widget = markup_editor_widget.MarkupEditorWidget(self)

        # Console
        self.console_dock_widget = QtWidgets.QDockWidget(self)
        self.console_dock_widget.setWindowTitle("Console")
        self.console_dock_widget.setFeatures(QtWidgets.QDockWidget.AllDockWidgetFeatures)

        self.console_widget = console_widget.ConsoleWidget(self)
        self.console_dock_widget.setWidget(self.console_widget)
        self.addDockWidget(QtCore.Qt.DockWidgetArea(8), self.console_dock_widget)

        # Finalization
        self.setCentralWidget(self.markup_editor_widget)

    def handle_file_closing(self, event):
        open_editor_tab_count = self.markup_editor_widget.count()
        forced_close_option = None

        # Loop through every open instance and request to close it
        for i in reversed(range(open_editor_tab_count)):
            option_chosen = file_handler.close_file(i, True, forced_close_option)

            if option_chosen is not None:
                forced_close_option = option_chosen

            if option_chosen is file_handler.CloseFileReplyType.CANCEL:
                event.ignore()
                return

        event.accept()

    def closeEvent(self, event):
        self.handle_file_closing(event)
