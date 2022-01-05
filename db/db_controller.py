import sqlite3
from datetime import datetime


class DbController:
    def __init__(self, db_name):
        self.db_name = db_name

    def query(self, sql, data):
        with sqlite3.connect(self.db_name) as db:
            cursor = db.cursor()
            cursor.execute("PRAGMA Foreign_Keys = ON")
            cursor.execute(sql, data)
            db.commit()

    def select_query(self, sql, data=None):
        with sqlite3.connect(self.db_name) as db:
            cursor = db.cursor()
            cursor.execute("PRAGMA Foreign_Keys = ON")
            if data:
                cursor.execute(sql, data)
            else:
                cursor.execute(sql)
            results = cursor.fetchall()
        return results

    def add_task(self, description, table_id):
        add_task_sql = "INSERT INTO Tasks (Description, ProjectID) VALUES (?,?)"
        self.query(add_task_sql, (description, table_id, ))

    def get_all_tasks(self, project_id):
        results = self.select_query("SELECT * FROM Tasks WHERE ProjectID = ?", (project_id,))
        return results

    def delete_task_by_id(self, task_id):
        self.query("DELETE FROM Tasks WHERE TaskID = ?", (task_id,))

    def delete_project_and_tasks(self, project_id):
        self.query("DELETE FROM Tasks WHERE ProjectID = ?", (project_id,))
        self.query("DELETE FROM Projects WHERE ProjectID = ?", (project_id,))

    def add_project(self, title, project_id):
        created = datetime.now()
        sql_add_project =  "INSERT INTO Projects (ProjectID, Title, Created) VALUES (?,?,?)"
        self.query(sql_add_project, (project_id, title, created,))
        return project_id

    def get_all_projects(self):
        results = self.select_query("SELECT * FROM Projects")
        return results