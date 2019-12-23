from PyQt5.QtWidgets import QFileDialog

from src import config

main_window = None
open_files = {}
#active_file = None


def initialize(main_window_inst):
    global main_window
    main_window = main_window_inst


def create_file():
    file_id = main_window.markup_editor_widget.create_instance()

    open_files_add(file_id)
    #active_file_switch(file_id)


def save_file_as():
    file_name = QFileDialog.getSaveFileName(main_window, 'Save file as', config.DEFAULT_SAVE_DIR, '*.txt')
    file_content = main_window.markup_editor_widget.currentWidget().markup_input_widget.toPlainText()

    file = open(file_name[0], 'w')
    file.write(file_content)
    file.close()


def open_files_add(id, file_path=None):
    global open_files

    open_files[id] = file_path
    print(open_files)


'''
def active_file_switch(id):
    global active_file

    if open_files:
        active_file = open_files[id]'''


'''
def close_file(key):
    # Close a single file
    if open_files:
        removed_file = open_files.pop(key)
        removed_file.close()'''


def quit():
    # Close all open files to prevent corruption
    if open_files:
        for file in open_files.values():
            if file is not None:
                file.close()
