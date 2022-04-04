import sys
from PySide2 import QtCore
from PySide2.QtWidgets import (QApplication, QMainWindow, QLabel, QLineEdit, QVBoxLayout, QHBoxLayout, QPushButton,
                               QWidget, QTextEdit)
from PySide2.QtCore import Qt, QEvent
from PySide2.QtGui import QKeyEvent
from howdoi import howdoi

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("How Do I?")

        self.input = QLineEdit()

        self.questionLabel = QLabel()
        self.questionLabel.setText("How do I:")

        self.answerTextBox = QTextEdit()
        self.answerTextBox.setAlignment(Qt.AlignTop)
        self.answerTextBox.setReadOnly(True)
        self.answerTextBox.setStyleSheet("background-color: #a6a6a6; color: #fff")

        self.askButton = QPushButton("Ask")
        self.askButton.clicked.connect(self.SubmitQuestion)

        askLayout = QHBoxLayout()
        askLayout.addWidget(self.questionLabel)
        askLayout.addWidget(self.input)
        askLayout.addWidget(self.askButton)

        self.questionLink = QLabel()
        self.askButton.clicked.connect(self.BuildLink)

        guiLayout = QVBoxLayout()
        guiLayout.addLayout(askLayout)
        guiLayout.addWidget(self.answerTextBox)
        guiLayout.addWidget(self.questionLink)

        guiContainer = QWidget()
        guiContainer.setMinimumSize(800, 400)
        guiContainer.setLayout(guiLayout)
        self.setCentralWidget(guiContainer)

    def keyPressEvent(self, event: QKeyEvent):
        if event.key() in (Qt.Key_Return, Qt.Key_Enter):
            self.askButton.click()

    def SubmitQuestion(self):
        question = self.input.text()
        if question != "":
            self.answerTextBox.setText(howdoi.howdoi(question))

    def BuildLink(self):
        queryText = self.input.text()
        if queryText != "":
            self.questionLink.setText("Show question on <a href=\"" + howdoi.howdoi(queryText + " -l") + "\">Stack Overflow</a>")
            self.questionLink.setOpenExternalLinks(True)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    app.exec_()
