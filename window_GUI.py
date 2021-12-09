from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import *
import sys
import os

from task import TaskElements
from title import TitleElements
from timer import Timer

from db.create_db import create_db
from db.db_controller import DbController



class MainWindow(QMainWindow):
    def __init__(self, width, height):
        super().__init__()
        self.width = width
        self.height = height
        self.dbController = DbController("to_do.db")
        self.tasksIdDescriptionList = []
        self.tasks_object_list = []
        self.tasks_layout_items = []


        self.setWindowIcon(QIcon('Images/logo.png'))
        self.setWindowTitle("To do List")
        self.setFixedSize(self.width, self.height)
        self.setGeometry(100, 100, self.width, self.height)

        self.titleElementsObject = TitleElements(self.height)
        self.timer = Timer()

        self.buttonAddTask = QPushButton("Add Task")
        self.lineEditAddTask = QLineEdit()

        self.buttonAddTask.clicked.connect(self.addTask)

        self.initUI()  # Initialize the UI

    def get_tasks_list(self):
        for entry in self.dbController.get_all_tasks():
            self.tasksIdDescriptionList.append(entry)

    def initUI(self):
        self.get_tasks_list()

        # scroll area widget contents - layout
        self.tasksLayout = QFormLayout()

        for entry in self.tasksIdDescriptionList:
            self.tasks_object_list.append((entry[0],
                                           TaskElements(entry[1], self.height, self.width, entry[0], self.removeTask)))

        for entry in self.tasks_object_list:
            self.tasksLayout.addRow(entry[1])
            layoutObject = self.tasksLayout  # .children()[self.tasksLayout.count() - 1]
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
        self.mainLayout.addWidget(self.titleElementsObject)
        self.mainLayout.addWidget(self.scrollArea)
        self.mainLayout.addWidget(self.timer)
        self.mainLayout.addWidget(self.addTaskWidget)

        self.mainWidget = QWidget()
        self.mainWidget.setLayout(self.mainLayout)

        self.setCentralWidget(self.mainWidget)

    def removeTask(self, task_id):
        for layout_item in self.tasks_layout_items:
            if layout_item[0] == task_id:
                self.tasksLayout.removeRow(layout_item[1])  # layout_item[1] is the layoutObject
                self.dbController.delete_task_by_id(task_id)

    def addTask(self):
        text = self.lineEditAddTask.text()
        if text != "":
            self.dbController.add_task(text)
            self.get_tasks_list()
            self.lineEditAddTask.clear()

            task = TaskElements(text, self.height, self.width, self.tasksLayout.count() + 1, self.removeTask)
            self.tasksLayout.addRow(task)  # task.taskLayout
            layoutObject = self.tasksLayout  # .children()[-1]
            self.tasks_layout_items.append((self.tasksLayout.count(), layoutObject))

        else:
            QMessageBox.warning(self, "Warning!", "You must enter a task.")

    def keyPressEvent(self, event):
        textAddTask = self.lineEditAddTask.text()
        textAddTitle = self.titleElementsObject.labelTitle.text()
        if textAddTask != "":
            if event.key() == Qt.Key_Return:
                self.addTask()
        elif textAddTitle != "" and self.titleElementsObject.buttonTitle.text() !="Change the Title":
            if event.key() == Qt.Key_Return:
                self.titleElementsObject.addTitle()


if __name__ == "__main__":
    app = QApplication(sys.argv)

    if not os.path.exists("to_do.db"):
        create_db("to_do.db")
        new_db = QMessageBox()
        new_db.setWindowTitle("New Database")
        new_db.setText("New database created")
        new_db.exec_()


    main = MainWindow(500, 800)
    main.show()

    sys.exit(app.exec())