from PyQt5 import QtCore, QtGui, QtWidgets
import mistune


class MarkupEditorUI(object):
    def setup_ui(self, markup_editor_parent_widget):
        markup_editor_parent_widget.setObjectName("markupEditorWidget")

        self.markupEditorWidget = QtWidgets.QWidget(markup_editor_parent_widget)
        self.markupEditorWidget.setObjectName("mainLayoutWidget")

        self.mainLayout = QtWidgets.QGridLayout(self.markupEditorWidget)
        self.mainLayout.setContentsMargins(0, 0, 0, 0)
        self.mainLayout.setSpacing(3)
        self.mainLayout.setObjectName("mainLayout")

        self.tabWidget = QtWidgets.QTabWidget(self.markupEditorWidget)
        self.tabWidget.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.tabWidget.setAutoFillBackground(False)
        self.tabWidget.setStyleSheet("")
        self.tabWidget.setTabPosition(QtWidgets.QTabWidget.North)
        self.tabWidget.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.tabWidget.setElideMode(QtCore.Qt.ElideMiddle)
        self.tabWidget.setUsesScrollButtons(True)
        self.tabWidget.setDocumentMode(True)
        self.tabWidget.setTabsClosable(True)
        self.tabWidget.setMovable(True)
        self.tabWidget.setTabBarAutoHide(True)
        self.tabWidget.setObjectName("tabWidget")

        # TEMPORARY
        self.markupEditorTabWidget = QtWidgets.QWidget()
        self.markupEditorTabWidget.setEnabled(True)
        self.markupEditorTabWidget.setObjectName("editorTabWidget")

        # TEMPORARY
        self.markupEditorTabWidget_2 = QtWidgets.QWidget()
        self.markupEditorTabWidget_2.setEnabled(True)
        self.markupEditorTabWidget_2.setObjectName("editorTabWidget_2")

        # TEMPORARY
        self.gridLayout_1 = QtWidgets.QGridLayout(self.markupEditorTabWidget)
        self.gridLayout_1.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_1.setObjectName("gridLayout_3")

        # TEMPORARY
        self.textEdit = QtWidgets.QTextEdit(self.markupEditorTabWidget)
        self.textEdit.setStyleSheet("")
        self.textEdit.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.textEdit.setFrameShadow(QtWidgets.QFrame.Plain)
        self.textEdit.setLineWidth(1)
        self.textEdit.setObjectName("textEdit")
        self.gridLayout_1.addWidget(self.textEdit, 0, 0, 1, 1)

        # https://pypi.org/project/mistune/
        self.markdown = mistune.Markdown()
        self.textEdit.append(self.markdown('# I am using the mistune markdown parser \n\n ## Cool stuff! \n\n **Lets see if this works**'))

        # TEMPORARY
        self.tabWidget.addTab(self.markupEditorTabWidget, "Tab 1")
        self.tabWidget.addTab(self.markupEditorTabWidget_2, "Tab 2")

        self.mainLayout.addWidget(self.tabWidget, 0, 0, 1, 1)
        markup_editor_parent_widget.setCentralWidget(self.tabWidget)

        self.retranslate_ui(markup_editor_parent_widget)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(markup_editor_parent_widget)

    def retranslate_ui(self, editor_widget):
        _translate = QtCore.QCoreApplication.translate
        editor_widget.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.markupEditorTabWidget), _translate("MainWindow", "Tab 1"))
