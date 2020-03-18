from PyQt5 import QtCore, QtGui, QtWidgets


class ButtonLineEdit(QtWidgets.QLineEdit):
    buttonClicked = QtCore.pyqtSignal(bool)

    def __init__(self, icon_path=None, parent=None):
        super(ButtonLineEdit, self).__init__(parent)

        if icon_path is None:
            icon = QtWidgets.QApplication.style().standardIcon(QtWidgets.QStyle.SP_DirIcon)
        else:
            icon = QtGui.QIcon(icon_path)

        self.action = self.addAction(icon, QtWidgets.QLineEdit.TrailingPosition)
        self.action.triggered.connect(self.buttonClicked.emit)
