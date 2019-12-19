from PyQt5 import QtCore, QtWidgets, QtWebEngineWidgets


class EditorPreviewInstance(object):
    def setup_ui(self):
        self.dock_widget = None

        # Preview content
        self.preview_web_engine_widget = QtWebEngineWidgets.QWebEngineView()
        self.preview_web_engine_widget.setObjectName("PreviewWebEngineWidget")

        self.preview_web_engine_widget.setHtml("<h1>Preview markdown</h1>")

    def add_to_dock_widget(self, main_window):
        # Preview dock widget
        self.dock_widget = QtWidgets.QDockWidget(main_window)
        self.dock_widget.setFeatures(QtWidgets.QDockWidget.AllDockWidgetFeatures)
        self.dock_widget.setObjectName("PreviewDockWidget")

        # Finalization
        self.dock_widget.setWidget(self.preview_web_engine_widget)
        main_window.addDockWidget(QtCore.Qt.DockWidgetArea(2), self.dock_widget)

    def retranslate_ui(self):
        if self.dock_widget is not None:
            _translate = QtCore.QCoreApplication.translate
            self.dock_widget.setWindowTitle(_translate("MainWindow", "Markup preview"))

    def update_html(self, html):
        self.preview_web_engine_widget.setHtml(html)

    def get_widget(self):
        return self.preview_web_engine_widget
