from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QTreeView


class FileExplorer(QTreeView):
    def __init__(self, parent=None):
        super(FileExplorer, self).__init__(parent)
        self.init_ui()

    def init_ui(self):
        self.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.setObjectName("FileExplorerTreeView")
        self.header().setVisible(True)

        # Tree layout
        self.layout = QtWidgets.QGridLayout(self)
        self.layout.setContentsMargins(3, 3, 3, 3)
        self.layout.setObjectName("FileExplorerTreeLayout")
        self.layout.addWidget(self, 0, 0, 1, 1)

        # Finalization
        self.retranslate_ui()

        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslate_ui(self):
        _translate = QtCore.QCoreApplication.translate
