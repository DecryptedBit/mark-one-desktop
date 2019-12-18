from PyQt5 import QtCore, QtWidgets


class MenuBar(object):
    def setup_ui(self, main_window):
        # Menu bar widget
        self.menu_bar_widget = QtWidgets.QMenuBar()
        self.menu_bar_widget.setGeometry(QtCore.QRect(0, 0, 1057, 21))
        self.menu_bar_widget.setDefaultUp(False)
        self.menu_bar_widget.setNativeMenuBar(True)
        self.menu_bar_widget.setObjectName("MenuBar")

        # File item
        self.file_item = QtWidgets.QMenu(self.menu_bar_widget)
        self.file_item.setObjectName("MenuBarFileMenu")

        self.save_action = QtWidgets.QAction(main_window)
        self.save_action.setObjectName("FileMenuSaveAction")
        self.save_as_action = QtWidgets.QAction(main_window)
        self.save_as_action.setObjectName("FileMenurSaveAsAction")

        self.file_item.addAction(self.save_action)
        self.file_item.addAction(self.save_as_action)
        self.file_item.addSeparator()

        # Edit item
        self.edit_item = QtWidgets.QMenu(self.menu_bar_widget)
        self.edit_item.setObjectName("MenuBarEditMenu")

        # Format item
        self.format_item = QtWidgets.QMenu(self.menu_bar_widget)
        self.format_item.setObjectName("MenuBarFormatMenu")

        # View item
        self.view_item = QtWidgets.QMenu(self.menu_bar_widget)
        self.view_item.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.view_item.setObjectName("MenuBarViewMenu")

        # Settings item
        self.settings_item = QtWidgets.QMenu(self.menu_bar_widget)
        self.settings_item.setObjectName("MenuBarSettingsMenu")

        self.preferences_action = QtWidgets.QAction(main_window)
        self.preferences_action.setObjectName("SettingsMenuPreferencesAction")
        self.theme_action = QtWidgets.QAction(main_window)
        self.theme_action.setObjectName("SettingsMenuThemeAction")
        self.stylesheet_action = QtWidgets.QAction(main_window)
        self.stylesheet_action.setObjectName("SettingsMenuStylesheetAction")

        self.settings_item.addAction(self.preferences_action)
        self.settings_item.addAction(self.theme_action)
        self.settings_item.addAction(self.stylesheet_action)

        # Finalization
        self.menu_bar_widget.addAction(self.file_item.menuAction())
        self.menu_bar_widget.addAction(self.edit_item.menuAction())
        self.menu_bar_widget.addAction(self.format_item.menuAction())
        self.menu_bar_widget.addAction(self.view_item.menuAction())
        self.menu_bar_widget.addAction(self.settings_item.menuAction())

        main_window.setMenuBar(self.menu_bar_widget)

    def retranslate_ui(self):
        _translate = QtCore.QCoreApplication.translate

        # Items
        self.file_item.setTitle(_translate("MainWindow", "File"))
        self.edit_item.setTitle(_translate("MainWindow", "Edit"))
        self.format_item.setTitle(_translate("MainWindow", "Format"))
        self.view_item.setTitle(_translate("MainWindow", "View"))
        self.settings_item.setTitle(_translate("MainWindow", "Settings"))

        # Item actions
        self.save_action.setText(_translate("MainWindow", "Save"))
        self.save_as_action.setText(_translate("MainWindow", "Save As"))
        
        self.preferences_action.setText(_translate("MainWindow", "Preferences"))
        self.theme_action.setText(_translate("MainWindow", "Theme"))
        self.stylesheet_action.setText(_translate("MainWindow", "Stylesheet"))
