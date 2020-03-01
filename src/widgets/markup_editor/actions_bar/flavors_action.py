from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QWidget

from src.handlers import converter_handler
from src.widgets.components.labeled_combo_box import LabeledComboBox


class FlavorsAction(QWidget):
    converterSelectionChanged = QtCore.pyqtSignal(object, int, int)

    def __init__(self, parent=None):
        super(FlavorsAction, self).__init__(parent)
        self.init_ui()

    def init_ui(self):
        self.layout = QtWidgets.QHBoxLayout(self)
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.layout.setSpacing(30)

        self.using_combo_box = LabeledComboBox("Using", self)
        self.using_combo_box.selectionChanged.connect(
            lambda: self.master_selection_changed(self.using_combo_box.get_item()))
        self.layout.addWidget(self.using_combo_box)

        self.from_combo_box = LabeledComboBox("From", self)
        self.from_combo_box.selectionChanged.connect(self.selection_changed)
        self.layout.addWidget(self.from_combo_box)

        self.to_combo_box = LabeledComboBox("To", self)
        self.to_combo_box.selectionChanged.connect(self.selection_changed)
        self.layout.addWidget(self.to_combo_box)

        for converter_name in converter_handler.converter_dictionary:
            self.using_combo_box.add_item(converter_name)

    def master_selection_changed(self, *args):
        converter_class = converter_handler.get_converter(args[0])

        self.update_combo_box(self.from_combo_box, converter_class.get_from_types())
        self.update_combo_box(self.to_combo_box, converter_class.get_to_types())

        self.selection_changed()

    def selection_changed(self):
        self.converterSelectionChanged.emit(self.using_combo_box.get_item(),
                                            self.from_combo_box.get_index(),
                                            self.to_combo_box.get_index())

    def get_converter_selection(self):
        return self.using_combo_box.get_item(), self.from_combo_box.get_index(), self.to_combo_box.get_index()

    def update_combo_box(self, combo_box, items):
        combo_box.selectionChanged.disconnect(self.selection_changed)
        combo_box.clear_items()

        for item in items:
            combo_box.add_item(item[1])

        combo_box.selectionChanged.connect(self.selection_changed)
