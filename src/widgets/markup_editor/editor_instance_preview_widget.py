from PyQt5.QtWebEngineWidgets import QWebEngineView


class EditorPreviewInstanceWidget(QWebEngineView):
    def __init__(self, parent=None):
        super(EditorPreviewInstanceWidget, self).__init__(parent)

    def update_content(self, content):
        self.setHtml(content)
