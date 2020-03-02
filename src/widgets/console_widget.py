from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QWidget
from enum import Enum
from src import config
from src.handlers import file_handler, command_handler
from src.widgets.console_line_edit import ConsoleLineEdit


class TraverseDirType(Enum):
    UP = "up"
    DOWN = "down"


class LoggingType(Enum):
    INPUT = "input"
    RESPONSE = "response"


def logging_add(text, logging_type):
    if logging_type is LoggingType.INPUT and config.CONSOLE_LOGGING is False:
        return
    elif logging_type is LoggingType.RESPONSE and config.CONSOLE_RESPONSE_LOGGING is False:
        return

    file_handler.append_file(config.CONSOLE_LOG_FILE_PATH, text)


class ConsoleWidget(QWidget):
    command_history = []
    history_index = 0

    def __init__(self, parent=None):
        super(ConsoleWidget, self).__init__(parent)

        self.layout = QtWidgets.QVBoxLayout(self)
        self.layout.setContentsMargins(3, 3, 3, 3)
        self.layout.setSpacing(3)
        self.setLayout(self.layout)

        # Output text edit
        self.output_edit = QtWidgets.QTextEdit(self)
        self.output_edit.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.output_edit.setReadOnly(True)
        self.layout.addWidget(self.output_edit)

        # Interaction area layout
        self.interaction_layout = QtWidgets.QHBoxLayout()
        self.interaction_layout.setSpacing(3)
        self.layout.addLayout(self.interaction_layout)

        # Input line edit
        self.input_edit = ConsoleLineEdit(self)
        self.input_edit.setFrame(False)
        self.input_edit.returnPressed.connect(self.send_command)
        self.input_edit.traverseUpPressed.connect(lambda: self.history_traverse(TraverseDirType.UP))
        self.input_edit.traverseDownPressed.connect(lambda: self.history_traverse(TraverseDirType.DOWN))
        self.interaction_layout.addWidget(self.input_edit)

        # Input send button
        self.send_button = QtWidgets.QPushButton(self)
        self.send_button.setText("Send")
        self.send_button.clicked.connect(self.send_command)
        self.interaction_layout.addWidget(self.send_button)

    def send_command(self):
        input = self.input_edit.text()

        if not input:
            return

        self.history_add(input)
        logging_add(input, LoggingType.INPUT)

        self.input_edit.clear()
        self.output_edit.append(config.CONSOLE_PREFIX + input)

        response = command_handler.manufacture(input)

        if response != "":
            self.output_edit.append(response + "\n")
            logging_add(response + "\n", LoggingType.RESPONSE)

    def history_add(self, command):
        self.command_history.append(command)

        if len(self.command_history) > config.CONSOLE_HISTORY_LEN:
            self.command_history.pop(0)

        self.history_index = len(self.command_history)

        print(f'Console history: {self.command_history}')

    def history_traverse(self, traverse_dir):
        if self.command_history:
            if traverse_dir == TraverseDirType.UP and self.history_index > 0:
                self.history_index -= 1
            elif traverse_dir == TraverseDirType.DOWN and self.history_index < len(self.command_history):
                self.history_index += 1

            if self.history_index < len(self.command_history):
                self.input_edit.setText(self.command_history[self.history_index])
            elif self.history_index == len(self.command_history):
                self.input_edit.clear()
