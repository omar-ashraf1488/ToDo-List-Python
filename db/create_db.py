import sqlite3


def create_db(db_name):
    with sqlite3.connect(db_name) as db:
        cursor = db.cursor()
        cursor.execute("""CREATE TABLE Tasks(
                                    TaskID integer,
                                    Description text,
                                    ProjectID integer,
                                    PRIMARY KEY(TaskID),
                                    FOREIGN KEY(ProjectID) REFERENCES Projects(ProjectID)
                                    );""")

        cursor.execute("""CREATE TABLE Projects(
                            ProjectID integer,
                            Title TEXT NOT NULL,
                            Created timestamp,
                            PRIMARY KEY(ProjectID)
                            );""")



        db.commit()

