import mistune
from PyQt5 import QtCore, QtWidgets

from src.widgets import MarkupEditorInstancePreview, MarkupEditorInstanceInput


class MarkupEditorInstanceUI(object):
    def setup_ui(self, tab_widget, tab_num):
        self.tab_num = tab_num

        # Tab instance
        self.editor_tab_instance_widget = QtWidgets.QWidget()
        self.editor_tab_instance_widget.setEnabled(True)
        self.editor_tab_instance_widget.setObjectName("MarkupEditorTabInstanceWidget")

        # Tab instance layout
        self.editor_tab_instance_layout = QtWidgets.QGridLayout(self.editor_tab_instance_widget)
        self.editor_tab_instance_layout.setContentsMargins(0, 0, 0, 0)
        self.editor_tab_instance_layout.setObjectName("InstanceLayout")

        # Markup input
        self.markup_input_widget = MarkupEditorInstanceInput.MarkupEditorInstanceInputUI()
        self.markup_input_widget.setup_ui(self, self.editor_tab_instance_widget)
        self.markup_input_widget.add_to_grid_layout(self.editor_tab_instance_layout, 0, 0)

        # Markup preview
        self.markup_preview_widget = MarkupEditorInstancePreview.MarkupEditorPreviewInstanceUI()
        self.markup_preview_widget.setup_ui()
        self.markup_preview_widget.add_to_grid_Layout(self.editor_tab_instance_layout, 0, 1)
        # self.markup_preview_widget.add_to_dock_widget(main_window)

        # Finalization
        tab_widget.addTab(self.editor_tab_instance_widget, f'Tab {self.tab_num}')
        self.retranslate_ui(tab_widget)
        QtCore.QMetaObject.connectSlotsByName(tab_widget)

    def retranslate_ui(self, parent_tab_widget):
        _translate = QtCore.QCoreApplication.translate
        parent_tab_widget.setTabText(parent_tab_widget.indexOf(self.editor_tab_instance_widget), _translate("MainWindow", f'Tab {self.tab_num}'))
        self.markup_preview_widget.retranslate_ui()

    def markup_input_text_changed(self, input_text):
        markdown_parser = mistune.Markdown()
        markdown = markdown_parser(input_text)

        self.markup_preview_widget.update_html(markdown)
