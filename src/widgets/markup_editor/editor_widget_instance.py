import sys

from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QWidget

from src.handlers import converter_handler
from src.widgets.markup_editor import editor_instance_input_widget, editor_instance_preview_widget
from src.widgets.markup_editor.actions_bar.editor_instance_actions_bar_widget import EditorInstanceActionsBarWidget


class EditorInstanceWidget(QWidget):
    contentChanged = QtCore.pyqtSignal()
    converter = None

    def __init__(self, parent=None):
        self.parent = parent
        self.content_edited = False

        super(EditorInstanceWidget, self).__init__(parent)
        self.init_ui()

    def init_ui(self):
        self.layout = QtWidgets.QVBoxLayout(self)
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.layout.setSpacing(0)

        # Markup actions bar
        self.actions_bar_widget = EditorInstanceActionsBarWidget(self)
        self.actions_bar_widget.converterSelectionChanged.connect(self.converter_selection_changed)

        converter_selection = self.actions_bar_widget.get_converter_selection()
        self.converter_selection_changed(converter_selection[0], converter_selection[1], converter_selection[2])

        self.layout.addWidget(self.actions_bar_widget)

        # Markup editor widgets
        self.editor_widget = QtWidgets.QWidget(self)
        self.layout.addWidget(self.editor_widget, 1)

        self.editor_widget_layout = QtWidgets.QGridLayout(self.editor_widget)
        self.editor_widget_layout.setContentsMargins(0, 0, 0, 0)

        # Markup input
        self.markup_input_widget = editor_instance_input_widget.EditorInputInstanceWidget(self)
        self.markup_input_widget.contentChanged.connect(self.content_changed)

        # Markup preview
        self.markup_preview_widget = editor_instance_preview_widget.EditorPreviewInstanceWidget(self)

        # Splitter between input and preview
        self.markup_input_preview_splitter = QtWidgets.QSplitter()
        self.markup_input_preview_splitter.addWidget(self.markup_input_widget)
        self.markup_input_preview_splitter.addWidget(self.markup_preview_widget)
        self.markup_input_preview_splitter.setSizes([sys.maxsize, sys.maxsize])
        self.editor_widget_layout.addWidget(self.markup_input_preview_splitter)

        # Finalization
        self.retranslate_ui()
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslate_ui(self):
        _translate = QtCore.QCoreApplication.translate

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
        self.content_edited = True

        if self.converter is not None:
            converted_content = self.converter.convert(content)
            self.markup_preview_widget.update_html(converted_content)

        self.contentChanged.emit()

    def reset_content_changed(self):
        self.content_edited = False

    def set_content(self, content):
        self.markup_input_widget.setText(content)
