from PyQt5 import QtCore, QtWidgets
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QMainWindow, QMessageBox

from src import config, file_handler
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
        self.layout = QtWidgets.QGridLayout(self)
        self.layout.setObjectName("MainWindowLayout")
        self.setLayout(self.layout)

        # Menu bar
        self.menu_bar_widget = menu_bar_widget.MenuBarWidget(self)
        self.setMenuBar(self.menu_bar_widget)

        # File explorer
        self.file_explorer_dock_widget = QtWidgets.QDockWidget(self)
        self.file_explorer_dock_widget.setFeatures(QtWidgets.QDockWidget.AllDockWidgetFeatures)
        self.file_explorer_dock_widget.setObjectName("FileExplorerDockWidget")

        self.file_explorer_widget = file_explorer_widget.FileExplorer(self)
        self.file_explorer_dock_widget.setWidget(self.file_explorer_widget)
        self.addDockWidget(QtCore.Qt.DockWidgetArea(1), self.file_explorer_dock_widget)

        # Markup editor
        self.markup_editor_widget = markup_editor_widget.MarkupEditorWidget(self)

        # Terminal
        self.terminal_dock_widget = QtWidgets.QDockWidget(self)
        self.terminal_dock_widget.setFeatures(QtWidgets.QDockWidget.AllDockWidgetFeatures)
        self.terminal_dock_widget.setObjectName("TerminalDockWidget")

        self.terminal_widget = terminal_widget.TerminalWidget(self)
        self.terminal_dock_widget.setWidget(self.terminal_widget)
        self.addDockWidget(QtCore.Qt.DockWidgetArea(8), self.terminal_dock_widget)

        # Finalization
        self.setCentralWidget(self.markup_editor_widget)
        self.retranslate_ui()
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslate_ui(self):
        _translate = QtCore.QCoreApplication.translate

        self.file_explorer_dock_widget.setWindowTitle(_translate("MainWindow", "File explorer"))
        self.terminal_dock_widget.setWindowTitle(_translate("MainWindow", "Terminal"))

        self.menu_bar_widget.retranslate_ui()
        self.markup_editor_widget.retranslate_ui()
        self.file_explorer_widget.retranslate_ui()
        self.terminal_widget.retranslate_ui()

    def closeEvent(self, event):
        reply = file_handler.handle_application_close_event()

        if reply is True:
            event.accept()
        else:
            event.ignore()
