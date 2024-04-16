import sqlite3

class DatabaseCreator():
    def __init__(self):
        self.db_name = "noteAppDataBase"

    def create_database(self):
        conn = sqlite3.connect(self.db_name)
        conn.close()

    def create_Users_table(self):
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        try:
            cursor.execute("""CREATE TABLE IF NOT EXISTS Users (
                            id INTEGER PRIMARY KEY,
                            login TEXT NOT NULL,
                            password TEXT NOT NULL,
                           )""")
        except sqlite3.Error as error:
            print("Error creating Users table", error)

        conn.commit()
        conn.close()

    def create_UsersNotes_table(self):
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        try:
            cursor.execute("""CREATE TABLE IF NOT EXISTS Users (
                            id INTEGER PRIMARY KEY,
                            user_id INTEGER NOT NULL,
                            text TEXT NOT NULL,
                            date TEXT NOT NULL,
                           )""")
        except sqlite3.Error as error:
            print("Error creating UsersNotes table", error)
            
        conn.commit()
        conn.close()
