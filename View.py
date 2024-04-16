from MainWindow import Ui_MainWindow
from AddNoteWindow import Ui_AddNoteWindow
from EditNoteWindow import Ui_EditNoteWindow
from LoginWindow import Ui_LoginWindow
from ViewModel import ViewModel
from PyQt6.QtWidgets import QMainWindow, QDialog
import pretty_errors

class MainWindowUI(Ui_MainWindow, QMainWindow):
    def __init__(self):
        super(Ui_MainWindow, self).__init__()
        super(QMainWindow, self).__init__()

class AddNoteWindowUI(Ui_AddNoteWindow, QDialog):
    def __init__(self):
        super(Ui_AddNoteWindow, self).__init__()
        super(QDialog, self).__init__()

class EditNoteWindowUI(Ui_EditNoteWindow, QDialog):
    def __init__(self):
        super(Ui_EditNoteWindow, self).__init__()
        super(QDialog, self).__init__()

class LoginWindowUI(Ui_LoginWindow, QDialog):
    def __init__(self):
        super(Ui_LoginWindow, self).__init__()
        super(QDialog, self).__init__()



class View():
    def __init__(self, viewModel: ViewModel) -> None:
        self.viewModel = viewModel
        self.main_Window = MainWindowUI()
        self.main_Window.setupUi(self.main_Window)

        self.add_note_window = AddNoteWindowUI()
        self.add_note_window.setupUi(self.add_note_window)

        self.edit_note_window = EditNoteWindowUI()
        self.edit_note_window.setupUi(self.edit_note_window)

        self.login_Window = LoginWindowUI()
        self.login_Window.setupUi(self.login_Window)
        self.login_Window.loginWarningLabel.setText("")
        self.login_Window.passwordWarningLabel.setText("")

        self.connect_all_events_of_buttons_in_MainWindow()
        self.connect_all_events_of_buttons_in_LoginWindow()
        self.connect_all_events_of_buttons_in_AddWindow()

        self.login_Window.show()

    #MainWindow
    def connect_all_events_of_buttons_in_MainWindow(self):
        self.main_Window.add_button.pressed.connect(lambda: self.add_button_in_MainWindow_is_pressed())
        self.main_Window.edit_button.pressed.connect(lambda: self.edit_button_in_MainWindow_is_pressed())

    def add_button_in_MainWindow_is_pressed(self):
        self.add_note_window.show()

    def edit_button_in_MainWindow_is_pressed(self):
        self.edit_note_window.show()

    #LoginWindow
    def connect_all_events_of_buttons_in_LoginWindow(self):
        self.login_Window.sign_up_button.pressed.connect(lambda: self.sign_up_button_in_LoginWindow_is_pressed())
        self.login_Window.sign_in_button.pressed.connect(lambda: self.sign_in_button_in_LoginWindow_is_pressed())

    def sign_in_button_in_LoginWindow_is_pressed(self):
        if self.check_loginLabelEdit_validation_is_passed():
            if self.check_passwordLabelEdit_validation_is_passed():
                pass

    def check_if_login_is_registered(self):
        if self.viewModel.check_login_is_registered():
            pass
        else:
            return False

    def sign_up_button_in_LoginWindow_is_pressed(self):
        if self.check_loginLabelEdit_validation_is_passed():
            if self.check_passwordLabelEdit_validation_is_passed():
                if self.viewModel.check_login_is_registered(self.login_Window.loginLabelEdit.text()):
                    self.login_Window.loginWarningLabel.setStyleSheet('color: red')
                    self.login_Window.loginWarningLabel.setText("This login is already used")
                else:
                    self.viewModel.add_user_in_Users_table(self.login_Window.loginLabelEdit.text(), self.login_Window.passwordLabelEdit.text())
                    self.login_Window.loginWarningLabel.setStyleSheet('color: green')
                    self.login_Window.loginWarningLabel.setText("Account is registered")

    def check_login_is_not_empty(self):
        if self.login_Window.loginLabelEdit.text() != "":
            self.login_Window.loginWarningLabel.setText("")
            return True
        else:
            self.login_Window.loginWarningLabel.setStyleSheet('color: red')
            self.login_Window.loginWarningLabel.setText("Please enter your login")
            return False

    def check_password_is_not_empty(self):
        if self.login_Window.passwordLabelEdit.text() != "":
            self.login_Window.passwordWarningLabel.setText("")
            return True
        else:
            self.login_Window.passwordWarningLabel.setStyleSheet('color: red')
            self.login_Window.passwordWarningLabel.setText("Please enter your password")
            return False

    def check_login_rules_are_followed(self):
        if len(self.login_Window.loginLabelEdit.text()) < 10:
            self.login_Window.loginWarningLabel.setText("")
            return True
        else:
            self.login_Window.loginWarningLabel.setStyleSheet('color: red')
            self.login_Window.loginWarningLabel.setText("Login must be less than 10 characters")
            return False

    def check_password_rules_are_followed(self):
        if len(self.login_Window.passwordLabelEdit.text()) > 8:
            self.login_Window.loginWarningLabel.setText("")
            return True
        else:
            self.login_Window.passwordWarningLabel.setStyleSheet('color: red')
            self.login_Window.passwordWarningLabel.setText("Password must be more than 8 characters")
            return False

    def check_loginLabelEdit_validation_is_passed(self):
        if self.check_login_is_not_empty():
            if self.check_login_rules_are_followed():
                return True
            else:
                return False
        else:
            return False

    def check_passwordLabelEdit_validation_is_passed(self):
        if self.check_password_is_not_empty():
            if self.check_password_rules_are_followed():
                return True
            else:
                return False
        else:
            return False

    #NoteWindow
    def connect_all_events_of_buttons_in_AddWindow(self):
        self.add_note_window.add_button.pressed.connect(lambda: self.add_button_in_AddNoteWindow_is_pressed())

    def add_button_in_AddNoteWindow_is_pressed():
        pass
