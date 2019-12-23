from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QLineEdit, QWidget
from enum import Enum
from src import config
from src.interpreter import command_handler


class TraverseDir(Enum):
    UP = "up"
    DOWN = "down"


class TerminalWidget(QWidget):
    command_history = []
    history_index = 0

    def __init__(self, parent=None):
        super(TerminalWidget, self).__init__(parent)
        self.init_ui()

    def init_ui(self):
        self.setObjectName("TerminalWidget")

        # Terminal widget layout
        self.layout = QtWidgets.QVBoxLayout(self)
        self.layout.setContentsMargins(3, 3, 3, 3)
        self.layout.setSpacing(3)
        self.layout.setObjectName("TerminalLayout")

        # Terminal widget output text edit
        self.output_edit = QtWidgets.QTextEdit(self)
        self.output_edit.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.output_edit.setReadOnly(True)
        self.output_edit.setObjectName("TerminalOutputEdit")
        self.layout.addWidget(self.output_edit)

        # Terminal widget interaction area layout
        self.interaction_layout = QtWidgets.QHBoxLayout()
        self.interaction_layout.setSpacing(3)
        self.interaction_layout.setObjectName("TerminalInteractionLayout")
        self.layout.addLayout(self.interaction_layout)

        # Interaction area input line edit
        self.input_edit = TerminalLineEdit(self)
        self.input_edit.setFrame(False)
        self.input_edit.setObjectName("TerminalInputEdit")
        self.input_edit.returnPressed.connect(self.send_command)
        self.interaction_layout.addWidget(self.input_edit)

        # Interaction area input send button
        self.send_button = QtWidgets.QPushButton(self)
        self.send_button.setObjectName("TerminalSendButton")
        self.interaction_layout.addWidget(self.send_button)

        # Finalization
        self.retranslate_ui()
        self.send_button.clicked.connect(self.send_command)

        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslate_ui(self):
        _translate = QtCore.QCoreApplication.translate
        self.send_button.setText(_translate("TerminalWidget", "Send"))

    def send_command(self):
        input = self.input_edit.text()

        if not input:
            return

        self.history_add(input)

        output = command_handler.manufacture(input)

        self.input_edit.clear()
        self.output_edit.append(config.TERMINAL_PREFIX + input)
        self.output_edit.append(output)

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
                self.input_edit.setText(self.command_history[self.history_index])
            elif self.history_index == len(self.command_history):
                self.input_edit.clear()


class TerminalLineEdit(QLineEdit):
    def __init__(self, parent=None):
        super(TerminalLineEdit, self).__init__(parent)
        self.parent = parent

    def keyPressEvent(self, event):
        key = event.key()

        if key > 0 and key == QtCore.Qt.Key_Up:
            self.parent.history_traverse(TraverseDir.UP) # history_traverse(TraverseDir.UP)
        if key > 0 and key == QtCore.Qt.Key_Down:
            self.parent.history_traverse(TraverseDir.DOWN)

        super(TerminalLineEdit, self).keyPressEvent(event)
