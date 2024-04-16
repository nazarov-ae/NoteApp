import pretty_errors
from Model import Model

class ViewModel():
    def __init__(self, model: Model) -> None:
        self.model = model

    def change_users_info(self, login, password):
        self.model.user.login = login
        self.model.user.password = password

    def change_selected_note(self):
        pass

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
