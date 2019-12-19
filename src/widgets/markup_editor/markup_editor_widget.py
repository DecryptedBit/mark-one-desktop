from PyQt5 import QtCore, QtGui, QtWidgets

from src import file_handler
from src.widgets.markup_editor import editor_widget_instance


class MarkupEditor(object):
    editor_instances = []
    editor_instance_num = 0

    def setup_ui(self, main_window):
        self.main_window = main_window

        self.editor_widget = QtWidgets.QWidget(main_window)
        self.editor_widget.setObjectName("MarkupEditorWidget")

        # Markup editor layout
        self.editor_layout = QtWidgets.QGridLayout(self.editor_widget)
        self.editor_layout.setContentsMargins(0, 0, 0, 0)
        self.editor_layout.setSpacing(3)
        self.editor_layout.setObjectName("MainLayout")

        # Tab widget
        self.tab_widget = QtWidgets.QTabWidget(self.editor_widget)
        self.tab_widget.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.tab_widget.setAutoFillBackground(False)
        self.tab_widget.setStyleSheet("")
        self.tab_widget.setTabPosition(QtWidgets.QTabWidget.North)
        self.tab_widget.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.tab_widget.setElideMode(QtCore.Qt.ElideMiddle)
        self.tab_widget.setUsesScrollButtons(True)
        self.tab_widget.setDocumentMode(True)
        self.tab_widget.setTabsClosable(True)
        self.tab_widget.setMovable(True)
        self.tab_widget.setTabBarAutoHide(True)
        self.tab_widget.setObjectName("TabWidget")

        # Finalization
        self.editor_layout.addWidget(self.tab_widget, 0, 0, 1, 1)
        self.main_window.setCentralWidget(self.tab_widget)
        self.retranslate_ui()
        self.tab_widget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(self.main_window)

    def retranslate_ui(self):
        if self.editor_instances:
            _translate = QtCore.QCoreApplication.translate
            for editor_instance in self.editor_instances:
                editor_instance.retranslate_ui(self.tab_widget)

    def create_instance(self, file_name="New file"):
        self.editor_instance_num += 1

        instance_tab = editor_widget_instance.EditorInstance()
        instance_tab.setup_ui(self.tab_widget, self.editor_instance_num, file_name)

        self.tab_widget.setCurrentIndex(self.editor_instance_num - 1)

        self.editor_instances.append(instance_tab)

        return self.editor_instance_num
