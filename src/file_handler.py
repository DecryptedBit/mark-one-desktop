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
    instance_id = main_window.markup_editor_widget.create_instance()
    open_files_add(instance_id)


def open_file():
    file_info = instantiate_file_dialog(main_window, 'Open file', '*.txt')
    if file_info is None:
        return

    file_content = read_file(file_info[1])

    if not main_window.markup_editor_widget.currentWidget().markup_input_widget.toPlainText():
        # If the current editor instance is empty, get the current widget id and update the file
        instance_id = main_window.markup_editor_widget.currentWidget().__hash__()
        open_files_update(instance_id, file_info)
    else:
        # If the current editor instance is filled, create a new widget and add the file
        instance_id = main_window.markup_editor_widget.create_instance()
        open_files_add(instance_id, file_info)

    main_window.markup_editor_widget.currentWidget().markup_input_widget.setText(file_content)
    main_window.markup_editor_widget.setTabText(main_window.markup_editor_widget.currentIndex(), file_info[0])


def save_file():
    instance_id = main_window.markup_editor_widget.currentWidget().__hash__()
    file_content = main_window.markup_editor_widget.currentWidget().markup_input_widget.toPlainText()

    if open_files[instance_id] is not None:
        file_path = open_files[instance_id][1]
        write_file(file_path, file_content)
        main_window.markup_editor_widget.current_instance_content_saved()
    else:
        save_file_as(instance_id, file_content)


def save_file_as(instance_id=None, file_content=None):
    if instance_id is None:
        instance_id = main_window.markup_editor_widget.currentWidget().__hash__()
    if file_content is None:
        file_content = main_window.markup_editor_widget.currentWidget().markup_input_widget.toPlainText()

    file_info = instantiate_file_dialog(main_window, 'Save file as', '*.txt')
    if file_info is None:
        return

    main_window.markup_editor_widget.setTabText(main_window.markup_editor_widget.currentIndex(), file_info[0])
    open_files_update(instance_id, file_info)
    write_file(file_info[1], file_content)
    main_window.markup_editor_widget.current_instance_content_saved()


def open_files_add(id, file_info=None):
    global open_files

    open_files[id] = file_info
    pprint(open_files)


def open_files_update(id, file_info):
    global open_files

    if id in open_files:
        open_files[id] = file_info

    pprint(open_files)


def open_files_remove(id):
    open_files.pop(id)
    pprint(open_files)


def instantiate_file_dialog(parent, title, file_types):
    file_dialog_response = QFileDialog.getOpenFileName(parent, title, config.DEFAULT_SAVE_DIR, file_types)

    pprint(f'{file_dialog_response[0]}, {file_dialog_response[1]}')

    file_types = file_dialog_response[1]
    file_path = file_dialog_response[0]
    file_name = os.path.basename(file_path)

    if not file_path:
        return None
    else:
        return file_name, file_path, file_types


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
    pass
