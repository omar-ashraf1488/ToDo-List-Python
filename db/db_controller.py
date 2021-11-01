import sqlite3


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

    def add_task(self, description):
        add_task_sql = "INSERT INTO Tasks (Description) VALUES (?)"
        self.query(add_task_sql, (description,))

    def get_all_tasks(self):
        results = self.select_query("SELECT * FROM Tasks")
        return results

    def delete_task_by_id(self, task_id):
        self.query("DELETE FROM Tasks WHERE TaskID = ?", (task_id,))
