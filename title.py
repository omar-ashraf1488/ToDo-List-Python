from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

from css import PushButtonStyle, LineEditStyle

class TitleElements(QWidget):
    def __init__(self):
        super().__init__()

        # Title
        self.labelTitle = QLineEdit()
        self.buttonTitle = QPushButton("Add List")

        self.labelTitle.setStyleSheet(LineEditStyle)
        self.buttonTitle.setStyleSheet(PushButtonStyle)
        self.buttonTitle.setCursor(QCursor(Qt.PointingHandCursor))

        self.labelTitle.setPlaceholderText("Title")


        self.title_layout1 = QHBoxLayout()
        self.title_layout1.addWidget(self.labelTitle)
        self.title_layout1.addWidget(self.buttonTitle)

        self.title_widget = QWidget()
        self.title_widget.setLayout(self.title_layout1)

        self.mainLayout = QVBoxLayout()
        self.mainLayout.addWidget(self.title_widget)

        self.setLayout(self.mainLayout)

        # Action of Button to add Title
        self.buttonTitle.clicked.connect(self.addTitle)


    def addTitle(self):
        text = self.labelTitle.text()
        if text != "":
            #self.tabs.setTabText(0, text)  # Bug!
            if self.buttonTitle.text() == "Change the Title":
                self.buttonTitle.setText("Add Title")
                self.labelTitle.setReadOnly(False)
                self.labelTitle.setAlignment(Qt.AlignLeft)

            elif self.buttonTitle.text() == "Add Title":
                self.buttonTitle.setText("Change the Title")
                self.labelTitle.setReadOnly(True)
                self.labelTitle.setAlignment(Qt.AlignCenter)
            return  text
        else:
            QMessageBox.warning(self, "Warning!", "You must enter a title.")




