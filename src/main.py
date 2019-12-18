import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from src import main_ui
from src.widgets import TerminalWidget
from src.interpreter import command_handler

if __name__ == "__main__":
    # Initialize the command handler
    command_handler.initialize()

    # Setup the UI
    app = QApplication(sys.argv)
    # app.setStyle("Fusion")

    window = QMainWindow()

    main_ui = main_ui.MainWindowUI()
    main_ui.setup_ui(window)

    terminal_widget = TerminalWidget.Ui_terminalWidget()
    terminal_widget.setupUi(main_ui.terminal_dock_layout)

    window.show()
    sys.exit(app.exec_())
