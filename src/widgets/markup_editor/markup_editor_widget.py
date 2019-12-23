from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QTabWidget

from src.widgets.markup_editor import editor_widget_instance


class MarkupEditorWidget(QTabWidget):
    def __init__(self, parent=None):
        super(MarkupEditorWidget, self).__init__(parent)
        self.init_ui()

    def init_ui(self):
        self.editor_instance_num = 0
        self.editor_instances = []

        self.setObjectName("MarkupEditorWidget")
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

        # Editor instances
        self.create_instance()

        # Finalization
        self.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslate_ui(self):
        _translate = QtCore.QCoreApplication.translate

        if self.editor_instances:
            _translate = QtCore.QCoreApplication.translate
            for editor_instance in self.editor_instances:
                editor_instance.retranslate_ui()

    def create_instance(self, file_name="New file"):
        self.editor_instance_num += 1

        instance_tab = editor_widget_instance.EditorInstanceWidget(self)
        instance_id = instance_tab.__hash__()

        self.addTab(instance_tab, file_name)
        self.setCurrentIndex(self.editor_instance_num - 1)

        self.editor_instances.append(instance_tab)

        return instance_id
