from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QWidget

from src.widgets.markup_editor import editor_widget_instance


class MarkupEditorWidget(QWidget):
    def __init__(self, parent=None):
        super(MarkupEditorWidget, self).__init__(parent)
        self.init_ui()

    def init_ui(self):
        self.setObjectName("MarkupEditorWidget")

        # Markup editor layout
        self.editor_layout = QtWidgets.QGridLayout(self)
        self.editor_layout.setContentsMargins(0, 0, 0, 0)
        self.editor_layout.setSpacing(3)
        self.editor_layout.setObjectName("MainLayout")

        # Tab widget
        self.tab_widget = QtWidgets.QTabWidget(self)
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

        # Editor instances
        self.instance_tab_1 = editor_widget_instance.EditorInstance()
        self.instance_tab_1.setup_ui(self.tab_widget, 1)

        self.instance_tab_2 = editor_widget_instance.EditorInstance()
        self.instance_tab_2.setup_ui(self.tab_widget, 2)

        # Finalization
        self.editor_layout.addWidget(self.tab_widget, 0, 0, 1, 1)
        #self.setLayout(self.editor_layout)
        self.tab_widget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslate_ui(self):
        _translate = QtCore.QCoreApplication.translate

        self.instance_tab_1.retranslate_ui(self.tab_widget)
        self.instance_tab_2.retranslate_ui(self.tab_widget)
