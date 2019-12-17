import mistune
from PyQt5 import QtCore, QtWidgets


class MarkupPreviewerUI(object):
    def setup_ui(self, parent_widget):
        # Preview dock widget master
        self.preview_dock_widget = QtWidgets.QDockWidget(parent_widget)
        self.preview_dock_widget.setStyleSheet("")
        self.preview_dock_widget.setObjectName("PreviewDockWidget")

        # Preview widget
        self.preview_widget = QtWidgets.QWidget()
        self.preview_widget.setObjectName("PreviewWidget")

        # Preview layout
        self.preview_layout = QtWidgets.QGridLayout(self.preview_widget)
        self.preview_layout.setContentsMargins(3, 3, 3, 3)
        self.preview_layout.setObjectName("PreviewLayout")

        # Preview content
        self.preview_content_widget = QtWidgets.QWidget(self.preview_widget)
        self.preview_content_widget.setObjectName("PreviwContentWidget")

        # Finalization
        self.preview_layout.addWidget(self.preview_content_widget, 0, 0, 1, 1)
        self.preview_dock_widget.setWidget(self.preview_widget)
        parent_widget.addDockWidget(QtCore.Qt.DockWidgetArea(2), self.preview_dock_widget)

    def retranslate_ui(self):
        _translate = QtCore.QCoreApplication.translate
        self.preview_dock_widget.setWindowTitle(_translate("MainWindow", "Markdown preview"))
