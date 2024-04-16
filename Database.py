import sqlite3

class DatabaseCreator():
    def __init__(self):
        self.db_name = "noteAppDataBase"
        self.create_database()
        self.create_Users_table()
        self.create_UsersNotes_table()

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
                            password TEXT NOT NULL
                           )""")
        except sqlite3.Error as error:
            print("Error creating Users table", error)

        conn.commit()
        conn.close()

    def create_UsersNotes_table(self):
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        try:
            cursor.execute("""CREATE TABLE IF NOT EXISTS UsersNotes (
                            id INTEGER PRIMARY KEY,
                            user_id INTEGER NOT NULL,
                            text TEXT NOT NULL,
                            date TEXT NOT NULL
                           )""")
        except sqlite3.Error as error:
            print("Error creating UsersNotes table", error)

        conn.commit()
        conn.close()

    def check_login_is_registered(self, login):
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()

        try:
            cursor.execute("SELECT * FROM Users")
        except sqlite3.Error as error:
            print("Error selecting login from users table", error)

        flag = False

        rows = cursor.fetchall()
        conn.close()

        for row in rows:
            print(row)
            if row[1] == login:
                flag = True

        print(flag)
        return flag

    def add_User_in_Users_table(self, login, password):
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()

        sql_query = """INSERT INTO Users (login, password) VALUES (?, ?)"""
        user_data = (login, password)

        cursor.execute(sql_query, user_data)

        conn.commit()
        conn.close()
