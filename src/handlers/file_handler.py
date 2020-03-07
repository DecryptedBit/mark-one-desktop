import os
from enum import Enum

from PyQt5.QtWidgets import QFileDialog

from src import config, widget_manager


class FileDialogType(Enum):
    SAVE = "save"
    OPEN = "open"


def instantiate_file_dialog(file_dialog_type, title, file_types):
    file_dialog_response = None

    # Create a file dialog and get the response
    if file_dialog_type == FileDialogType.OPEN:
        file_dialog_response = QFileDialog.getOpenFileName(widget_manager.main_window, title,
                                                           config.DEFAULT_SAVE_DIR, file_types)
    elif file_dialog_type == FileDialogType.SAVE:
        file_dialog_response = QFileDialog.getSaveFileName(widget_manager.main_window, title,
                                                           config.DEFAULT_SAVE_DIR, file_types)

    file_path = file_dialog_response[0]

    # Check if the response was valid
    if file_path == '' or file_dialog_response is None:
        return None

    return file_path


def write_file(file_path, file_content):
    with open(file_path, 'w') as file:
        file.write(file_content)
        file.close()


def append_file(file_path, append_text):
    os.makedirs(os.path.dirname(file_path), exist_ok=True)
    with open(file_path, 'a+') as file:
        file.write(append_text + "\n")
        file.close()


def read_file(file_path):
    with open(file_path, 'r') as file:
        file_content = file.read()
        file.close()
        return file_content
