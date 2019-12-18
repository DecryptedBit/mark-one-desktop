from PyQt5 import QtWidgets


class MarkupEditorInstanceInputUI(object):
    def setup_ui(self, instantiator):
        self.instantiator = instantiator

        self.markup_input_widget = QtWidgets.QTextEdit()
        self.markup_input_widget.setStyleSheet("")
        self.markup_input_widget.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.markup_input_widget.setFrameShadow(QtWidgets.QFrame.Plain)
        self.markup_input_widget.setLineWidth(1)
        self.markup_input_widget.setObjectName("InstanceInputWidget")

        self.markup_input_widget.textChanged.connect(self.input_text_changed)

    def add_to_grid_layout(self, layout, row, column):
        layout.addWidget(self.markup_input_widget, row, column, 1, 1)

    def input_text_changed(self):
        self.instantiator.markup_input_text_changed(self.markup_input_widget.toPlainText())

    def get_widget(self):
        return self.markup_input_widget
