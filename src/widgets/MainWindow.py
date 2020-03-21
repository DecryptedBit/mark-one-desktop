from PyQt5 import QtCore, QtWidgets
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QMainWindow

from src import config, widget_manager
from src.widgets import ConsoleWidget, FileExplorerTreeView, MenuBar, EditorTabWidget


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)

        self.resize(config.UI_RESOLUTION[0], config.UI_RESOLUTION[1])
        self.setWindowTitle('Mark-one ALPHA')
        self.setWindowIcon(QIcon('resources/logo.svg'))
        self.setAutoFillBackground(False)

        # File explorer
        self.file_explorer_dock_widget = QtWidgets.QDockWidget(self)
        self.file_explorer_dock_widget.setFeatures(QtWidgets.QDockWidget.AllDockWidgetFeatures)

        self.file_explorer_tree_view = FileExplorerTreeView.FileExplorerTreeView(self)
        self.file_explorer_dock_widget.setWindowTitle("File explorer")
        self.file_explorer_dock_widget.setWidget(self.file_explorer_tree_view)
        self.addDockWidget(QtCore.Qt.DockWidgetArea(1), self.file_explorer_dock_widget)
        widget_manager.file_explorer_tree_view = self.file_explorer_tree_view

        # Markup editor
        self.editor_tab_widget = EditorTabWidget.EditorTabWidget(self)
        widget_manager.editor_tab_widget = self.editor_tab_widget

        # Console
        self.console_dock_widget = QtWidgets.QDockWidget(self)
        self.console_dock_widget.setWindowTitle("Console")
        self.console_dock_widget.setFeatures(QtWidgets.QDockWidget.AllDockWidgetFeatures)

        self.console_widget = ConsoleWidget.ConsoleWidget(self)
        self.console_dock_widget.setWidget(self.console_widget)
        self.addDockWidget(QtCore.Qt.DockWidgetArea(8), self.console_dock_widget)
        widget_manager.console_widget = self.console_widget

        # Menu bar
        self.menu_bar = MenuBar.MenuBar(self)
        self.setMenuBar(self.menu_bar)

        # Finalization
        self.setCentralWidget(self.editor_tab_widget)

    def on_close_request(self, event):
        result = self.editor_tab_widget.close_files()

        if result is self.editor_tab_widget.CloseReplyType.CANCELLED:
            event.ignore()
        else:
            event.accept()

    def closeEvent(self, event):
        self.on_close_request(event)
