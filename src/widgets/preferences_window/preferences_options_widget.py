from PyQt5.QtWidgets import QTabWidget


class PreferencesOptionsWidget(QTabWidget):
    def __init__(self, parent=None):
        super(PreferencesOptionsWidget, self).__init__(parent)

        self.setContentsMargins(0, 0, 0, 0)
        self.setTabsClosable(False)
        self.tabBar().setHidden(True)
        self.setStyleSheet("QTabWidget::pane { border: 0; }")

    def add_option_widget(self, widget, name):
        self.addTab(widget, name)

    def add_option_widgets(self, widgets, names):
        for widget, name in zip(widgets, names):
            self.add_option_widget(widget, name)

        self.setCurrentIndex(0)
