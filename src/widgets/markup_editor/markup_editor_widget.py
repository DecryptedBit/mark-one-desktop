from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QTabWidget

from src import file_handler
from src.widgets.markup_editor import editor_widget_instance


class MarkupEditorWidget(QTabWidget):
    def __init__(self, parent=None):
        super(MarkupEditorWidget, self).__init__(parent)
        self.init_ui()

    def init_ui(self):
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

        # Finalization
        self.setCurrentIndex(0)
        self.setTabsClosable(True)
        self.tabCloseRequested.connect(self.close_instance)
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslate_ui(self):
        _translate = QtCore.QCoreApplication.translate

    def create_instance(self, file_name="New file"):
        instance_tab = editor_widget_instance.EditorInstanceWidget(self)
        instance_tab.retranslate_ui()

        instance_id = instance_tab.__hash__()

        self.addTab(instance_tab, file_name)
        self.setCurrentIndex(self.count() - 1)

        return instance_id

    def close_instance(self, instance_num):
        file_id = self.widget(instance_num).__hash__()
        file_handler.open_files_remove(file_id)
        self.removeTab(instance_num)
