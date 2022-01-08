from PyQt5.QtCore import Qt
from PyQt5.QtGui import QCursor, QIcon
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QTabWidget, QPushButton, QMessageBox, QLineEdit, QHBoxLayout

from css import PushButtonStyle
from toDoList import ToDoList
from db.db_controller import *

class TabsController(QWidget):
    def __init__(self):
        super().__init__()
        self.dbController = DbController("to_do.db")
        #self.lists_layout_items = []
        self.projects_list = []
        self.projects_object_list = []
        self.projects_id_list = []
        self.count = 0


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
        self.tabs = QTabWidget()
        self.tabs.setTabsClosable(True)
        self.tabs.tabCloseRequested.connect(self.onTabCloseRequested)

        # Add tabs to widget
        self.layout.addWidget(self.tabs)
        self.setLayout(self.layout)

        # Action of Button to add To do list
        self.buttonAddList.clicked.connect(self.insertTab)


        self.get_projects_list()
        self.fill_projects_list()
        self.fill_tabs_layout()

        for i in range(len(self.projects_id_list)):
            for entry in self.projects_id_list:
                self.tabs.widget(i).titleElements.buttonTitle.clicked.connect(lambda: self.changeTitle(entry))



    def get_projects_list(self):
        for entry in self.dbController.get_all_projects():
            self.projects_list.append(entry)
            self.projects_id_list.append(entry[0])

    def fill_projects_list(self):
        for entry in self.projects_list:
            self.projects_object_list.append((entry[0], entry[1], ToDoList(500, 800, entry[0]))) # entry[0]=list_id # entry[1]=title

    def fill_tabs_layout(self):
        count = 0
        for entry in self.projects_object_list:
            self.tabs.addTab(entry[2], entry[1])
            self.tabs.setTabIcon(count, QIcon('Images/logo.png'))
            count += 1

    def insertTab(self):
        if self.tabs.count() <= 5:
            text = self.labelTitle.text()
            # Check if a title was written or not
            if text != "":
                if len(self.projects_id_list) !=0:
                    for i in self.projects_id_list:
                        if i == self.projects_id_list[-1]:
                            count = self.projects_id_list[-1] + 1
                else:
                    count = 0
                # Create instance of ToDoList class
                toDoListTab = ToDoList(500, 800, count)
                # Create project in database
                self.dbController.add_project(text, count)
                self.projects_id_list.append(count)
                # Add Tab to Tabs Widget
                self.tabs.addTab(toDoListTab, text)
                # Set Icon for the tabs
                self.tabs.setTabIcon(self.tabs.count()-1, QIcon('Images/logo.png'))
                # Clear th label of title
                self.labelTitle.clear()
            else:
                QMessageBox.warning(self, "Warning!", "You must enter a title.")

            if self.tabs.count() == 5:
                self.buttonAddList.setEnabled(False)

    def onTabCloseRequested(self, index):
        for entry in self.projects_id_list:
            if entry == self.tabs.widget(index).list_id:
                self.dbController.delete_project_and_tasks(entry)
                self.projects_id_list.remove(entry)
                self.tabs.widget(index).deleteLater()
                self.tabs.removeTab(entry)
        # Create only five lists
        if self.tabs.count() < 5:
            self.buttonAddList.setEnabled(True)

    def changeTitle(self, index):
        print(index)
        text = self.tabs.widget(index).titleElements.addTitle()

        self.tabs.setTabText(index, text)