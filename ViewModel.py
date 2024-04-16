import pretty_errors
from Model import Model

class ViewModel():
    def __init__(self, model: Model) -> None:
        self.model = model

    def change_users_info(self, login, password):
        self.model.user.login = login
        self.model.user.password = password

    def delete_note(self, note_id):
        self.model.database_creator.delete_note(note_id)

    def edit_note(self, note_id, note, date):
        self.model.database_creator.edit_note(note_id, note, date)

    def reset_selected_note(self):
        self.model.user.selectedNote.note_id = 0
        self.model.user.selectedNote.note = ""
        self.model.user.selectedNote.date = ""

    def change_selected_note(self, note_id, note, date):
        self.model.user.selectedNote.note_id = note_id
        self.model.user.selectedNote.note = note
        self.model.user.selectedNote.date = date

    def get_selected_note(self):
        return self.model.user.selectedNote

    def get_login_of_User(self):
        return self.model.user.login

    def get_password_of_User(self):
        return self.model.user.password

    def get_all_notes_of_User(self, login, search_filter):
        return self.model.database_creator.get_all_notes_of_User(login, search_filter)

    def add_note_in_UsersNotes_table(self, login, note, date):
        self.model.database_creator.add_note_in_UsersNotes_table(login, note, date)

    def check_login_is_registered(self, login):
        if self.model.database_creator.check_login_is_registered(login):
            return True
        else:
            return False

    def check_password_is_correct(self, login, password):
        if self.model.database_creator.check_password_is_correct(login, password):
            return True
        else:
            return False

    def add_user_in_Users_table(self, login, password):
        self.model.database_creator.add_User_in_Users_table(login, password)
