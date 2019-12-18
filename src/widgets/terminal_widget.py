from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QLineEdit
from enum import Enum
from src import config
from src.interpreter import command_handler


class TraverseDir(Enum):
    UP = "up"
    DOWN = "down"


class Terminal(object):
    command_history = []
    history_index = 0

    def setup_ui(self, main_window):
        # Dock widget
        self.dock_widget = QtWidgets.QDockWidget(main_window)
        self.dock_widget.setFeatures(QtWidgets.QDockWidget.AllDockWidgetFeatures)
        self.dock_widget.setObjectName("TerminalDockWidget")

        # Terminal widget
        self.terminal_widget = QtWidgets.QWidget()
        self.terminal_widget.setObjectName("TerminalWidget")
        self.dock_widget.setWidget(self.terminal_widget)

        # Terminal widget layout
        self.terminal_layout = QtWidgets.QVBoxLayout(self.terminal_widget)
        self.terminal_layout.setContentsMargins(3, 3, 3, 3)
        self.terminal_layout.setSpacing(3)
        self.terminal_layout.setObjectName("TerminalLayout")

        # Terminal widget output text edit
        self.terminal_output_edit = QtWidgets.QTextEdit(self.terminal_widget)
        self.terminal_output_edit.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.terminal_output_edit.setReadOnly(True)
        self.terminal_output_edit.setObjectName("TerminalOutputEdit")
        self.terminal_layout.addWidget(self.terminal_output_edit)

        # Terminal widget interaction area layout
        self.terminal_interaction_layout = QtWidgets.QHBoxLayout()
        self.terminal_interaction_layout.setSpacing(4)
        self.terminal_interaction_layout.setObjectName("TerminalInteractionLayout")
        self.terminal_layout.addLayout(self.terminal_interaction_layout)

        # Interaction area input line edit
        self.terminal_input_edit = TerminalLineEdit(self.terminal_widget, self)
        self.terminal_input_edit.setFrame(False)
        self.terminal_input_edit.setObjectName("TerminalInputEdit")
        self.terminal_interaction_layout.addWidget(self.terminal_input_edit)

        # Interaction area input send button
        self.terminal_send_button = QtWidgets.QPushButton(self.terminal_widget)
        self.terminal_send_button.setObjectName("TerminalSendButton")
        self.terminal_interaction_layout.addWidget(self.terminal_send_button)

        # Finalization
        self.retranslate_ui()
        self.terminal_send_button.clicked.connect(self.send_command)
        self.terminal_input_edit.returnPressed.connect(self.send_command)

        main_window.addDockWidget(QtCore.Qt.DockWidgetArea(8), self.dock_widget)

        QtCore.QMetaObject.connectSlotsByName(self.terminal_widget)

    def retranslate_ui(self):
        _translate = QtCore.QCoreApplication.translate
        self.dock_widget.setWindowTitle(_translate("MainWindow", "Terminal"))

    def retranslate_ui(self):
        _translate = QtCore.QCoreApplication.translate
        self.dock_widget.setWindowTitle(_translate("TerminalWidget", "Terminal"))
        self.terminal_send_button.setText(_translate("TerminalWidget", "Send"))

    def send_command(self):
        input = self.terminal_input_edit.text()

        if not input:
            return

        self.history_add(input)

        output = command_handler.manufacture(input)

        self.terminal_input_edit.clear()
        self.terminal_output_edit.append(config.TERMINAL_PREFIX + input)
        self.terminal_output_edit.append(output)

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
                self.terminal_input_edit.setText(self.command_history[self.history_index])
            elif self.history_index == len(self.command_history):
                self.terminal_input_edit.clear()


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
