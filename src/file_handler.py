import os
from pprint import pprint

from PyQt5.QtWidgets import QFileDialog

from src import config

main_window = None
open_files = {}


def initialize(main_window_inst):
    global main_window
    main_window = main_window_inst


def create_file():
    file_id = main_window.markup_editor_widget.create_instance()

    open_files_add(file_id)


def open_file():
    file_info = QFileDialog.getOpenFileName(main_window, 'Open file', config.DEFAULT_SAVE_DIR, '*.txt')

    file_type = file_info[1]
    file_path = file_info[0]
    file_name = os.path.basename(file_path)

    file_content = read_file(file_path)

    if not main_window.markup_editor_widget.currentWidget().markup_input_widget.toPlainText():
        # If the current editor instance is empty, get the current widget id and update the file
        file_id = main_window.markup_editor_widget.currentWidget().__hash__()
        open_files_update(file_id, (file_name, file_path, file_type))
    else:
        # If the current editor instance is filled, create a new widget and add the file
        file_id = main_window.markup_editor_widget.create_instance()
        open_files_add(file_id, (file_name, file_path, file_type))

    main_window.markup_editor_widget.currentWidget().markup_input_widget.setText(file_content)
    main_window.markup_editor_widget.setTabText(main_window.markup_editor_widget.currentIndex(), file_name)


def save_file():
    file_id = main_window.markup_editor_widget.currentWidget().__hash__()
    file_content = main_window.markup_editor_widget.currentWidget().markup_input_widget.toPlainText()

    if open_files[file_id] is not None:
        file_path = open_files[file_id][0]
        pprint(file_path)
        write_file(file_path, file_content)
    else:
        save_file_as(file_id)


def save_file_as(file_id=None, file_content=None):
    if file_id is None:
        file_id = main_window.markup_editor_widget.currentWidget().__hash__()

    if file_content is None:
        file_content = main_window.markup_editor_widget.currentWidget().markup_input_widget.toPlainText()

    file_info = QFileDialog.getSaveFileName(main_window, 'Save file as', config.DEFAULT_SAVE_DIR, '*.txt')
    file_path = file_info[0]
    file_type = file_info[1]

    file_name = os.path.basename(file_path)
    main_window.markup_editor_widget.setTabText(main_window.markup_editor_widget.currentIndex(), file_name)

    open_files_update(file_id, (file_name, file_path, file_type))
    write_file(file_path, file_content)


def open_files_add(id, file_info=None):
    global open_files

    open_files[id] = file_info
    pprint(open_files)


def open_files_update(id, file_info):
    global open_files

    if id in open_files:
        open_files[id] = file_info

    pprint(open_files)


'''
def close_file(key):
    # Close a single file
    if open_files:
        removed_file = open_files.pop(key)
        removed_file.close()'''


def write_file(file_path, file_content):
    file = open(file_path, 'w')
    file.write(file_content)
    file.close()


def read_file(file_path):
    file = open(file_path, 'r')

    with file:
        file_content = file.read()

    file.close()
    return file_content


def quit():
    # Close all open files to prevent corruption
    if open_files:
        for file in open_files.values():
            if file is not None:
                file.close()
