from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QWidget

from src.widgets.preferences_window.options_widgets.option_entries.input_entry_widget import InputEntryWidget


class OptionsFlavorWidget(QWidget):
    def __init__(self, parent=None):
        super(OptionsFlavorWidget, self).__init__(parent)
        self.init_ui()

    def init_ui(self):
        self.layout = QtWidgets.QVBoxLayout(self)
        self.layout.setContentsMargins(18, 18, 18, 18)
        self.layout.setSpacing(9)

        # Entries
        self.pandoc_path_input_entry = InputEntryWidget("Pandoc path", "resources/logo_inverted.png", self)
        self.pandoc_path_input_entry.buttonClicked.connect(lambda e: print("works"))
        self.layout.addWidget(self.pandoc_path_input_entry)

        self.layout.addStretch()
