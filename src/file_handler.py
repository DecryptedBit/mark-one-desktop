import os
from enum import Enum
from pprint import pprint

from PyQt5.QtWidgets import QFileDialog, QMessageBox

from src import config

main_window = None
open_instances = {}


def initialize(main_window_inst):
    global main_window
    main_window = main_window_inst


def create_file(file_info=None):
    # Create a new markup editor instance and get the instance id
    instance_id = main_window.markup_editor_widget.create_instance()
    # Add a new instances to the open instances without any information
    open_instances_add(instance_id, file_info)


def open_file():
    # Get the file to open information
    file_info = instantiate_file_dialog(FileDialogType.OPEN, main_window, 'Open file', '*.txt')
    if file_info is None:
        return

    # Open the file using the given information and return the content
    file_content = read_file(file_info[1])

    # Check if the current editor instance has any text, if not we can populate this one
    if not main_window.markup_editor_widget.currentWidget().markup_input_widget.toPlainText():
        # Get the current markup editor instance id
        instance_id = main_window.markup_editor_widget.currentWidget().__hash__()
        # Update the markup editor instance information
        open_instances_update(instance_id, file_info)
    else:
        create_file(file_info)

    # Set the text of the current instance
    main_window.markup_editor_widget.currentWidget().markup_input_widget.setText(file_content)
    # Set the tab text of the current instance
    main_window.markup_editor_widget.setTabText(main_window.markup_editor_widget.currentIndex(), file_info[0])


def save_file():
    # Get the current markup editor instance id
    instance_id = main_window.markup_editor_widget.currentWidget().__hash__()
    # Get the current markup editor content
    file_content = main_window.markup_editor_widget.currentWidget().markup_input_widget.toPlainText()

    # Check if the markup editor has any information present. If it doesn't the file has not been saved before
    if open_instances[instance_id] is not None:
        # Write the content to the given file
        file_path = open_instances[instance_id][1]
        write_file(file_path, file_content)
        # Tell the markup editor and the current markup editor instance that the content has been saved
        main_window.markup_editor_widget.current_instance_content_saved()
    else:
        save_file_as(instance_id, file_content)


def save_file_as(instance_id=None, file_content=None):
    if instance_id is None:
        instance_id = main_window.markup_editor_widget.currentWidget().__hash__()
    if file_content is None:
        file_content = main_window.markup_editor_widget.currentWidget().markup_input_widget.toPlainText()

    file_info = instantiate_file_dialog(FileDialogType.SAVE, main_window, 'Save file as', '*.txt')
    if file_info is None:
        return

    #
    main_window.markup_editor_widget.setTabText(main_window.markup_editor_widget.currentIndex(), file_info[0])
    # Update the markup editor instance information
    open_instances_update(instance_id, file_info)
    # Write the content to the given file
    file_path = file_info[1]
    write_file(file_path, file_content)
    # Tell the markup editor and the current markup editor instance that the content has been saved
    main_window.markup_editor_widget.current_instance_content_saved()


def open_instances_add(id, file_info=None):
    global open_instances

    open_instances[id] = file_info
    pprint(open_instances)


def open_instances_update(id, file_info):
    global open_instances

    if id in open_instances:
        open_instances[id] = file_info

    pprint(open_instances)


def open_instances_remove(id):
    open_instances.pop(id)
    pprint(open_instances)


class FileDialogType(Enum):
    SAVE = "save"
    OPEN = "open"


def instantiate_file_dialog(file_dialog_type, parent, title, file_types):
    file_dialog_response = None

    # Create a file dialog and get the response
    if file_dialog_type == FileDialogType.OPEN:
        file_dialog_response = QFileDialog.getOpenFileName(parent, title, config.DEFAULT_SAVE_DIR, file_types)
    elif file_dialog_type == FileDialogType.SAVE:
        file_dialog_response = QFileDialog.getSaveFileName(parent, title, config.DEFAULT_SAVE_DIR, file_types)

    if not file_dialog_response:
        return None

    # Get all the information out of the response
    file_types = file_dialog_response[1]
    file_path = file_dialog_response[0]
    file_name = os.path.basename(file_path)

    # Check if the response was valid
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


def handle_instance_close_event(instance_num):
    # Set the tab to the current tab that is being inspected
    main_window.markup_editor_widget.setCurrentIndex(instance_num)
    markup_editor_instance = main_window.markup_editor_widget.currentWidget()

    # Check if the content of the markup editor instance has been edited
    if markup_editor_instance.content_edited is True:
        # Create a message box with all available options
        reply = QMessageBox.question(main_window, 'Unsaved Changes', f'Should we save __FILENAME__?',
                                     QMessageBox.Yes | QMessageBox.No | QMessageBox.Cancel,
                                     QMessageBox.Yes)

        # Read the message box reply
        if reply == QMessageBox.Yes:
            # Save the markup editor instance content
            save_file()

            # Remove and close the markup editor instance
            file_id = markup_editor_instance.__hash__()
            open_instances_remove(file_id)
            main_window.markup_editor_widget.removeTab(instance_num)
        elif reply == QMessageBox.No:
            # Remove and close the markup editor instance
            file_id = markup_editor_instance.__hash__()
            open_instances_remove(file_id)
            main_window.markup_editor_widget.removeTab(instance_num)
        elif reply == QMessageBox.Cancel:
            pass
    else:
        # Remove and close the markup editor instance
        file_id = markup_editor_instance.__hash__()
        open_instances_remove(file_id)
        main_window.markup_editor_widget.removeTab(instance_num)


def handle_application_close_event():
    save_all_required = False
    discard_all_required = False

    for i in reversed(range(main_window.markup_editor_widget.count())):
        # Set the tab to the current tab that is being inspected
        main_window.markup_editor_widget.setCurrentIndex(i)
        markup_editor_instance = main_window.markup_editor_widget.currentWidget()

        # Check if the content of the markup editor instance has been edited
        if markup_editor_instance.content_edited is True:
            if not save_all_required and not discard_all_required:
                # Create a message box with all available options
                reply = QMessageBox.question(main_window, 'Unsaved Changes', f'Should we save __FILENAME__?',
                                             QMessageBox.YesAll | QMessageBox.Yes | QMessageBox.No | QMessageBox.NoAll | QMessageBox.Cancel,
                                             QMessageBox.YesAll)

                # Read the message box reply
                if reply == QMessageBox.YesAll:
                    # Save all future files
                    save_all_required = True
                    # Save the markup editor instance content
                    save_file()
                    # Close the markup editor instance
                    #main_window.markup_editor_widget.close_instance(i)
                elif reply == QMessageBox.Yes:
                    # Save the markup editor instance content
                    save_file()
                    # Close the markup editor instance
                    #main_window.markup_editor_widget.close_instance(i)
                elif reply == QMessageBox.No:
                    # Close the markup editor instance without saving
                    #main_window.markup_editor_widget.close_instance(i)
                    pass
                elif reply == QMessageBox.NoAll:
                    # Discard all future files
                    discard_all_required = True
                elif reply == QMessageBox.Cancel:
                    # Cancel the close event
                    return False
            elif save_all_required:
                save_file()
                #main_window.markup_editor_widget.close_instance(i)
            elif discard_all_required:
                # Close the markup editor instance without saving
                # main_window.markup_editor_widget.close_instance(i)
                pass
        else:
            # Close the markup editor instance without saving since it doesn't have any changes
            #main_window.markup_editor_widget.close_instance(i)
            pass

    # Accept the close event
    return True
