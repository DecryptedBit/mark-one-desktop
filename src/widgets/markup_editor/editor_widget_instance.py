import sys

import mistune
from PyQt5 import QtCore, QtWidgets

from src.widgets.markup_editor import editor_instance_input_widget, editor_instance_preview_widget


class EditorInstance(object):
    def setup_ui(self, tab_widget, tab_num, tab_name):
        self.tab_num = tab_num
        self.tab_name = tab_name

        # Tab instance
        self.editor_tab_instance_widget = QtWidgets.QWidget()
        self.editor_tab_instance_widget.setEnabled(True)
        self.editor_tab_instance_widget.setObjectName("MarkupEditorTabInstanceWidget")

        # Tab instance layout
        self.editor_tab_instance_layout = QtWidgets.QGridLayout(self.editor_tab_instance_widget)
        self.editor_tab_instance_layout.setContentsMargins(0, 0, 0, 0)
        self.editor_tab_instance_layout.setObjectName("InstanceLayout")

        # Markup input
        self.markup_input_widget = editor_instance_input_widget.EditorInputInstance()
        self.markup_input_widget.setup_ui(self)

        # Markup preview
        self.markup_preview_widget = editor_instance_preview_widget.EditorPreviewInstance()
        self.markup_preview_widget.setup_ui()
        # self.markup_preview_widget.add_to_dock_widget(main_window)

        # Splitter between input and preview
        self.markup_input_preview_splitter = QtWidgets.QSplitter()
        self.markup_input_preview_splitter.addWidget(self.markup_input_widget.get_widget())
        self.markup_input_preview_splitter.addWidget(self.markup_preview_widget.get_widget())
        self.markup_input_preview_splitter.setSizes([sys.maxsize, sys.maxsize])
        self.editor_tab_instance_layout.addWidget(self.markup_input_preview_splitter)

        # Finalization
        tab_widget.addTab(self.editor_tab_instance_widget, f'{self.tab_name}')
        self.retranslate_ui(tab_widget)
        QtCore.QMetaObject.connectSlotsByName(tab_widget)

    def retranslate_ui(self, parent_tab_widget):
        _translate = QtCore.QCoreApplication.translate
        parent_tab_widget.setTabText(parent_tab_widget.indexOf(self.editor_tab_instance_widget), _translate("MainWindow", f'{self.tab_name}'))
        self.markup_preview_widget.retranslate_ui()

    def markup_input_text_changed(self, input_text):
        markdown_parser = mistune.Markdown()
        markdown = markdown_parser(input_text)

        self.markup_preview_widget.update_html(markdown)
