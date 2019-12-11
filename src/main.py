import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from src import main_ui
from src.widgets import TerminalWidget


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.ui = Ui_MainWindow()

        self.ui.setupUi(self)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyle("Fusion")

    window = QMainWindow()

    main_ui = main_ui.Ui_MainWindow()
    main_ui.setupUi(window)

    terminal_widget = TerminalWidget.Ui_Form()
    terminal_widget.setupUi(main_ui.terminalDockLayout)

    window.show()
    sys.exit(app.exec_())
