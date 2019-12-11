import sys
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtCore import QDir, QUrl

if __name__ == "__main__":
    sys.argv.append("--disable-web-security")
    app = QApplication(sys.argv)

    path = QDir.current().filePath('plotly-latest.min.js')
    local = QUrl.fromLocalFile(path).toString()

    raw_html = '<html><head><meta charset="utf-8" />'
    raw_html += '<script src="{}"></script></head>'.format(local)
    raw_html += '<body>'
    raw_html += '<h1>This is a test ya smuck!</h1>'
    raw_html += '</body></html>'

    view = QWebEngineView()
    view.setHtml(raw_html)

    view.show()
    sys.exit(app.exec_())
