from PyQt5.QtWidgets import QWidget, QVBoxLayout, QTabWidget

from toDoList import ToDoList


class TabsController(QWidget):
    def __init__(self, titleList="tab1"):
        super().__init__()

        self.titleList = titleList
        self.layout = QVBoxLayout()

        # Initialize tab screen
        self.tabs = QTabWidget()
        self.tab1 = QWidget()
        self.tab2 = QWidget()


        # Add tabs
        self.tabs.addTab(self.tab1, "Tab 1")
        self.tabs.addTab(self.tab2, "Tab 2")

        self.toDoList1 = ToDoList(500, 800, self.titleList)
        self.toDoList2 = ToDoList(500, 800)

        self.tabs.setTabText(0, self.titleList)


        # Create first tab
        self.tab1.layout = QVBoxLayout(self)
        self.tab1.layout.addWidget(self.toDoList1)
        self.tab1.setLayout(self.tab1.layout)

        # Create second tab
        self.tab2.layout = QVBoxLayout(self)
        self.tab2.layout.addWidget(self.toDoList2)
        self.tab2.setLayout(self.tab2.layout)

        # Add tabs to widget
        self.layout.addWidget(self.tabs)
        self.setLayout(self.layout)