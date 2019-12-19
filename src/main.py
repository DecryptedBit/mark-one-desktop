import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from src import main_ui
from src.interpreter import command_handler

if __name__ == "__main__":
    # Initialize the command handler
    command_handler.initialize()

    app = QApplication(sys.argv)
    # app.setStyle("Fusion")
    window = main_ui.MainWindow()
    window.show()
    sys.exit(app.exec_())
