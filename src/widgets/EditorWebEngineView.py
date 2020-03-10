from PyQt5.QtWebEngineWidgets import QWebEngineView


class EditorWebEngineView(QWebEngineView):
    def __init__(self, parent=None):
        super(EditorWebEngineView, self).__init__(parent)

    def update_content(self, content):
        self.setHtml(content)
