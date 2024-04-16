from MainWindow import Ui_MainWindow
from NoteWindow import Ui_NoteWindow
from LoginWindow import Ui_LoginWindow
from ViewModel import ViewModel
from PyQt6.QtWidgets import QMainWindow, QDialog
import pretty_errors

class MainWindowUI(Ui_MainWindow, QMainWindow):
    def __init__(self):
        super(Ui_MainWindow, self).__init__()
        super(QMainWindow, self).__init__()

class NoteWindowUI(Ui_NoteWindow, QDialog):
    def __init__(self):
        super(Ui_NoteWindow, self).__init__()
        super(QDialog, self).__init__()

class LoginWindowUI(Ui_LoginWindow, QDialog):
    def __init__(self):
        super(Ui_LoginWindow, self).__init__()
        super(QDialog, self).__init__()

class View():
    def __init__(self, viewModel: ViewModel) -> None:
        self.mainWindow = MainWindowUI()
        self.mainWindow.setupUi(self.mainWindow)

        self.noteWindow = NoteWindowUI()
        self.noteWindow.setupUi(self.noteWindow)

        self.loginWindow = LoginWindowUI()
        self.loginWindow.setupUi(self.loginWindow)
        self.loginWindow.loginWarningLabel.setText("")
        self.loginWindow.passwordWarningLabel.setText("")

        self.connect_all_events_of_buttons_in_MainWindow()
        self.connect_all_events_of_buttons_in_LoginWindow()
        self.loginWindow.show()

    def connect_all_events_of_buttons_in_MainWindow(self):
        self.mainWindow.add_button.pressed.connect(lambda: self.add_button_in_MainWindow_is_pressed())
        self.mainWindow.edit_button.pressed.connect(lambda: self.edit_button_in_MainWindow_is_pressed())

    def connect_all_events_of_buttons_in_LoginWindow(self):
        self.loginWindow.signInButton.pressed.connect(lambda: self.signIn_button_in_LoginWindow_is_pressed())

    def signIn_button_in_LoginWindow_is_pressed(self):
        if self.check_loginLabelEdit_validation_is_passed():
            if self.check_passwordLabelEdit_validation_is_passed():
                self.mainWindow.mainTabLabel.setText(f"Welcome {self.loginWindow.loginLabelEdit.text()}. Here all your notes")
                self.mainWindow.show()

    def check_login_is_not_empty(self):
        if self.loginWindow.loginLabelEdit.text() != "":
            self.loginWindow.loginWarningLabel.setText("")
            return True
        else:
            self.loginWindow.loginWarningLabel.setText("Пожалуйста введите логин")
            return False

    def check_password_is_not_empty(self):
        if self.loginWindow.passwordLabelEdit.text() != "":
            self.loginWindow.passwordWarningLabel.setText("")
            return True
        else:
            self.loginWindow.passwordWarningLabel.setText("Пожалуйста введите пароль")
            return False

    def check_login_rules_are_followed(self):
        if len(self.loginWindow.loginLabelEdit.text()) < 10:
            self.loginWindow.loginWarningLabel.setText("")
            return True
        else:
            self.loginWindow.loginWarningLabel.setText("Логин должен быть меньше либо равен 10 символам")
            return False

    def check_password_rules_are_followed(self):
        if len(self.loginWindow.passwordLabelEdit.text()) < 8:
            self.loginWindow.loginWarningLabel.setText("")
            return True
        else:
            self.loginWindow.loginWarningLabel.setText("Пароль должен быть длиней 8 символов")
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


    def add_button_in_MainWindow_is_pressed(self):
        self.noteWindow.noteTabTittle.setText("Add note")
        self.noteWindow.addOrEditButton.setText("Add")
        self.noteWindow.show()

    def edit_button_in_MainWindow_is_pressed(self):
        self.noteWindow.noteTabTittle.setText("Edit note")
        self.noteWindow.addOrEditButton.setText("Edit")
        self.noteWindow.show()
