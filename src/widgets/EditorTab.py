import os

from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QWidget

from src.handlers import converter_handler
from src.widgets import EditorTextEdit, EditorWebEngineView, EditorActionsWidget


class EditorTab(QWidget):
    onFirstContentEdit = QtCore.pyqtSignal()
    converter = None

    def __init__(self, file_path, file_content=None, parent=None):
        self.file_path = file_path

        if not file_content:
            self.is_new_file = True
        else:
            self.is_new_file = False

        self.content_edited = False

        super(EditorTab, self).__init__(parent)

        self.layout = QtWidgets.QVBoxLayout(self)
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.layout.setSpacing(0)
        self.setLayout(self.layout)

        # Editor actions widget
        self.editor_actions_widget = EditorActionsWidget.EditorActionsWidget(self)
        self.editor_actions_widget.converterSelectionChanged.connect(self.converter_selection_changed)

        converter_selection = self.editor_actions_widget.get_converter_selection()
        self.converter_selection_changed(converter_selection[0], converter_selection[1], converter_selection[2])

        self.layout.addWidget(self.editor_actions_widget)

        # Editor text edit parent
        self.editor_widget = QtWidgets.QWidget(self)
        self.layout.addWidget(self.editor_widget, 1)

        self.editor_widget_layout = QtWidgets.QGridLayout(self.editor_widget)
        self.editor_widget_layout.setContentsMargins(0, 0, 0, 0)
        self.editor_widget.setLayout(self.editor_widget_layout)

        # Editor text edit
        self.editor_text_edit = EditorTextEdit.EditorTextEdit(self)
        if file_content:
            self.editor_text_edit.setText(file_content)
        self.editor_text_edit.contentChanged.connect(self.content_changed)

        # Markup preview
        self.editor_web_engine_view = EditorWebEngineView.EditorWebEngineView(self)

        # Splitter between input and preview
        self.splitter = QtWidgets.QSplitter()
        self.splitter.addWidget(self.editor_text_edit)
        self.splitter.addWidget(self.editor_web_engine_view)
        self.splitter.setSizes([1000, 1000])
        self.editor_widget_layout.addWidget(self.splitter)

        # Finalization
        self.convert_content(self.editor_text_edit.toPlainText())

    def update(self, file_path):
        self.file_path = file_path

    def converter_selection_changed(self, converter_name, from_type_index, to_type_index):
        converter_class = converter_handler.get_converter(converter_name)

        if self.converter is None or self.converter.get_name() != converter_class.get_name():
            print("Converter switched:")
            self.converter = converter_class(from_type_index, to_type_index)
        else:
            print("Converter updated:")
            self.converter.set_from_type(from_type_index)
            self.converter.set_to_type(to_type_index)

        print("\tUsing:", self.converter.get_name(),
              "\n\tFrom:", self.converter.get_from_type(),
              "\n\tTo:", self.converter.get_to_type())

    def content_changed(self, content):
        if self.content_edited is False:
            self.onFirstContentEdit.emit()
            self.content_edited = True

        self.convert_content(content)

    def convert_content(self, content):
        if self.converter is not None:
            converted_content = self.converter.convert(content)
            self.editor_web_engine_view.update_content(converted_content)

    def reset_changed_state(self):
        self.content_edited = False

    def get_file_path(self):
        return self.file_path

    def get_file_name(self):
        return os.path.basename(self.file_path)

    def set_is_new_file(self, boolean):
        self.is_new_file = boolean

    def get_is_new_file(self):
        return self.is_new_file

    def set_content(self, content):
        self.editor_text_edit.setText(content)

    def get_content(self):
        return self.editor_text_edit.toPlainText()
