from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QLineEdit
from enum import Enum
from src import config
from src.interpreter import command_handler


class TraverseDir(Enum):
    UP = "up"
    DOWN = "down"


class Ui_terminalWidget(object):
    command_history = []
    history_index = 0

    def setupUi(self, terminalWidget):
        terminalWidget.setObjectName("terminalWidget")
        terminalWidget.resize(620, 326)

        self.verticalLayout = QtWidgets.QVBoxLayout(terminalWidget)
        self.verticalLayout.setContentsMargins(3, 3, 3, 3)
        self.verticalLayout.setSpacing(4)
        self.verticalLayout.setObjectName("verticalLayout")

        self.terminalOutputEdit = QtWidgets.QTextEdit(terminalWidget)
        self.terminalOutputEdit.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.terminalOutputEdit.setReadOnly(True)
        self.terminalOutputEdit.setObjectName("terminalOutputEdit")
        self.verticalLayout.addWidget(self.terminalOutputEdit)

        self.terminalLayout = QtWidgets.QHBoxLayout()
        self.terminalLayout.setSpacing(4)
        self.terminalLayout.setObjectName("terminalLayout")

        self.terminalInputEdit = TerminalLineEdit(terminalWidget, self)
        self.terminalInputEdit.setFrame(False)
        self.terminalInputEdit.setObjectName("terminalInputEdit")
        self.terminalLayout.addWidget(self.terminalInputEdit)

        self.terminalSendButton = QtWidgets.QPushButton(terminalWidget)
        self.terminalSendButton.setObjectName("terminalSendButton")
        self.terminalLayout.addWidget(self.terminalSendButton)

        self.verticalLayout.addLayout(self.terminalLayout)

        self.retranslateUi(terminalWidget)
        self.terminalSendButton.clicked.connect(self.send_command)
        self.terminalInputEdit.returnPressed.connect(self.send_command)

        QtCore.QMetaObject.connectSlotsByName(terminalWidget)

    def retranslateUi(self, terminalWidget):
        _translate = QtCore.QCoreApplication.translate
        terminalWidget.setWindowTitle(_translate("terminalWidget", "Form"))
        self.terminalSendButton.setText(_translate("terminalWidget", "PushButton"))

    def send_command(self):
        input = self.terminalInputEdit.text()

        if not input:
            return

        self.history_add(input)

        output = command_handler.manufacture(input)

        self.terminalInputEdit.clear()
        self.terminalOutputEdit.append(config.TERMINAL_PREFIX + input)
        self.terminalOutputEdit.append(output)

    def history_add(self, command):
        self.command_history.append(command)

        if len(self.command_history) > config.TERMINAL_HISTORY_LEN:
            self.command_history.pop(0)

        self.history_index = len(self.command_history)

        print(self.command_history)

    def history_traverse(self, traverse_dir):
        if self.command_history:
            if traverse_dir == TraverseDir.UP and self.history_index > 0:
                self.history_index -= 1
            elif traverse_dir == TraverseDir.DOWN and self.history_index < len(self.command_history):
                self.history_index += 1

            print(self.history_index)

            if self.history_index < len(self.command_history):
                self.terminalInputEdit.setText(self.command_history[self.history_index])
            elif self.history_index == len(self.command_history):
                self.terminalInputEdit.clear()


class TerminalLineEdit(QLineEdit):
    def __init__(self, parent, terminal_widget):
        super(TerminalLineEdit, self).__init__(parent)
        self.terminal_widget = terminal_widget

    def keyPressEvent(self, event):
        key = event.key()

        if key > 0 and key == QtCore.Qt.Key_Up:
            self.terminal_widget.history_traverse(TraverseDir.UP) # history_traverse(TraverseDir.UP)
        if key > 0 and key == QtCore.Qt.Key_Down:
            self.terminal_widget.history_traverse(TraverseDir.DOWN)

        super(TerminalLineEdit, self).keyPressEvent(event)
