import sys
from PyQt5.QtWidgets import QApplication
from src import main_window
from src.handlers import file_handler, settings_handler, command_handler, converter_handler

main_window_obj = None


def initialize(main_window_inst):
    global main_window_obj
    main_window_obj = main_window_inst

    converter_handler.initialize()
    command_handler.initialize(main_window_obj)
    file_handler.initialize(main_window_obj)
    settings_handler.read_settings(main_window_obj.settings)


if __name__ == "__main__":
    # Setup the UI
    app = QApplication(sys.argv)
    # app.setStyle("Fusion")

    window = main_window.MainWindow()

    initialize(window)

    window.show()
    sys.exit(app.exec_())
