from pprint import pprint

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QTabWidget

from src.handlers import file_handler
from src.widgets.markup_editor import editor_widget_instance


class MarkupEditorWidget(QTabWidget):
    def __init__(self, parent=None):
        super(MarkupEditorWidget, self).__init__(parent)
        self.init_ui()

        self.open_instances = {}

    def init_ui(self):
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

        # Finalization
        self.setCurrentIndex(0)
        self.setTabsClosable(True)
        self.tabCloseRequested.connect(file_handler.close_file)
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslate_ui(self):
        _translate = QtCore.QCoreApplication.translate

    def create_instance(self, file_info, file_content=""):
        # Create a new markup editor instance and get the instance id
        instance_id = self.create_editor_instance(file_info[0])

        # Add a new instances to the open instances
        instance_info = [instance_id, file_info, False, file_content]
        self.open_instances[instance_id] = instance_info
        pprint(self.open_instances)

        # Set the text of the current instance
        self.currentWidget().set_content(file_content)
        self.current_instance_reset_content_changed(instance_id)

    def update_instance(self, instance_info):
        file_info = instance_info[1]

        # Tell the markup editor and the current markup editor instance that the content has been saved
        self.current_instance_reset_content_changed(instance_info[0])

        # Update the tab text
        self.setTabText(self.currentIndex(), file_info[0])

    def close_instance(self):
        # Remove and close the markup editor instance
        instance_id = self.currentWidget().__hash__()

        self.open_instances.pop(instance_id)
        pprint(self.open_instances)

        self.removeTab(self.currentIndex())

    def create_editor_instance(self, instance_name="New file"):
        # Create a editor instance widget
        instance_tab = editor_widget_instance.EditorInstanceWidget(self)
        instance_tab.contentChanged.connect(self.current_instance_content_changed)
        instance_tab.retranslate_ui()

        # Get the editor instance widget hash to use as the unique identifier
        instance_id = instance_tab.__hash__()

        # Add the new editor instance widget as a tab and set the index to this tab
        self.addTab(instance_tab, instance_name)
        self.setCurrentIndex(self.count() - 1)

        return instance_id

    def get_current_instance_info(self):
        if self.currentWidget() is None:
            return None

        instance_id = self.currentWidget().__hash__()

        # Update the content held in the open instance info
        self.update_instance_info(instance_id=instance_id,
                                  new_instance_content=self.currentWidget().markup_input_widget.toPlainText())

        return self.open_instances[instance_id]

    def update_instance_info(self, instance_info=None, instance_id=None, new_file_info=None, new_instance_edited=None,
                             new_instance_content=None):
        # The should be either an instance_info or instance_id given
        if instance_info is None:
            instance_info = self.open_instances[instance_id]

        # Update the file information
        if new_file_info is not None:
            instance_info[1] = new_file_info

        # Update the edited boolean
        if new_instance_edited is not None:
            instance_info[2] = new_instance_edited

        # Update the content
        if new_instance_content is not None:
            instance_info[3] = new_instance_content

    def current_instance_content_changed(self):
        current_instance = self.currentWidget()
        instance_id = current_instance.__hash__()
        current_tab_text = self.tabText(self.currentIndex())

        # Update the tab text to indicate a change in content after the last save
        if current_tab_text.endswith("*") is False:
            self.setTabText(self.currentIndex(), f'{current_tab_text} *')
            self.open_instances[instance_id][2] = True

    def current_instance_reset_content_changed(self, instance_id):
        current_tab_text = self.tabText(self.currentIndex())

        # Remove the indication that told the contact has changed
        if current_tab_text.endswith("*"):
            self.setTabText(self.currentIndex(), current_tab_text[:-2])
            self.open_instances[instance_id][2] = False

        self.currentWidget().reset_content_changed()
