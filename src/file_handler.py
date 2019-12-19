main_window = None
open_files = {}
active_file = None


def initialize(main_window_inst):
    global main_window
    main_window = main_window_inst


def create_file():
    file_id = main_window.markup_editor_widget.create_instance()
    print(file_id)

    open_files[file_id] = None


'''
def switch_active_file(index):
    global active_file

    if open_files:
        active_file = open_files[index]


def close_file(key):
    # Close a single file
    if open_files:
        removed_file = open_files.pop(key)
        removed_file.close()
'''


def quit():
    # Close all open files to prevent corruption
    if open_files:
        for file in open_files.values():
            if file is not None:
                file.close()
