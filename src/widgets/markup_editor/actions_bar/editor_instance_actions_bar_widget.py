from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QWidget

from src.widgets.markup_editor.actions_bar.flavors_action import FlavorsAction


class EditorInstanceActionsBarWidget(QWidget):
    converterSelectionChanged = QtCore.pyqtSignal(object, int, int)

    def __init__(self, parent=None):
        super(EditorInstanceActionsBarWidget, self).__init__(parent)
        self.init_ui()

    def init_ui(self):
        self.layout = QtWidgets.QHBoxLayout(self)

        self.flavors_action = FlavorsAction(self)
        self.flavors_action.converterSelectionChanged.connect(self.converter_selection_changed)
        self.layout.addWidget(self.flavors_action)

        self.layout.addStretch()

    def get_converter_selection(self):
        return self.flavors_action.get_converter_selection()

    def converter_selection_changed(self, converter_name, from_type_index, to_type_index):
        self.converterSelectionChanged.emit(converter_name, from_type_index, to_type_index)
