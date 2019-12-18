from PyQt5 import QtCore, QtWidgets


class FileExplorer(object):
    def setup_ui(self, main_window):
        # Dock layout
        self.dock_widget = QtWidgets.QDockWidget(main_window)
        self.dock_widget.setFeatures(QtWidgets.QDockWidget.AllDockWidgetFeatures)
        self.dock_widget.setObjectName("FileExplorerDockWidget")

        # Tree view widget
        self.tree_view_widget = QtWidgets.QTreeView()
        self.tree_view_widget.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.tree_view_widget.setObjectName("FileExplorerTreeView")
        self.tree_view_widget.header().setVisible(True)
        self.dock_widget.setWidget(self.tree_view_widget)

        # Tree layout
        self.tree_view_layout = QtWidgets.QGridLayout(self.tree_view_widget)
        self.tree_view_layout.setContentsMargins(3, 3, 3, 3)
        self.tree_view_layout.setObjectName("FileExplorerTreeLayout")
        self.tree_view_layout.addWidget(self.tree_view_widget, 0, 0, 1, 1)

        # Finalization
        self.retranslate_ui()
        main_window.addDockWidget(QtCore.Qt.DockWidgetArea(1), self.dock_widget)

        QtCore.QMetaObject.connectSlotsByName(self.tree_view_widget)

    def retranslate_ui(self):
        _translate = QtCore.QCoreApplication.translate
        self.dock_widget.setWindowTitle(_translate("MainWindow", "File explorer"))
