import mistune
from PyQt5 import QtCore, QtWidgets

from src.widgets import MarkupEditorInstancePreview


class MarkupEditorInstanceUI(object):
    def setup_ui(self, main_window, tab_widget, tab_num):
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
        self.markup_input_widget = QtWidgets.QTextEdit(self.editor_tab_instance_widget)
        self.markup_input_widget.setStyleSheet("")
        self.markup_input_widget.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.markup_input_widget.setFrameShadow(QtWidgets.QFrame.Plain)
        self.markup_input_widget.setLineWidth(1)
        self.markup_input_widget.setObjectName("InstanceInputWidget")
        self.editor_tab_instance_layout.addWidget(self.markup_input_widget, 0, 0, 1, 1)
        markdown = mistune.Markdown()
        self.markup_input_widget.append(markdown(
            '# I am using the mistune markdown parser \n\n ## Cool stuff! \n\n **Lets see if this works**'))

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
