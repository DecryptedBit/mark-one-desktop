from src import file_handler

current_file = None
main_window = None


def initialize(main_window_inst):
    global main_window
    main_window = main_window_inst


def new_action_triggered():
    file_handler.create_file()


def save_as_action_triggered():
    file_handler.save_file_as()
