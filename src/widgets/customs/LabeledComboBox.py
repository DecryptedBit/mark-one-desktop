from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.QtWidgets import QWidget


class LabeledComboBox(QWidget):
    selectionChanged = QtCore.pyqtSignal()

    def __init__(self, label_text, parent=None):
        super(LabeledComboBox, self).__init__(parent)

        self.layout = QtWidgets.QHBoxLayout(self)
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.layout.setSpacing(6)
        self.setLayout(self.layout)

        self.label = QtWidgets.QLabel(self)
        self.label.setText(label_text + ": ")
        self.layout.addWidget(self.label)

        self.combo_box = QtWidgets.QComboBox(self)
        self.combo_box.setSizeAdjustPolicy(QtWidgets.QComboBox.AdjustToContents)
        self.combo_box.currentIndexChanged.connect(self.combo_box_selection_changed)
        self.layout.addWidget(self.combo_box)

    def combo_box_selection_changed(self):
        self.selectionChanged.emit()

    def add_item(self, item):
        self.combo_box.addItem(item)

    def add_items(self, items):
        self.combo_box.addItems(items)

    def clear_items(self):
        self.combo_box.clear()

    def set_item(self, item_name):
        index = self.combo_box.findText(item_name, QtCore.Qt.MatchFixedString)

        if index >= 0:
            self.combo_box.setCurrentIndex(index)

    def get_item(self):
        return self.combo_box.itemText(self.combo_box.currentIndex())

    def get_index(self):
        return self.combo_box.currentIndex()
