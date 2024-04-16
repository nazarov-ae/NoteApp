from MainWindow import Ui_MainWindow
from AddNoteWindow import Ui_AddNoteWindow
from EditNoteWindow import Ui_EditNoteWindow
from LoginWindow import Ui_LoginWindow
from ViewModel import ViewModel
from PyQt6 import QtCore
from PyQt6.QtCore import Qt, QModelIndex, QDate
from PyQt6.QtWidgets import QMainWindow, QDialog
from PyQt6.QtGui import QStandardItemModel, QStandardItem
from typing import List
from Note import Note
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

        self.login = ""
        self.password = ""

        self.note = ""
        self.note_date = ""
        self.search_filter = ""

        self.main_Window = MainWindowUI()
        self.main_Window.setupUi(self.main_Window)

        self.table_of_notes_item_model = QStandardItemModel()
        self.setup_model_in_table_of_notes_in_MainWindow()

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
        self.connect_all_events_of_buttons_in_EditWindow()

        self.login_Window.loginLabelEdit.textChanged.connect(self.connect_login_to_loginEdit)
        self.login_Window.passwordLabelEdit.textChanged.connect(self.connect_password_to_passwordEdit)

        self.add_note_window.noteTextEdit.textChanged.connect(self.connect_note_to_noteTextEdit_in_Add_note_Window)

        self.main_Window.showEvent = self.main_Window_showEvent
        self.add_note_window.showEvent = self.add_note_Window_showEvent
        self.edit_note_window.showEvent = self.edit_note_Window_showEvent
        self.main_Window.searchBar.textChanged.connect(self.connect_search_filter_to_SearchBar_in_MainWindow)
        self.main_Window.table_of_notes.clicked.connect(self.change_selected_Note_of_User)

        self.add_note_window.noteSelectedDate.selectionChanged.connect(self.connect_date_to_noteSelectedDate_in_Add_note_Window)

        self.login_Window.show()

    def main_Window_showEvent(self, event):
        self.change_notes_in_table_of_notes_in_MainWindow()

    def add_note_Window_showEvent(self, event):
        self.change_date_in_Add_note_Window()

    def edit_note_Window_showEvent(self, event):
        self.change_date_in_calendar_in_edit_note_window()
        note_text = self.viewModel.get_selected_note().note
        self.edit_note_window.noteTextEdit.setPlainText(note_text)

    def change_date_in_calendar_in_edit_note_window(self):
        date = QDate.fromString(self.viewModel.get_selected_note().date, "yyyy-MM-dd")
        self.edit_note_window.noteSelectedDate.setSelectedDate(date)

    def connect_login_to_loginEdit(self):
        self.login = self.login_Window.loginLabelEdit.text()

    def connect_password_to_passwordEdit(self):
        self.password = self.login_Window.passwordLabelEdit.text()

    def connect_note_to_noteTextEdit_in_Add_note_Window(self):
        self.note = self.add_note_window.noteTextEdit.toPlainText()

    def connect_search_filter_to_SearchBar_in_MainWindow(self):
        self.search_filter = self.main_Window.searchBar.text()
        self.change_notes_in_table_of_notes_in_MainWindow()

    def connect_date_to_noteSelectedDate_in_Add_note_Window(self):
        self.change_date_in_Add_note_Window()

    def change_date_in_Add_note_Window(self):
        self.note_date = self.add_note_window.noteSelectedDate.selectedDate().toString("yyyy-MM-dd")

    def get_all_notes_of_User(self):
        return self.viewModel.get_all_notes_of_User(self.viewModel.get_login_of_User(), self.search_filter)

    #MainWindow
    def setup_model_in_table_of_notes_in_MainWindow(self):
        self.main_Window.table_of_notes.setModel(self.table_of_notes_item_model)
        self.table_of_notes_item_model.setHorizontalHeaderLabels(['Note', 'Date'])

    def change_notes_in_table_of_notes_in_MainWindow(self):
        self.table_of_notes_item_model.clear()
        self.rows = self.get_all_notes_of_User()

        for row in self.rows:
            note = Note(row[0], row[1], row[2])

            note_id = QStandardItem(str(note.note_id))
            note_text = QStandardItem(str(note.note))
            note_date = QStandardItem(str(note.date))
            self.table_of_notes_item_model.appendRow([note_id, note_text, note_date])
            self.table_of_notes_item_model.setHorizontalHeaderLabels(["Id", "Note", "Date"])
            self.main_Window.table_of_notes.setColumnHidden(0, True)

    def change_selected_Note_of_User(self, index: QModelIndex):
        if index.isValid():
            selected_row = index.row()
            note_id = self.table_of_notes_item_model.item(selected_row, 0).text()
            note_text = self.table_of_notes_item_model.item(selected_row, 1).text()
            note_date = self.table_of_notes_item_model.item(selected_row, 2).text()
            self.viewModel.change_selected_note(int(note_id), note_text, note_date)
            print(self.viewModel.get_selected_note().note)
            print(f"Selected item: ID={note_id}, Note={note_text}, Date={note_date}")

    def delete_note_in_MainWindow_is_pressed(self):
        note_id = self.viewModel.get_selected_note().note_id
        self.viewModel.delete_note(note_id)
        self.viewModel.reset_selected_note()
        self.change_notes_in_table_of_notes_in_MainWindow()

    def connect_all_events_of_buttons_in_MainWindow(self):
        self.main_Window.add_button.pressed.connect(lambda: self.add_button_in_MainWindow_is_pressed())
        self.main_Window.edit_button.pressed.connect(lambda: self.edit_button_in_MainWindow_is_pressed())
        self.main_Window.delete_button.pressed.connect(lambda: self.delete_note_in_MainWindow_is_pressed())

    def add_button_in_MainWindow_is_pressed(self):
        self.add_note_window.show()

    def edit_button_in_MainWindow_is_pressed(self):
        self.edit_note_window.show()

    #AddNoteWindow
    def connect_all_events_of_buttons_in_AddWindow(self):
        self.add_note_window.add_button.pressed.connect(lambda: self.add_button_in_AddNoteWindow_is_pressed())

    def add_button_in_AddNoteWindow_is_pressed(self):
        self.viewModel.add_note_in_UsersNotes_table(self.viewModel.get_login_of_User(), self.note, self.note_date)
        self.change_notes_in_table_of_notes_in_MainWindow()

    #LoginWindow
    def connect_all_events_of_buttons_in_LoginWindow(self):
        self.login_Window.sign_up_button.pressed.connect(lambda: self.sign_up_button_in_LoginWindow_is_pressed())
        self.login_Window.sign_in_button.pressed.connect(lambda: self.sign_in_button_in_LoginWindow_is_pressed())

    def sign_in_button_in_LoginWindow_is_pressed(self):
        if self.check_loginLabelEdit_validation_is_passed():
            if self.check_passwordLabelEdit_validation_is_passed():
                if self.viewModel.check_login_is_registered(self.login):
                    if self.viewModel.check_password_is_correct(self.login, self.password):
                        self.viewModel.change_users_info(self.login, self.password)
                        self.main_Window.mainTabLabel.setText(f"Welcome {self.login}. Here all your notes")
                        self.viewModel.reset_selected_note()
                        self.main_Window.show()
                    else:
                        self.login_Window.passwordWarningLabel.setStyleSheet('color: red')
                        self.login_Window.passwordWarningLabel.setText("Incorrect password")
                else:
                    self.login_Window.loginWarningLabel.setStyleSheet('color: red')
                    self.login_Window.loginWarningLabel.setText("This login does not registered")

    def sign_up_button_in_LoginWindow_is_pressed(self):
        if self.check_loginLabelEdit_validation_is_passed():
            if self.check_passwordLabelEdit_validation_is_passed():
                if self.viewModel.check_login_is_registered(self.login):
                    self.login_Window.loginWarningLabel.setStyleSheet('color: red')
                    self.login_Window.loginWarningLabel.setText("This login is already registered")
                else:
                    self.viewModel.add_user_in_Users_table(self.login, self.password)
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

    #EditWindow
    def connect_all_events_of_buttons_in_EditWindow(self):
        self.edit_note_window.edit_button.pressed.connect(lambda: self.edit_button_in_edit_note_window_Is_Pressed())

    def edit_button_in_edit_note_window_Is_Pressed(self):
        self.note_id = self.viewModel.get_selected_note().note_id
        self.note_text = self.edit_note_window.noteTextEdit.toPlainText()
        self.note_date = self.edit_note_window.noteSelectedDate.selectedDate().toString("yyyy-MM-dd")

        self.viewModel.edit_note(self.note_id, self.note_text, self.note_date)
        self.change_notes_in_table_of_notes_in_MainWindow()
