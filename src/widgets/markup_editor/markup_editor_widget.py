from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QTabWidget

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

        # Editor instances
        self.instance_tab_1 = editor_widget_instance.EditorInstanceWidget(self)
        self.addTab(self.instance_tab_1, "Tab 1")

        self.instance_tab_2 = editor_widget_instance.EditorInstanceWidget(self)
        self.addTab(self.instance_tab_2, "Tab 2")

        # Finalization
        self.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslate_ui(self):
        _translate = QtCore.QCoreApplication.translate
        self.instance_tab_1.retranslate_ui()
        self.instance_tab_2.retranslate_ui()
