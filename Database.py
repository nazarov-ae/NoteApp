import sqlite3

class Database():
    def __init__(self):
        self.db_name = "noteAppDataBase"
        self.create_database()
        self.create_Users_table()
        self.create_UsersNotes_table()

    def create_database(self):
        # conn = sqlite3.connect(self.db_name) повторяется во всех методах.
        # Как вариант можно сделать self.conn = sqlite3.connect(self.db_name)
        # в __init__ и обращаться далее к нему. Или лучше сразу курсор, так
        # как общаешься с базой именно через него.
        conn = sqlite3.connect(self.db_name)
        conn.close()

    def create_Users_table(self):
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        try:
            # Если в QT есть возможность вместо SQL делать запросы через
            # python-объекты, то это надо использовать.
            # Почитай про ORM.
            # Похоже, что тебе надо создать таблицу, только если ее нет, а
            # не каждый раз.
            cursor.execute("""CREATE TABLE IF NOT EXISTS Users (
                            id INTEGER PRIMARY KEY,
                            login TEXT NOT NULL,
                            password TEXT NOT NULL
                           )""")
            conn.commit()
        except sqlite3.Error as error:
            # Это сообщение должно быть записано в логи и должно быть выведено
            # пользователю, желательно в понятном ему виде.
            print("Error creating Users table", error)

        # Каждый раз открывать/закрывать соединение с базой не надо.
        # Открыли при создании класса и работаем с ним.
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
            conn.commit()
        except sqlite3.Error as error:
            print("Error creating UsersNotes table", error)

        conn.close()

    def check_login_is_registered(self, login):
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()

        try:
            cursor.execute("SELECT login FROM Users")
            conn.commit()
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
            conn.commit()
        except sqlite3.Error as error:
            print("Error selecting login and password from users table", error)

        flag = False

        # Здесь приложение упадет, если до этого будет ошибка qlite3.Error
        rows = cursor.fetchall()
        conn.close()

        # Это можно сделать напрямую с помощью SQL.
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
            conn.commit()
        except sqlite3.Error as error:
            print("Error selecting login and id from users table", error)

        # Здесь приложение упадет, если до этого будет ошибка qlite3.Error
        rows = cursor.fetchall()
        conn.close()

        # Это можно сделать напрямую с помощью SQL.
        for row in rows:
            if row[1] == login:
                id_of_user = row[0]

        return id_of_user

        # # В итоге все методы можно свести к подобному виду:
        # query = ''
        # try:
        #     self.cursor.execute(query)
        #     return conn.commit()
        # except sqlite3.Error as error:
        #     # Пишем логи и прокидываем исключение дальше. Ловим и обрабатываем
        #     # в ViewModel.
        #     raise

    def add_note_in_UsersNotes_table(self, login, note, date):
        user_id = self.get_user_id(login)
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()

        sql_query = """INSERT INTO UsersNotes (user_id, text, date) VALUES (?, ?, ?)"""
        note_data = (user_id, note, date)

        print(date)

        try:
            cursor.execute(sql_query, note_data)
            conn.commit()
        except sqlite3.Error as error:
            print("Error added note in UsersNote", error)

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
            conn.commit()
        except sqlite3.Error as error:
            print("Error getting all notes of User", error)

        rows = cursor.fetchall()

        conn.close()
        return rows

    def add_User_in_Users_table(self, login, password):
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()

        sql_query = """INSERT INTO Users (login, password) VALUES (?, ?)"""
        user_data = (login, password)

        try:
            cursor.execute(sql_query, user_data)
            conn.commit()
        except sqlite3.Error as error:
            print("Error added user in Users table", error)

        conn.close()

    def delete_note(self, note_id):
        print(note_id, type(note_id))
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()

        sql_query = "DELETE FROM UsersNotes WHERE id = ?"
        user_data = (str(note_id),)

        try:
            cursor.execute(sql_query, user_data)
            conn.commit()
        except sqlite3.Error as error:
            print("Error deleting note from UsersNotes", error)


        conn.close()

    def edit_note(self, note_id, note, date):
        print(note_id, type(note_id))
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()

        sql_query = "UPDATE UsersNotes SET text = ?, date = ? WHERE id = ?"
        user_data = (note, date, str(note_id))

        try:
            cursor.execute(sql_query, user_data)
            conn.commit()
        except sqlite3.Error as error:
            print("Error editing note from UsersNotes", error)

        conn.close()
