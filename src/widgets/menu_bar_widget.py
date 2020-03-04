from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QMenuBar

from src import widget_manager
from src.widgets.preferences_window.preferences_window_widget import PreferencesWindowWidget


class MenuBarWidget(QMenuBar):
    def __init__(self, parent=None):
        super(MenuBarWidget, self).__init__(parent)

        self.setGeometry(QtCore.QRect(0, 0, 1057, 21))
        self.setDefaultUp(False)
        self.setNativeMenuBar(True)
        self.setObjectName("MenuBar")

        # File item
        self.file_item = QtWidgets.QMenu(self)
        self.file_item.setTitle("File")

        self.new_action = QtWidgets.QAction(self)
        self.new_action.setText("New")
        self.new_action.setShortcut("Ctrl+N")
        self.new_action.triggered.connect(widget_manager.markup_editor_widget.create_new_file)

        self.open_action = QtWidgets.QAction(self)
        self.open_action.setText("Open")
        self.open_action.setShortcut("Ctrl+O")
        self.open_action.triggered.connect(widget_manager.markup_editor_widget.open_file)

        self.save_action = QtWidgets.QAction(self)
        self.save_action.setText("Save")
        self.save_action.setShortcut("Ctrl+S")
        self.save_action.triggered.connect(widget_manager.markup_editor_widget.save_file)

        self.save_as_action = QtWidgets.QAction(self)
        self.save_as_action.setText("Save as")
        self.save_as_action.triggered.connect(widget_manager.markup_editor_widget.save_file_as)

        self.file_item.addAction(self.new_action)
        self.file_item.addAction(self.open_action)
        self.file_item.addSeparator()
        self.file_item.addAction(self.save_action)
        self.file_item.addAction(self.save_as_action)

        # Edit item
        self.edit_item = QtWidgets.QMenu(self)
        self.edit_item.setTitle("Edit")

        # Format item
        self.format_item = QtWidgets.QMenu(self)
        self.format_item.setTitle("Format")

        # View item
        self.view_item = QtWidgets.QMenu(self)
        self.view_item.setTitle("View")
        self.view_item.setLayoutDirection(QtCore.Qt.RightToLeft)

        # Settings item
        self.settings_item = QtWidgets.QMenu(self)
        self.settings_item.setTitle("Settings")

        self.preferences_action = QtWidgets.QAction(self)
        self.preferences_action.setText("Preferences")
        self.preferences_action.triggered.connect(lambda: PreferencesWindowWidget(widget_manager.main_window).exec())

        self.theme_action = QtWidgets.QAction(self)
        self.theme_action.setText("Theme")

        self.stylesheet_action = QtWidgets.QAction(self)
        self.stylesheet_action.setText("Stylesheet")

        self.settings_item.addAction(self.preferences_action)
        self.settings_item.addAction(self.theme_action)
        self.settings_item.addAction(self.stylesheet_action)

        # Finalization
        self.addAction(self.file_item.menuAction())
        self.addAction(self.edit_item.menuAction())
        self.addAction(self.format_item.menuAction())
        self.addAction(self.view_item.menuAction())
        self.addAction(self.settings_item.menuAction())
