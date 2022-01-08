from PyQt5.QtCore import Qt
from PyQt5.QtGui import QCursor
from PyQt5.QtWidgets import QWidget, QPushButton, QFormLayout, QScrollArea, QHBoxLayout, QVBoxLayout, QMessageBox, \
    QLineEdit

from css import PushButtonStyle, LineEditStyle
from db.db_controller import DbController
from task import TaskElements
from timer import Timer
from title import TitleElements



class ToDoList(QWidget):
    def __init__(self, width, height, list_id):
        super().__init__()
        self.titleElements = TitleElements()
        self.height = height
        self.width = width
        self.list_id = list_id

        self.dbController = DbController("to_do.db")
        self.tasksIdDescriptionList = []
        self.tasks_object_list = []
        self.tasks_layout_items = []


        self.timer = Timer()

        self.buttonAddTask = QPushButton("Add Task")
        self.buttonAddTask.setStyleSheet(PushButtonStyle)
        self.buttonAddTask.setCursor(QCursor(Qt.PointingHandCursor))

        self.lineEditAddTask = QLineEdit()
        self.lineEditAddTask.setStyleSheet(LineEditStyle)

        self.buttonAddTask.clicked.connect(self.addTask)

        self.initUI()  # Initialize the UI

    def get_tasks_list(self, list_id):
        for entry in self.dbController.get_all_tasks(list_id):
            self.tasksIdDescriptionList.append(entry)

    def initUI(self):
        self.get_tasks_list(self.list_id)

        # scroll area widget contents - layout
        self.tasksLayout = QFormLayout()

        for entry in self.tasksIdDescriptionList:
            self.tasks_object_list.append((entry[0],
                                           TaskElements(entry[1], self.height, self.width, entry[0], self.removeTask)))

        for entry in self.tasks_object_list:
            self.tasksLayout.addRow(entry[1])
            layoutObject = self.tasksLayout
            self.tasks_layout_items.append((entry[0], layoutObject))  # entry[0] is taskID

        self.tasksWidget = QWidget()
        self.tasksWidget.setLayout(self.tasksLayout)

        self.scrollArea = QScrollArea()
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setWidget(self.tasksWidget)

        self.addTaskLayout = QHBoxLayout()
        self.addTaskLayout.addWidget(self.buttonAddTask)
        self.addTaskLayout.addWidget(self.lineEditAddTask)

        self.addTaskWidget = QWidget()
        self.addTaskWidget.setLayout(self.addTaskLayout)

        self.mainLayout = QVBoxLayout()
        self.mainLayout.addWidget(self.titleElements)
        self.mainLayout.addWidget(self.scrollArea)
        self.mainLayout.addWidget(self.timer)
        self.mainLayout.addWidget(self.addTaskWidget)

        self.setLayout(self.mainLayout)

    def removeTask(self, task_id):
        for layout_item in self.tasks_layout_items:
            if layout_item[0] == task_id:
                self.tasksLayout.removeRow(layout_item[1])
                self.dbController.delete_task_by_id(task_id)

    def addTask(self):
        text = self.lineEditAddTask.text()
        if text != "":
            self.dbController.add_task(text, self.list_id)
            self.get_tasks_list(self.list_id)
            self.lineEditAddTask.clear()

            task = TaskElements(text, self.height, self.width, self.tasksLayout.count() + 1, self.removeTask)
            self.tasksLayout.addRow(task)
            layoutObject = self.tasksLayout
            self.tasks_layout_items.append((self.tasksLayout.count(), layoutObject))

        else:
            QMessageBox.warning(self, "Warning!", "You must enter a task.")

    def keyPressEvent(self, event):
        textAddTask = self.lineEditAddTask.text()
        textAddTitle = self.titleElements.labelTitle.text()
        if textAddTask != "":
            if event.key() == Qt.Key_Return:
                self.addTask()
        elif textAddTitle != "" and self.titleElements.buttonTitle.text() != "Change the Title":
            if event.key() == Qt.Key_Return:
                self.titleElements.addTitle()

