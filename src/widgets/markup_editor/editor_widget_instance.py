import sys

import mistune
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QWidget

from src.widgets.markup_editor import editor_instance_input_widget, editor_instance_preview_widget


class EditorInstanceWidget(QWidget):
    def __init__(self, parent=None):
        self.parent = parent
        self.content_edited = False

        super(EditorInstanceWidget, self).__init__(parent)
        self.init_ui()

    def init_ui(self):
        self.setObjectName("MarkupEditorTabInstanceWidget")

        # Tab instance layout
        self.editor_tab_instance_layout = QtWidgets.QGridLayout(self)
        self.editor_tab_instance_layout.setContentsMargins(0, 0, 0, 0)
        self.editor_tab_instance_layout.setObjectName("InstanceLayout")

        # Markup input
        self.markup_input_widget = editor_instance_input_widget.EditorInputInstanceWidget(self)

        # Markup preview
        self.markup_preview_widget = editor_instance_preview_widget.EditorPreviewInstanceWidget(self)

        # Splitter between input and preview
        self.markup_input_preview_splitter = QtWidgets.QSplitter()
        self.markup_input_preview_splitter.addWidget(self.markup_input_widget)
        self.markup_input_preview_splitter.addWidget(self.markup_preview_widget)
        self.markup_input_preview_splitter.setSizes([sys.maxsize, sys.maxsize])
        self.editor_tab_instance_layout.addWidget(self.markup_input_preview_splitter)

        # Finalization
        self.retranslate_ui()
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslate_ui(self):
        _translate = QtCore.QCoreApplication.translate

    def markup_input_text_changed(self, input_text):
        markdown_parser = mistune.Markdown()
        markdown = markdown_parser(input_text)

        self.markup_preview_widget.update_html(markdown)
        self.content_changed()

    def content_changed(self):
        self.content_edited = True
        # Parent is the markup editor widget, this sets the name of the tab to indicate a change in the instance
        self.parent.current_instance_content_changed()

    def reset_content_changed(self):
        self.content_edited = False
