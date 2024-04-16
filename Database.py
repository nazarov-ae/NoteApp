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
            cursor.execute("SELECT login FROM Users")
        except sqlite3.Error as error:
            print("Error selecting login from users table", error)

        flag = False

        rows = cursor.fetchall()
        conn.close()

        for row in rows:
            if row[0] == login:
                flag = True

        return flag

    def check_password_is_correct(self, login, password):
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()

        try:
            cursor.execute("SELECT login, password FROM Users")
        except sqlite3.Error as error:
            print("Error selecting login and password from users table", error)

        flag = False

        rows = cursor.fetchall()
        conn.close()

        for row in rows:
            if row[0] == login:
                if row[1] == password:
                    flag = True

        return flag

    def get_user_id(self, login):
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        id_of_user = 0

        try:
            cursor.execute("SELECT id, login FROM Users")
        except sqlite3.Error as error:
            print("Error selecting login and id from users table", error)


        rows = cursor.fetchall()
        conn.close()

        for row in rows:
            if row[1] == login:
                id_of_user = row[0]

        return id_of_user

    def add_note_in_UsersNotes_table(self, login, note, date):
        user_id = self.get_user_id(login)
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()

        sql_query = """INSERT INTO UsersNotes (user_id, text, date) VALUES (?, ?, ?)"""
        note_data = (user_id, note, date)

        print(date)

        try:
            cursor.execute(sql_query, note_data)
        except sqlite3.Error as error:
            print("Error added note in UsersNote", error)

        conn.commit()
        conn.close()

    def get_all_notes_of_User(self, login, search_filter):
        user_id = self.get_user_id(login)
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()

        sql_query = """SELECT id, text, date FROM UsersNotes
        WHERE user_id=? AND text LIKE ?"""
        note_data = (user_id, f"%{search_filter}%" if search_filter else "%")

        try:
            cursor.execute(sql_query, note_data)
        except sqlite3.Error as error:
            print("Error getting all notes of User", error)

        rows = cursor.fetchall()

        conn.commit()
        conn.close()
        return rows

    def add_User_in_Users_table(self, login, password):
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()

        sql_query = """INSERT INTO Users (login, password) VALUES (?, ?)"""
        user_data = (login, password)

        try:
            cursor.execute(sql_query, user_data)
        except sqlite3.Error as error:
            print("Error added user in Users table", error)

        conn.commit()
        conn.close()
