from PyQt5 import QtCore
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QCursor, QIcon
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QTabWidget, QPushButton, QMessageBox, QLineEdit, QHBoxLayout

from css import PushButtonStyle
from toDoList import ToDoList

class TabsController(QWidget):
    def __init__(self):
        super().__init__()
        self.lists_layout_items = []

        self.labelTitle = QLineEdit()
        self.buttonAddList = QPushButton("Add List")
        self.buttonAddList.setStyleSheet(PushButtonStyle)
        """QPushButton{
        margin: 0 150px 0 150px;
        }
        """
        self.buttonAddList.setCursor(QCursor(Qt.PointingHandCursor))

        # Widget of Button and Label
        self.labelButtonLayout = QHBoxLayout()
        self.labelButtonLayout.addWidget(self.labelTitle)
        self.labelButtonLayout.addWidget(self.buttonAddList)
        self.labelButtonWidget = QWidget()
        self.labelButtonWidget.setLayout(self.labelButtonLayout)

        # Main Layout of this Class
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.labelButtonWidget)

        # Initialize tab screen
        self.tabs = QTabWidget(tabsClosable=True)

        # Add tabs to widget
        self.layout.addWidget(self.tabs)
        self.setLayout(self.layout)

        # Action of Button to add To do list
        self.buttonAddList.clicked.connect(self.insertTab)


    def insertTab(self):
        if self.tabs.count() <= 5:
            text = self.labelTitle.text()

            # Check if a title was written or not
            print(self.tabs.count())
            if text != "":
                self.labelTitle.setReadOnly(False)
                self.labelTitle.setAlignment(Qt.AlignLeft)

                toDoList = ToDoList(500, 800, self.tabs.count())
                self.tabs.addTab(toDoList, text)
                print(self.tabs.count())
                self.tabs.setTabIcon(self.tabs.count()-1, QIcon('Images/logo.png'))
                self.tabs.tabCloseRequested.connect(self.onTabCloseRequested)

                layoutObject = toDoList
                self.lists_layout_items.append((self.tabs.count(), layoutObject))
                self.labelTitle.clear()

            else:
                QMessageBox.warning(self, "Warning!", "You must enter a title.")

            # Create an instance of To Do List
            #toDoList = ToDoList(500, 800, self.tabs.count() + 1)
            #self.tabs.addTab(toDoList, "New List")
            #title = toDoList.titleElements.addTitle()
            #print("the title is "+ str(title))
            #toDoList.titleElements.buttonTitle.clicked.connect(lambda: self.changeTitleName(self.tabs.count()-1,title))
            #layoutObject = toDoList
            #self.lists_layout_items.append((self.tabs.count(), layoutObject))
            #title = toDoList.titleElements.addTitle

            if self.tabs.count() == 5:
                self.buttonAddList.setEnabled(False)

    @QtCore.pyqtSlot(int)
    def onTabCloseRequested(self, index):
        # gets the widget
        widget = self.tabs.widget(index)

        # if the widget exists
        if widget:
            # removes the widget
            widget.deleteLater()

        # removes the tab of the QTabWidget
        self.tabs.removeTab(index)

'''
    def test(self):
        for i in range(len(self.lists_layout_items)):
            print(i)
            a, b = self.lists_layout_items[i]
            text = b.titleElements.labelTitle.text()
            text = b.titleElements.updateTitle(text)
            #text="heloo"

            print("titel is: "+str(text))
            if text !="":
                b.titleElements.buttonTitle.clicked.connect(lambda: self.changeTitleName(i, text))

    def changeTitleName(self, tabNumber, title):
        self.tabs.setTabText(tabNumber, title)
'''