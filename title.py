from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *


class TitleElements(QWidget):
    def __init__(self, height):
        self.height = height
        super().__init__()

        # Title
        self.title = QLabel('To Do List')
        self.labelTitle = QLineEdit()
        self.buttonTitle = QPushButton("Add Title")

        self.title.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        self.title.setFont(QFont("Arial"))
        self.labelTitle.setPlaceholderText("Title")
        self.title.setStyleSheet(
            'font-size:{0}px; font-weight:bold; text-align: center; color:black; border-style:none;'.format(
                int(height / 12)))

        self.title_layout1 = QHBoxLayout()
        self.title_layout1.addWidget(self.labelTitle)
        self.title_layout1.addWidget(self.buttonTitle)

        self.title_widget = QWidget()
        self.title_widget.setLayout(self.title_layout1)

        self.titleLayout = QVBoxLayout()
        self.titleLayout.addWidget(self.title)
        self.titleLayout.addWidget(self.title_widget)

        # Action of Button to add Title
        self.buttonTitle.clicked.connect(self.addTitle)

    def addTitle(self):
        print("add title")
        self.buttonTitle.setText("Change the Title")
