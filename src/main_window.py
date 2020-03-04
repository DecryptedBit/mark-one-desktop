from PyQt5 import QtCore, QtWidgets
from PyQt5.QtCore import QSettings
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QMainWindow

from src import config, widget_manager
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
        widget_manager.main_window = self

        # File explorer
        self.file_explorer_dock_widget = QtWidgets.QDockWidget(self)
        self.file_explorer_dock_widget.setFeatures(QtWidgets.QDockWidget.AllDockWidgetFeatures)

        self.file_explorer_widget = file_explorer_widget.FileExplorer(self)
        self.file_explorer_dock_widget.setWindowTitle("File explorer")
        self.file_explorer_dock_widget.setWidget(self.file_explorer_widget)
        self.addDockWidget(QtCore.Qt.DockWidgetArea(1), self.file_explorer_dock_widget)
        widget_manager.file_explorer_widget = self.file_explorer_widget

        # Markup editor
        self.markup_editor_widget = markup_editor_widget.MarkupEditorWidget(self)
        widget_manager.markup_editor_widget = self.markup_editor_widget

        # Console
        self.console_dock_widget = QtWidgets.QDockWidget(self)
        self.console_dock_widget.setWindowTitle("Console")
        self.console_dock_widget.setFeatures(QtWidgets.QDockWidget.AllDockWidgetFeatures)

        self.console_widget = console_widget.ConsoleWidget(self)
        self.console_dock_widget.setWidget(self.console_widget)
        self.addDockWidget(QtCore.Qt.DockWidgetArea(8), self.console_dock_widget)
        widget_manager.console_widget = self.console_widget

        # Menu bar
        self.menu_bar_widget = menu_bar_widget.MenuBarWidget(self)
        self.setMenuBar(self.menu_bar_widget)

        # Finalization
        self.setCentralWidget(self.markup_editor_widget)

    def on_close_request(self, event):
        result = self.markup_editor_widget.close_files()

        if result is self.markup_editor_widget.CloseReplyType.CANCELLED:
            event.ignore()
        else:
            event.accept()

    def closeEvent(self, event):
        self.on_close_request(event)
