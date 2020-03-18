from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QWidget

from src import widget_manager
from src.widgets.customs.LabeledLineEdit import LabeledLineEdit


class FlavorsOptionsWidget(QWidget):
    def __init__(self, parent=None):
        super(FlavorsOptionsWidget, self).__init__(parent)
        self.settings = widget_manager.main_window.settings

        self.layout = QtWidgets.QVBoxLayout(self)
        self.layout.setContentsMargins(18, 18, 18, 18)
        self.layout.setSpacing(9)
        self.setLayout(self.layout)

        # Inputs
        self.pandoc_path_line_edit = LabeledLineEdit("Pandoc path", parent=self)
        self.pandoc_path_line_edit.set_text(self.settings.value("flavors/pandoc_path", "", type=str))
        self.pandoc_path_line_edit.buttonClicked.connect(self.instantiate_folder_dialog)
        self.layout.addWidget(self.pandoc_path_line_edit)

        self.layout.addStretch()

    def instantiate_folder_dialog(self):
        file_dialog_response = QtWidgets.QFileDialog.getExistingDirectory(self, "Select Pandoc Directory")

        if file_dialog_response != '':
            self.pandoc_path_line_edit.set_text(file_dialog_response)

    def save_settings(self):
        self.settings.setValue("flavors/pandoc_path", self.pandoc_path_line_edit.get_text())
