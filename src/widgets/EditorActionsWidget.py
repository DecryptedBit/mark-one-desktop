from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QWidget

from src.widgets.action_widgets import FlavorsActionWidget


class EditorActionsWidget(QWidget):
    converterSelectionChanged = QtCore.pyqtSignal(object, int, int)

    def __init__(self, parent=None):
        super(EditorActionsWidget, self).__init__(parent)

        self.layout = QtWidgets.QHBoxLayout(self)
        self.setLayout(self.layout)

        self.flavors_action_widget = FlavorsActionWidget.FlavorsActionWidget(self)
        self.flavors_action_widget.converterSelectionChanged.connect(self.converter_selection_changed)
        self.layout.addWidget(self.flavors_action_widget)

        self.layout.addStretch()

    def get_converter_selection(self):
        return self.flavors_action_widget.get_converter_selection()

    def converter_selection_changed(self, converter_name, from_type_index, to_type_index):
        self.converterSelectionChanged.emit(converter_name, from_type_index, to_type_index)
