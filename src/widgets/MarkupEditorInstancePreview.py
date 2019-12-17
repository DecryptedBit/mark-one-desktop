import mistune
from PyQt5 import QtCore, QtWidgets, QtWebEngineWidgets


class MarkupEditorPreviewInstanceUI(object):
    def setup_ui(self):
        # Preview content
        self.preview_web_engine_widget = QtWebEngineWidgets.QWebEngineView()
        self.preview_web_engine_widget.setObjectName("PreviewWebEngineWidget")
        self.preview_web_engine_widget.setHtml("<h1>This is some test HTML</h1>")

    def add_to_grid_Layout(self, layout, row, column):
        self.dock_widget = None

        layout.addWidget(self.preview_web_engine_widget, row, column, 1, 1)

    def add_to_dock_widget(self, main_window):
        self.dock_widget = main_window

        # Preview dock widget master
        self.dock_widget = QtWidgets.QDockWidget(main_window)
        self.dock_widget.setStyleSheet("")
        self.dock_widget.setObjectName("PreviewDockWidget")

        # Finalization
        self.dock_widget.setWidget(self.preview_web_engine_widget)
        main_window.addDockWidget(QtCore.Qt.DockWidgetArea(2), self.dock_widget)

    def retranslate_ui(self):
        _translate = QtCore.QCoreApplication.translate

        if self.dock_widget is not None:
            self.dock_widget.setWindowTitle(_translate("MainWindow", "Markup preview"))
