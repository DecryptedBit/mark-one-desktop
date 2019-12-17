import mistune
from PyQt5 import QtWidgets


class MarkupEditorInstanceInputUI(object):
    def setup_ui(self, parent_widget):
        self.markup_input_widget = QtWidgets.QTextEdit(parent_widget)
        self.markup_input_widget.setStyleSheet("")
        self.markup_input_widget.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.markup_input_widget.setFrameShadow(QtWidgets.QFrame.Plain)
        self.markup_input_widget.setLineWidth(1)
        self.markup_input_widget.setObjectName("InstanceInputWidget")

        markdown = mistune.Markdown()
        self.markup_input_widget.append(markdown(
            '# I am using the mistune markdown parser \n\n ## Cool stuff! \n\n **Lets see if this works**'))

    def add_to_grid_layout(self, layout, row, column):
        layout.addWidget(self.markup_input_widget, row, column, 1, 1)