from PyQt5 import QtCore, QtWidgets

from src import config
from src.widgets import MarkupEditor, MarkupEditorInstancePreview


class MainWindowUI(object):
    def setup_ui(self, main_window):
        main_window.setObjectName("MainWindow")
        main_window.resize(config.UI_RESOLUTION[0], config.UI_RESOLUTION[1])
        main_window.setAutoFillBackground(False)

        # Main window layout
        self.main_window_layout = QtWidgets.QWidget(main_window)
        self.main_window_layout.setObjectName("MainWindowLayout")
        main_window.setCentralWidget(self.main_window_layout)

        # Menu bar and items
        self.menu_bar_widget = QtWidgets.QMenuBar(main_window)
        self.menu_bar_widget.setGeometry(QtCore.QRect(0, 0, 1057, 21))
        self.menu_bar_widget.setDefaultUp(False)
        self.menu_bar_widget.setNativeMenuBar(True)
        self.menu_bar_widget.setObjectName("MenuBar")

        # Menu bar and items: File item
        self.menu_bar_file_item = QtWidgets.QMenu(self.menu_bar_widget)
        self.menu_bar_file_item.setObjectName("MenuBarFileMenu")

        self.file_item_save_action = QtWidgets.QAction(main_window)
        self.file_item_save_action.setObjectName("FileMenuSaveAction")
        self.file_item_save_as_action = QtWidgets.QAction(main_window)
        self.file_item_save_as_action.setObjectName("FileMenurSaveAsAction")

        self.menu_bar_file_item.addAction(self.file_item_save_action)
        self.menu_bar_file_item.addAction(self.file_item_save_as_action)
        self.menu_bar_file_item.addSeparator()

        # Menu bar and items: Edit item
        self.menu_bar_edit_item = QtWidgets.QMenu(self.menu_bar_widget)
        self.menu_bar_edit_item.setObjectName("MenuBarEditMenu")

        # Menu bar and items: Format item
        self.menu_bar_format_item = QtWidgets.QMenu(self.menu_bar_widget)
        self.menu_bar_format_item.setObjectName("MenuBarFormatMenu")

        # Menu bar and items: View item
        self.menu_bar_view_item = QtWidgets.QMenu(self.menu_bar_widget)
        self.menu_bar_view_item.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.menu_bar_view_item.setObjectName("MenuBarViewMenu")

        # Menu bar and items: Settings item
        self.menu_bar_settings_item = QtWidgets.QMenu(self.menu_bar_widget)
        self.menu_bar_settings_item.setObjectName("MenuBarSettingsMenu")

        self.settings_item_preferences_action = QtWidgets.QAction(main_window)
        self.settings_item_preferences_action.setObjectName("SettingsMenuPreferencesAction")
        self.settings_item_theme_action = QtWidgets.QAction(main_window)
        self.settings_item_theme_action.setObjectName("SettingsMenuThemeAction")
        self.settings_item_stylesheet_action = QtWidgets.QAction(main_window)
        self.settings_item_stylesheet_action.setObjectName("SettingsMenuStylesheetAction")

        self.menu_bar_settings_item.addAction(self.settings_item_preferences_action)
        self.menu_bar_settings_item.addAction(self.settings_item_theme_action)
        self.menu_bar_settings_item.addAction(self.settings_item_stylesheet_action)

        # Menu bar and items: Finalization
        self.menu_bar_widget.addAction(self.menu_bar_file_item.menuAction())
        self.menu_bar_widget.addAction(self.menu_bar_edit_item.menuAction())
        self.menu_bar_widget.addAction(self.menu_bar_format_item.menuAction())
        self.menu_bar_widget.addAction(self.menu_bar_view_item.menuAction())
        self.menu_bar_widget.addAction(self.menu_bar_settings_item.menuAction())

        main_window.setMenuBar(self.menu_bar_widget)

        # File explorer
        self.file_explorer_dock_widget = QtWidgets.QDockWidget(main_window)
        self.file_explorer_dock_widget.setFeatures(QtWidgets.QDockWidget.AllDockWidgetFeatures)
        self.file_explorer_dock_widget.setObjectName("FileExplorerDockWidget")

        self.file_explorer_dock_layout = QtWidgets.QWidget()
        self.file_explorer_dock_layout.setObjectName("FileExplorerDockLayout")

        self.file_explorer_tree_view_widget = QtWidgets.QTreeView(self.file_explorer_dock_layout)
        self.file_explorer_tree_view_widget.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.file_explorer_tree_view_widget.setObjectName("FileExplorerTreeView")
        self.file_explorer_tree_view_widget.header().setVisible(True)

        self.file_explorer_tree_view_layout = QtWidgets.QGridLayout(self.file_explorer_dock_layout)
        self.file_explorer_tree_view_layout.setContentsMargins(3, 3, 3, 3)
        self.file_explorer_tree_view_layout.setObjectName("ileExplorerTreeLayout")
        self.file_explorer_tree_view_layout.addWidget(self.file_explorer_tree_view_widget, 0, 0, 1, 1)

        self.file_explorer_dock_widget.setWidget(self.file_explorer_dock_layout)
        main_window.addDockWidget(QtCore.Qt.DockWidgetArea(1), self.file_explorer_dock_widget)

        # Markup editor (the previewer is built in the editor)
        self.markup_editor_widget = MarkupEditor.MarkupEditorUI()
        self.markup_editor_widget.setup_ui(main_window)

        # Terminal
        self.terminal_dock_widget = QtWidgets.QDockWidget(main_window)
        self.terminal_dock_widget.setFeatures(QtWidgets.QDockWidget.AllDockWidgetFeatures)
        self.terminal_dock_widget.setObjectName("TerminalDockWidget")
        self.terminal_dock_layout = QtWidgets.QWidget()
        self.terminal_dock_layout.setObjectName("TerminalDockLayout")
        self.terminal_dock_widget.setWidget(self.terminal_dock_layout)
        main_window.addDockWidget(QtCore.Qt.DockWidgetArea(8), self.terminal_dock_widget)

        # Finalization
        self.retranslate_ui(main_window)
        QtCore.QMetaObject.connectSlotsByName(main_window)

    def retranslate_ui(self, main_window):
        _translate = QtCore.QCoreApplication.translate
        main_window.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.menu_bar_file_item.setTitle(_translate("MainWindow", "File"))
        self.menu_bar_edit_item.setTitle(_translate("MainWindow", "Edit"))
        self.menu_bar_format_item.setTitle(_translate("MainWindow", "Format"))
        self.menu_bar_view_item.setTitle(_translate("MainWindow", "View"))
        self.menu_bar_settings_item.setTitle(_translate("MainWindow", "Settings"))
        self.file_explorer_dock_widget.setWindowTitle(_translate("MainWindow", "File explorer"))
        self.terminal_dock_widget.setWindowTitle(_translate("MainWindow", "Terminal"))
        self.file_item_save_action.setText(_translate("MainWindow", "Save"))
        self.file_item_save_as_action.setText(_translate("MainWindow", "Save As"))
        self.settings_item_preferences_action.setText(_translate("MainWindow", "Preferences"))
        self.settings_item_theme_action.setText(_translate("MainWindow", "Theme"))
        self.settings_item_stylesheet_action.setText(_translate("MainWindow", "Stylesheet"))

        self.markup_editor_widget.retranslate_ui()
