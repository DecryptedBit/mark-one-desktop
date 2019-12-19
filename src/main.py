import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from src import main_ui, menu_actions_handler, file_handler
from src.interpreter import command_handler

main_window = None


def initialize(main_window_inst):
    global main_window
    main_window = main_window_inst

    command_handler.initialize()
    menu_actions_handler.initialize(main_window)
    file_handler.initialize(main_window)


def quit_application():
    file_handler.quit()

def test(main_window2):
    main_window2.test()


if __name__ == "__main__":
    # Setup the UI
    app = QApplication(sys.argv)
    app.aboutToQuit.connect(quit_application)
    # app.setStyle("Fusion")

    window = QMainWindow()

    main_window = main_ui.MainWindowUI()
    main_window.setup_ui(window)

    initialize(main_window)

    window.show()
    sys.exit(app.exec_())
