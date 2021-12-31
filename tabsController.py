from PyQt5.QtCore import Qt
from PyQt5.QtGui import QCursor
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QTabWidget, QMessageBox, QPushButton, QLineEdit, QHBoxLayout

from css import LineEditStyle, PushButtonStyle
from toDoList import ToDoList


class TabsController(QWidget):
    def __init__(self):
        super().__init__()

        self.buttonAddList = QPushButton("Add List")
        self.buttonAddList.setStyleSheet(PushButtonStyle + """QPushButton{
                                            margin: 0 150px 0 150px;
                                            }
                                            """)
        self.buttonAddList.setCursor(QCursor(Qt.PointingHandCursor))

        self.layout = QVBoxLayout()
        self.layout.addWidget(self.buttonAddList)



        # Initialize tab screen
        self.tabs = QTabWidget()

        self.toDoList = ToDoList(500, 800)

        # Title
        self.labelTitle = QLineEdit()
        self.buttonTitle = QPushButton("Add Title")

        self.labelTitle.setStyleSheet(LineEditStyle)
        self.buttonTitle.setStyleSheet(PushButtonStyle)
        self.buttonTitle.setCursor(QCursor(Qt.PointingHandCursor))

        self.labelTitle.setPlaceholderText("Title")

        self.title_layout1 = QHBoxLayout()
        self.title_layout1.addWidget(self.labelTitle)
        self.title_layout1.addWidget(self.buttonTitle)

        self.title_widget = QWidget()
        self.title_widget.setLayout(self.title_layout1)

        # Add tabs to widget
        self.layout.addWidget(self.tabs)
        self.setLayout(self.layout)

        # Action of Button to add Title
        self.buttonTitle.clicked.connect(self.addTitle)
        self.buttonAddList.clicked.connect(self.insertTab)

    def addTitle(self):
        text = self.labelTitle.text()
        if text != "":
            self.tabs.setTabText(0, text) #Bug!
            if self.buttonTitle.text() == "Change the Title":
                self.buttonTitle.setText("Add Title")
                self.labelTitle.setReadOnly(False)
                self.labelTitle.setAlignment(Qt.AlignLeft)

            elif self.buttonTitle.text() == "Add Title":
                self.buttonTitle.setText("Change the Title")
                self.labelTitle.setReadOnly(True)
                self.labelTitle.setAlignment(Qt.AlignCenter)

        else:
            QMessageBox.warning(self, "Warning!", "You must enter a title.")

    def insertTab(self):
        if self.tabs.count() <= 4:
            self.tab = QWidget()
            self.tabs.addTab(self.tab, "New Tab")
            # Create first tab
            self.tab.layout = QVBoxLayout(self)
            self.tab.layout.addWidget(self.title_widget)
            self.tab.layout.addWidget(self.toDoList)
            self.tab.setLayout(self.tab.layout)

            if self.tabs.count() == 4:
                self.buttonAddList.setEnabled(False)
