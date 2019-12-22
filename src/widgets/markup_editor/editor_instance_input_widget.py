from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QTextEdit


class EditorInputInstanceWidget(QTextEdit):
    def __init__(self, parent=None):
        self.parent = parent
        super(EditorInputInstanceWidget, self).__init__(parent)
        self.init_ui()

    def init_ui(self):
        self.setStyleSheet("")
        self.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.setFrameShadow(QtWidgets.QFrame.Plain)
        self.setLineWidth(1)
        self.setObjectName("InstanceInputWidget")

        self.textChanged.connect(self.input_text_changed)

    def add_to_grid_layout(self, layout, row, column):
        layout.addWidget(self.markup_input_widget, row, column, 1, 1)

    def input_text_changed(self):
        self.parent.markup_input_text_changed(self.toPlainText())
