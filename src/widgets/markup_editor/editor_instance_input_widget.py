from PyQt5 import QtCore
from PyQt5.QtWidgets import QTextEdit, QFrame


class EditorInputInstanceWidget(QTextEdit):
    contentChanged = QtCore.pyqtSignal(str)

    def __init__(self, parent=None):
        super(EditorInputInstanceWidget, self).__init__(parent)
        self.init_ui()

    def init_ui(self):
        self.setStyleSheet("")
        self.setFrameShape(QFrame.NoFrame)
        self.setFrameShadow(QFrame.Plain)
        self.setLineWidth(1)

        self.textChanged.connect(lambda: self.contentChanged.emit(self.toPlainText()))
