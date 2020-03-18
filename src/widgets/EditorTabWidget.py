from enum import Enum

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QTabWidget, QMessageBox

from src import widget_manager
from src.handlers import file_handler
from src.widgets import EditorTab


class EditorTabWidget(QTabWidget):
    edited_tab_amount = 0

    def __init__(self, parent=None):
        super(EditorTabWidget, self).__init__(parent)

        self.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.setAutoFillBackground(False)
        self.setStyleSheet("")
        self.setTabPosition(QtWidgets.QTabWidget.North)
        self.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.setElideMode(QtCore.Qt.ElideMiddle)
        self.setUsesScrollButtons(True)
        self.setDocumentMode(True)
        self.setTabsClosable(True)
        self.setMovable(True)
        self.setTabBarAutoHide(True)
        self.setCurrentIndex(0)
        self.tabCloseRequested.connect(self.close_file)

    # region File creation, opening and tab creation

    # Returns file path if file is created successfully
    def create_new_file(self):
        # Create a tab with the file path
        editor_tab = self.create_tab("New file")
        return editor_tab.get_file_path()

    # Returns file path if file is opened successfully
    # Returns none if opening failed
    def open_file(self):
        # Check if we already received a file path to open
        file_path = file_handler.instantiate_file_dialog(file_handler.FileDialogType.OPEN, 'Open file',
                                                         'Markdown Files (*.md)')

        # Check if the user cancelled opening the file resulting in none file path
        if not file_path:
            return None

        # Create a tab with the file path and content
        editor_tab = self.create_tab(file_path, file_handler.read_file(file_path))
        return editor_tab.get_file_path()

    def create_tab(self, file_path, file_content=None):
        # Create an editor tab widget
        editor_tab = EditorTab.EditorTab(file_path, file_content, self)
        editor_tab.onFirstContentEdit.connect(self.on_tab_first_content_edit)

        # Add the new editor tab widget as a tab and set the index to this tab
        self.addTab(editor_tab, editor_tab.get_file_name())
        self.setCurrentIndex(self.count() - 1)

        return editor_tab

    # endregion

    # region File and tab closing

    class CloseReplyType(Enum):
        CANCELLED = "cancelled"
        FAILED = "failed"
        FORCE_YES_ALL = "force_yes_all"
        FORCE_NO_ALL = "force_no_all"

    # Returns an array filled with file paths if all files were closed successfully
    # Returns CloseReplyType.FAILED if closing failed
    # Returns CloseReplyType.CANCELLED if closing was cancelled
    def close_files(self):
        if self.count() == 0:
            return self.CloseReplyType.FAILED

        forced_reply_type = None
        file_path_array = []

        for i in reversed(range(self.count())):
            # Determine if te multiple options option should be used
            multi_options = True
            if self.edited_tab_amount <= 1:
                multi_options = False

            close_reply_type = self.close_file(i, multi_options, forced_reply_type)

            # Read the close reply type
            if close_reply_type == self.CloseReplyType.CANCELLED or close_reply_type == self.CloseReplyType.FAILED:
                return close_reply_type
            elif close_reply_type == self.CloseReplyType.FORCE_YES_ALL \
                    or close_reply_type == self.CloseReplyType.FORCE_NO_ALL:
                forced_reply_type = close_reply_type
            else:
                file_path_array.append(close_reply_type)

        return file_path_array

    # Returns file path if closed successfully
    # Returns CloseReplyType.FAILED if closing failed
    # Returns CloseReplyType.CANCELLED if closing was cancelled
    def close_file(self, tab_num=None, multi_options=False, forced_type=None):
        if self.count() == 0:
            return self.CloseReplyType.FAILED

        if tab_num is None:
            tab_num = self.currentIndex()

        # Set the variables before setting the index in case the content has not been edited
        editor_tab = self.widget(tab_num)
        file_path = editor_tab.get_file_path()

        # Check if the content has been edited or not
        # If not then there is no need to create a message box
        if not editor_tab.content_edited:
            self.removeTab(tab_num)
            return file_path

        # Set the current index since the content has been edited
        self.setCurrentIndex(tab_num)

        # Create a message box with options
        dialog_result = None

        if forced_type is None:
            if multi_options:
                dialog_result = QMessageBox.question(widget_manager.main_window, 'Unsaved Changes',
                                                     f'Should we save \'{editor_tab.get_file_name()}\'?',
                                                     QMessageBox.YesAll | QMessageBox.Yes | QMessageBox.No |
                                                     QMessageBox.NoAll | QMessageBox.Cancel, QMessageBox.YesAll)
            else:
                dialog_result = QMessageBox.question(widget_manager.main_window, 'Unsaved Changes',
                                                     f'Should we save \'{editor_tab.get_file_name()}\'?',
                                                     QMessageBox.Yes | QMessageBox.No |
                                                     QMessageBox.Cancel, QMessageBox.Yes)

        # Read the message box result
        if forced_type == self.CloseReplyType.FORCE_YES_ALL or dialog_result == QMessageBox.YesAll:
            save_dialog_result = self.save_file()

            if save_dialog_result is not None:
                self.removeTab(self.currentIndex())

            return self.CloseReplyType.FORCE_YES_ALL
        elif dialog_result == QMessageBox.Yes:
            save_dialog_result = self.save_file()

            if save_dialog_result is not None:
                self.removeTab(self.currentIndex())

            return file_path
        elif forced_type == self.CloseReplyType.FORCE_NO_ALL or dialog_result == QMessageBox.NoAll:
            self.removeTab(self.currentIndex())
            return self.CloseReplyType.FORCE_NO_ALL
        elif dialog_result == QMessageBox.No:
            self.removeTab(self.currentIndex())
            return file_path
        elif dialog_result == QMessageBox.Cancel or dialog_result is None:
            return self.CloseReplyType.CANCELLED

    # endregion

    # region File saving and saving as

    # Returns file path if file is saved successfully
    # Returns none if saving failed
    def save_file(self):
        if self.count() == 0:
            return None

        editor_tab = self.currentWidget()

        if editor_tab.get_is_new_file():
            return self.save_file_as()
        else:
            # Write the content to the file path
            self.reset_tab_state()
            file_handler.write_file(editor_tab.get_file_path(),
                                    editor_tab.get_content())
            return editor_tab.get_file_path()

    # Returns file path if file is saved successfully
    # Returns none if saving failed
    def save_file_as(self):
        if self.count() == 0:
            return None

        editor_tab = self.currentWidget()

        # Instantiate a dialog to save the file as, and check if it got cancelled resulting in no file path
        new_file_path = file_handler.instantiate_file_dialog(file_handler.FileDialogType.SAVE, 'Save file as',
                                                             'Markdown Files (*.md)')
        if new_file_path is None:
            return None

        self.update_tab(new_file_path)
        file_handler.write_file(editor_tab.get_file_path(),
                                editor_tab.get_content())

        return editor_tab.get_file_path()

    # endregion

    # region Miscellaneous tab methods

    def update_tab(self, file_path):
        editor_tab = self.currentWidget()
        editor_tab.update(file_path)

        self.reset_tab_state()
        self.setTabText(self.currentIndex(), editor_tab.get_file_name())

    def reset_tab_state(self):
        self.edited_tab_amount -= 1

        current_tab_text = self.tabText(self.currentIndex())
        editor_tab = self.currentWidget()

        editor_tab.set_is_new_file(False)

        # Remove the indication that told the contact has changed
        if editor_tab.content_edited:
            self.setTabText(self.currentIndex(), current_tab_text[:-2])
            editor_tab.reset_changed_state()

    def on_tab_first_content_edit(self):
        self.edited_tab_amount += 1

        # Update the tab text to indicate a change in content after the last save
        self.setTabText(self.currentIndex(), f'{self.currentWidget().get_file_name()} *')

    # endregion
