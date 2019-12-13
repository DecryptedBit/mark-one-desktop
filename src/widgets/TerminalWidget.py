from PyQt5 import QtCore, QtWidgets
from src import constants
from src.interpreter import command_handler


class Ui_terminalWidget(object):
    def setupUi(self, terminalWidget):
        terminalWidget.setObjectName("terminalWidget")
        terminalWidget.resize(620, 326)
        self.verticalLayout = QtWidgets.QVBoxLayout(terminalWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
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
        self.terminalInputEdit = QtWidgets.QLineEdit(terminalWidget)
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
        output = command_handler.manufacture(input)

        self.terminalInputEdit.clear()
        self.terminalOutputEdit.append(constants.TERMINAL_PREFIX + input)
        self.terminalOutputEdit.append(output)
