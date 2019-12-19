import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from src import main_window
from src.interpreter import command_handler

if __name__ == "__main__":
    # Initialize the command handler
    command_handler.initialize()

    app = QApplication(sys.argv)
    # app.setStyle("Fusion")
    window = main_window.MainWindow()
    window.show()
    sys.exit(app.exec_())
