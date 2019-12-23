from PyQt5.QtWidgets import QTextEdit, QFrame


class EditorInputInstanceWidget(QTextEdit):
    def __init__(self, parent=None):
        super(EditorInputInstanceWidget, self).__init__(parent)
        self.parent = parent
        self.init_ui()

    def init_ui(self):
        self.setStyleSheet("")
        self.setFrameShape(QFrame.NoFrame)
        self.setFrameShadow(QFrame.Plain)
        self.setLineWidth(1)
        self.setObjectName("InstanceInputWidget")

        self.textChanged.connect(self.input_text_changed)

    def input_text_changed(self):
        self.parent.markup_input_text_changed(self.toPlainText())
