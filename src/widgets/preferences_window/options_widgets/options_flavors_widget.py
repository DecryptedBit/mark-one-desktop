from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QWidget

from src.widgets.preferences_window.options_widgets.option_entries.input_entry_widget import InputEntryWidget


class OptionsFlavorsWidget(QWidget):
    def __init__(self, settings, parent=None):
        super(OptionsFlavorsWidget, self).__init__(parent)
        self.settings = settings
        self.init_ui()

    def init_ui(self):
        self.layout = QtWidgets.QVBoxLayout(self)
        self.layout.setContentsMargins(18, 18, 18, 18)
        self.layout.setSpacing(9)

        # Entries
        self.pandoc_path_input_entry = InputEntryWidget("Pandoc path", "resources/logo_inverted.png", self)
        self.pandoc_path_input_entry.set_text(self.settings.value("flavors/pandoc_path", "", type=str))
        self.pandoc_path_input_entry.buttonClicked.connect(self.instantiate_folder_dialog)
        self.layout.addWidget(self.pandoc_path_input_entry)

        self.layout.addStretch()

    def instantiate_folder_dialog(self):
        file_dialog_response = QtWidgets.QFileDialog.getExistingDirectory(self, "Select Pandoc Directory")

        if file_dialog_response != '':
            self.pandoc_path_input_entry.set_text(file_dialog_response)

    def save_settings(self):
        self.settings.setValue("flavors/pandoc_path", self.pandoc_path_input_entry.get_text())
