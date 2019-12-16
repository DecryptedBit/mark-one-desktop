from PyQt5 import QtCore, QtGui, QtWidgets

from src.widgets import MarkupEditorTabInstance


class MarkupEditorUI(object):
    def setup_ui(self, parent_widget):
        self.editor_widget = QtWidgets.QWidget(parent_widget)
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

        # Tab instances
        self.tab_widget_tab_1 = MarkupEditorTabInstance.MarkupEditorTabInstanceUI()
        self.tab_widget_tab_1.setup_ui(self.tab_widget, 1)

        self.tab_widget_tab_2 = MarkupEditorTabInstance.MarkupEditorTabInstanceUI()
        self.tab_widget_tab_2.setup_ui(self.tab_widget, 2)

        # Finalization
        self.editor_layout.addWidget(self.tab_widget, 0, 0, 1, 1)
        parent_widget.setCentralWidget(self.tab_widget)
        self.retranslate_ui(parent_widget)
        self.tab_widget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(parent_widget)

    def retranslate_ui(self, editor_widget):
        _translate = QtCore.QCoreApplication.translate
