from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QTreeView


class FileExplorer(QTreeView):
    def __init__(self, parent=None):
        super(FileExplorer, self).__init__(parent)

        self.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.header().setVisible(True)

        self.layout = QtWidgets.QGridLayout(self)
        self.layout.setContentsMargins(3, 3, 3, 3)
        self.layout.addWidget(self, 0, 0, 1, 1)
        self.setLayout(self.layout)
