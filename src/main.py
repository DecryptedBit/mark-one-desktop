import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from src import menu_actions_handler, file_handler, main_window
from src.interpreter import command_handler

main_window_obj = None


def initialize(main_window_inst):
    global main_window_obj
    main_window_obj = main_window_inst

    command_handler.initialize()
    menu_actions_handler.initialize(main_window_obj)
    file_handler.initialize(main_window_obj)


def quit_application():
    file_handler.quit()


def test(main_window2):
    main_window2.test()


if __name__ == "__main__":
    # Setup the UI
    app = QApplication(sys.argv)
    app.aboutToQuit.connect(quit_application)
    # app.setStyle("Fusion")

    window = main_window.MainWindow()

    initialize(window)

    window.show()
    sys.exit(app.exec_())
