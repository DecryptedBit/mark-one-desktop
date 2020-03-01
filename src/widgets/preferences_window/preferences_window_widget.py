from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QDialog

from src.widgets.preferences_window.options_widgets.options_flavors_widget import OptionsFlavorsWidget
from src.widgets.preferences_window.preferences_index_widget import PreferencesIndexWidget
from src.widgets.preferences_window.preferences_options_widget import PreferencesOptionsWidget


def on_open(main_window):
    settings = main_window.settings
    preference_dialog = PreferencesWindowWidget(settings, main_window)
    preference_dialog.exec()


class PreferencesWindowWidget(QDialog):
    def __init__(self, settings, parent=None):
        super(PreferencesWindowWidget, self).__init__(parent)
        self.settings = settings
        self.init_ui()

    def init_ui(self):
        self.setObjectName("PreferencesWindowWidget")

        self.layout = QtWidgets.QVBoxLayout(self)
        self.layout.setContentsMargins(0, 0, 0, 9)
        self.layout.setSpacing(9)

        self.option_widgets = [OptionsFlavorsWidget(self.settings, self)]
        self.option_widgets_names = ["Flavors"]

        # Index
        self.index_widget = PreferencesIndexWidget(self)
        self.index_widget.add_items(self.option_widgets_names)
        self.index_widget.hierarchyItemActivated.connect(self.hierarchy_item_activated)

        # Options
        self.options_widget = PreferencesOptionsWidget(self)
        self.options_widget.add_option_widgets(self.option_widgets, self.option_widgets_names)

        # Splitter
        self.splitter = QtWidgets.QSplitter(self)
        self.splitter.addWidget(self.index_widget)
        self.splitter.addWidget(self.options_widget)
        self.splitter.setHandleWidth(6)
        self.layout.addWidget(self.splitter)

        # Actions box
        self.actions_button_box = QtWidgets.QDialogButtonBox(self)
        self.actions_button_box.setCenterButtons(True)
        self.layout.addWidget(self.actions_button_box)

        # Actions box buttons
        button_ok = self.actions_button_box.addButton(QtWidgets.QDialogButtonBox.Ok)
        button_ok.clicked.connect(self.accept)

        button_cancel = self.actions_button_box.addButton(QtWidgets.QDialogButtonBox.Cancel)
        button_cancel.clicked.connect(self.reject)

        button_apply = self.actions_button_box.addButton(QtWidgets.QDialogButtonBox.Apply)
        button_apply.clicked.connect(self.save_settings)

        QtCore.QMetaObject.connectSlotsByName(self)

    def hierarchy_item_activated(self, index):
        self.options_widget.setCurrentIndex(index)

    def save_settings(self):
        for option_widget in self.option_widgets:
            option_widget.save_settings()

        self.settings.sync()
        print("Settings are saved")
