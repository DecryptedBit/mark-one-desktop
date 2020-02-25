from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QDialog

from src.widgets.preferences_window.options_widgets.options_flavors_widget import OptionsFlavorWidget
from src.widgets.preferences_window.options_widgets.options_general_widget import OptionsGeneralWidget
from src.widgets.preferences_window.preferences_index_widget import PreferencesIndexWidget
from src.widgets.preferences_window.preferences_options_widget import PreferencesOptionsWidget


def on_open(main_window):
    settings = main_window.settings

    preference_dialog = PreferencesWindowWidget(main_window)

    # On execution, set changes to settings object
    if preference_dialog.exec():
        pass

    # Write settings to storage
    del settings


class PreferencesWindowWidget(QDialog):
    def __init__(self, parent=None):
        super(PreferencesWindowWidget, self).__init__(parent)
        self.init_ui()

    def init_ui(self):
        self.setObjectName("PreferencesWindowWidget")

        self.layout = QtWidgets.QVBoxLayout(self)
        self.layout.setContentsMargins(0, 0, 0, 9)
        self.layout.setSpacing(9)

        self.option_widgets = [QtWidgets.QWidget(self), OptionsFlavorWidget(self), QtWidgets.QWidget(self)]
        self.option_widgets_names = ["General", "Flavors", "Terminal"]

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
        self.actions_button_box.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel | QtWidgets.QDialogButtonBox.Apply)
        self.actions_button_box.setCenterButtons(True)
        self.actions_button_box.setObjectName("PreferencesWindowButtonBox")

        self.actions_button_box.accepted.connect(self.accept)
        self.actions_button_box.rejected.connect(self.reject)

        self.layout.addWidget(self.actions_button_box)

        QtCore.QMetaObject.connectSlotsByName(self)

    def hierarchy_item_activated(self, index):
        self.options_widget.setCurrentIndex(index)
