from PyQt5.QtWidgets import *
import sys
import os

from task import TaskElements
from title import TitleElements

from db.create_db import create_db
from db.db_controller import DbController


class main_window(QMainWindow):
    def __init__(self, width, height):
        super().__init__()
        self.width = width
        self.height = height
        self.dbController = DbController("to_do.db")
        # self.controller.db_name = "to_do.db"
        self.tasksIdDescriptionList = []
        self.tasks_object_list = []
        self.tasks_layout_items = []

        self.setWindowTitle("To do List")
        self.setGeometry(0, 0, self.width, self.height)

        self.titleElementsObject = TitleElements(self.height)

        self.buttonAddTask = QPushButton("Add Task")
        self.lineEditAddTask = QLineEdit()

        self.buttonAddTask.clicked.connect(self.addTask)

        self.initUI(self.width, self.height)  # Initialize the UI

    def get_tasks_list(self):
        for entry in self.dbController.get_all_tasks():
            self.tasksIdDescriptionList.append(entry)

    def initUI(self, width, height):
        self.get_tasks_list()

        # Horizontal box layout objects
        self.titleElementsWidget = QWidget()
        self.titleElementsWidget.setLayout(self.titleElementsObject.titleLayout)

        # scroll area widget contents - layout
        self.tasksLayout = QFormLayout()

        for entry in self.tasksIdDescriptionList:
            self.tasks_object_list.append(
                (entry[0], TaskElements(entry[1], self.height, self.width, entry[0], self.removeTask)))

        for entry in self.tasks_object_list:
            self.tasksLayout.addRow(entry[1].taskLayout)
            layoutObject = self.tasksLayout.children()[self.tasksLayout.count() - 1]
            self.tasks_layout_items.append((entry[0], layoutObject))  # entry[0] is taskID
            print(self.tasks_layout_items)

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
        self.mainLayout.addWidget(self.titleElementsWidget)
        self.mainLayout.addWidget(self.scrollArea)
        self.mainLayout.addWidget(self.addTaskWidget)

        self.mainWidget = QWidget()
        self.mainWidget.setLayout(self.mainLayout)

        self.setCentralWidget(self.mainWidget)

    def removeTask(self, task_id):
        for layout_item in self.tasks_layout_items:
            if layout_item[0] == task_id:
                print("here")
                self.tasksLayout.removeWidget(layout_item[1])  # layout_item[1] is the layoutObject
                self.dbController.delete_task_by_id(task_id)

    def addTask(self):
        text = self.lineEditAddTask.text()
        if text != "":
            self.dbController.add_task(text)
            self.get_tasks_list()
            self.lineEditAddTask.clear()

            task = TaskElements(text, self.height, self.width)
            self.tasksLayout.addRow(task.taskLayout)
            layoutObject = self.tasksLayout.children()[-1]
            print(layoutObject)
            self.tasks_layout_items.append((self.tasksLayout.count(), layoutObject))
        else:
            QMessageBox.warning(self, "Warning!", "You must enter a task.")

    # Actions of checkbox functions
    def checkBoxtaskChecked(self, checkBox, lineEdit):
        if checkBox.isChecked():
            lineEdit.setDisabled(True)
        else:
            lineEdit.setDisabled(False)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    main = main_window(500, 800)
    main.show()

    if not os.path.exists("to_do.db"):
        create_db("to_do.db")
        new_db = QMessageBox()
        new_db.setWindowTitle("New Database")
        new_db.setText("New database created")
        new_db.exec_()

    sys.exit(app.exec())
