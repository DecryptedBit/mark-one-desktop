from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QWidget


class PreferencesIndexWidget(QWidget):
    hierarchyItemActivated = QtCore.pyqtSignal(int)

    def __init__(self, parent=None):
        super(PreferencesIndexWidget, self).__init__(parent)

        self.layout = QtWidgets.QVBoxLayout(self)
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.layout.setSpacing(6)
        self.setLayout(self.layout)

        # Search
        self.search_layout = QtWidgets.QHBoxLayout(self)
        self.search_layout.setContentsMargins(6, 6, 6, 6)
        self.search_layout.setSpacing(6)
        self.layout.addLayout(self.search_layout)

        # Search line edit
        self.search_line_edit = QtWidgets.QLineEdit(self)
        self.search_line_edit_font = self.search_line_edit.font()
        self.search_line_edit_font.setPointSize(10)
        self.search_line_edit.setFont(self.search_line_edit_font)
        self.search_layout.addWidget(self.search_line_edit)

        # Hierarchy
        self.hierarchy_list_widget = QtWidgets.QListWidget(self)
        self.hierarchy_list_widget.setStyleSheet("border: none;")
        self.hierarchy_list_widget.currentItemChanged.connect(self.on_item_changed)
        self.layout.addWidget(self.hierarchy_list_widget)

    def on_item_changed(self, item):
        index = self.hierarchy_list_widget.indexFromItem(item).row()
        self.hierarchyItemActivated.emit(index)

    def add_item(self, name):
        new_option = QtWidgets.QListWidgetItem(name)
        new_option.setTextAlignment(QtCore.Qt.AlignHCenter)
        self.hierarchy_list_widget.addItem(new_option)

    def add_items(self, names):
        for name in names:
            self.add_item(name)

        self.hierarchy_list_widget.setCurrentRow(0)
