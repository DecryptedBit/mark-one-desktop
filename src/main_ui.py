from PyQt5 import QtCore, QtWidgets

from src import config
from src.widgets import terminal_widget, file_explorer_widget, menu_bar_widget
from src.widgets.markup_editor import markup_editor_widget


class MainWindowUI(object):
    def setup_ui(self, main_window):
        main_window.setObjectName("MainWindow")
        main_window.resize(config.UI_RESOLUTION[0], config.UI_RESOLUTION[1])
        main_window.setAutoFillBackground(False)

        # Main window layout
        self.main_window_layout = QtWidgets.QWidget(main_window)
        self.main_window_layout.setObjectName("MainWindowLayout")
        main_window.setCentralWidget(self.main_window_layout)

        # Menu bar
        self.menu_bar_widget = menu_bar_widget.MenuBar()
        self.menu_bar_widget.setup_ui(main_window)

        # File explorer
        self.file_explorer_widget = file_explorer_widget.FileExplorer()
        self.file_explorer_widget.setup_ui(main_window)

        # Markup editor
        self.markup_editor_widget = markup_editor_widget.MarkupEditor()
        self.markup_editor_widget.setup_ui(main_window)

        # Terminal
        self.terminal_widget = terminal_widget.Terminal()
        self.terminal_widget.setup_ui(main_window)

        # Finalization
        self.retranslate_ui(main_window)
        QtCore.QMetaObject.connectSlotsByName(main_window)

    def retranslate_ui(self, main_window):
        _translate = QtCore.QCoreApplication.translate
        main_window.setWindowTitle(_translate("MainWindow", "MainWindow"))

        self.menu_bar_widget.retranslate_ui()
        self.file_explorer_widget.retranslate_ui()
        self.markup_editor_widget.retranslate_ui()
        self.terminal_widget.retranslate_ui()
