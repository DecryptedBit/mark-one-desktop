import os
from enum import Enum

from PyQt5.QtWidgets import QFileDialog, QMessageBox

from src import config

main_window = None


def initialize(main_window_inst):
    global main_window
    main_window = main_window_inst


def create_file():
    main_window.markup_editor_widget.create_instance(["New file", None, None])


def open_file(file_info=None):
    # Check if we already received a file path to open
    if not file_info:
        file_info = instantiate_file_dialog(FileDialogType.OPEN, 'Open file', '*.txt')

        # Check if the user cancelled opening the file resulting in none file info
        if not file_info:
            return None

    # Create an instance with the file contents
    main_window.markup_editor_widget.create_instance(file_info, read_file(file_info[1]))

    return file_info


def save_file(instance_info=None):
    if instance_info is None:
        instance_info = main_window.markup_editor_widget.get_current_instance_info()

        if instance_info is None:
            return None

    file_info = instance_info[1]

    # Check if the markup editor has complete file information present. If it doesn't the file has not been saved before
    if None not in file_info:
        instance_content = instance_info[3]

        # Write the content to the given file
        file_path = file_info[1]
        write_file(file_path, instance_content)

        # Update the markup editor instance
        main_window.markup_editor_widget.update_instance(instance_info)
    else:
        instance_info = save_file_as(instance_info)

    return instance_info


def save_file_as(instance_info=None):
    if instance_info is None:
        instance_info = main_window.markup_editor_widget.get_current_instance_info()

        if instance_info is None:
            return None

    # Instantiate a dialog to save the file as, and check if it got cancelled resulting in no file info
    new_file_info = instantiate_file_dialog(FileDialogType.SAVE, 'Save file as', '*.txt')
    if new_file_info is None:
        return None

    # Update the instance_info variable with the newly acquired information
    main_window.markup_editor_widget.update_instance_info(instance_info=instance_info, new_file_info=new_file_info)

    save_file(instance_info)

    return instance_info


class CloseFileReplyType(Enum):
    YES_ALL = "yes all"
    NO_ALL = "no all"
    CANCEL = "cancel"


def close_file(tab_num, multi_file_options=False, forced_close_option=None):
    # Get the right instance and set the tab
    main_window.markup_editor_widget.setCurrentIndex(tab_num)
    instance_info = main_window.markup_editor_widget.get_current_instance_info()
    file_info = instance_info[1]

    # Check if the instance content has been edited
    if instance_info[2] is False:
        # Remove and close the instance
        main_window.markup_editor_widget.close_instance()
        return None

    # Create a message box with all available options
    if forced_close_option is None and multi_file_options is True:
        reply = QMessageBox.question(main_window, 'Unsaved Changes', f'Should we save \'{file_info[0]}\'?',
                                     QMessageBox.YesAll | QMessageBox.Yes | QMessageBox.No | QMessageBox.NoAll |
                                     QMessageBox.Cancel, QMessageBox.YesAll)
    elif forced_close_option is None and multi_file_options is False:
        reply = QMessageBox.question(main_window, 'Unsaved Changes', f'Should we save \'{file_info[0]}\'?',
                                     QMessageBox.Yes | QMessageBox.No | QMessageBox.Cancel,
                                     QMessageBox.Yes)
    else:
        reply = None

    # Read the message box reply
    if reply == QMessageBox.YesAll or (reply is None and forced_close_option is CloseFileReplyType.YES_ALL):
        # Save the markup editor instance content
        save_file()
        # Remove and close the instance
        main_window.markup_editor_widget.close_instance()
        return CloseFileReplyType.YES_ALL
    elif reply == QMessageBox.Yes:
        # Save the markup editor instance content
        save_file()
        # Remove and close the instance
        main_window.markup_editor_widget.close_instance()
    elif reply == QMessageBox.No:
        # Remove and close the instance
        main_window.markup_editor_widget.close_instance()
    elif reply == QMessageBox.NoAll or (reply is None and forced_close_option is CloseFileReplyType.NO_ALL):
        # Remove and close the instance
        main_window.markup_editor_widget.close_instance()
        return CloseFileReplyType.NO_ALL
    elif reply == QMessageBox.Cancel:
        return CloseFileReplyType.CANCEL


class FileDialogType(Enum):
    SAVE = "save"
    OPEN = "open"


def instantiate_file_dialog(file_dialog_type, title, file_types):
    file_dialog_response = None

    # Create a file dialog and get the response
    if file_dialog_type == FileDialogType.OPEN:
        file_dialog_response = QFileDialog.getOpenFileName(main_window, title, config.DEFAULT_SAVE_DIR, file_types)
    elif file_dialog_type == FileDialogType.SAVE:
        file_dialog_response = QFileDialog.getSaveFileName(main_window, title, config.DEFAULT_SAVE_DIR, file_types)

    # Check if the response was valid
    if '' in file_dialog_response or file_dialog_response is None:
        return None

    # Get all the information out of the response
    file_types = file_dialog_response[1]
    file_path = file_dialog_response[0]
    file_name = os.path.basename(file_path)

    return file_name, file_path, file_types


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
