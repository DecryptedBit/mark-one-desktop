from PyQt5 import QtCore, QtWidgets
from PyQt5.QtCore import QSettings
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QMainWindow

from src import config, file_handler
from src.widgets import terminal_widget, file_explorer_widget, menu_bar_widget
from src.widgets.markup_editor import markup_editor_widget


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)

        self.settings = QSettings("DeBit", "MarkI-Desktop")
        print(self.settings.fileName())

        self.init_ui()

    def init_ui(self):
        self.resize(config.UI_RESOLUTION[0], config.UI_RESOLUTION[1])
        self.setWindowTitle('Markup Project ALPHA')
        self.setWindowIcon(QIcon('resources/logo.svg'))

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
