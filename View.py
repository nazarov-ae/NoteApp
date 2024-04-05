from MainWindow import Ui_MainWindow
from NoteWindow import Ui_NoteWindow
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

class View():
    def __init__(self, viewModel: ViewModel) -> None:
        self.mainWindow = MainWindowUI()
        self.mainWindow.setupUi(self.mainWindow)

        self.noteWindow = NoteWindowUI()
        self.noteWindow.setupUi(self.noteWindow)

        self.setupEventsOfButtonsInMainWindow()

        self.showMainWindow()

    def showMainWindow(self):
        self.mainWindow.show()

    def setupEventsOfButtonsInMainWindow(self):
        self.mainWindow.add_button.pressed.connect(lambda: self.addButtonInMainWindowIsPressed())
        self.mainWindow.edit_button.pressed.connect(lambda: self.editButtonInMainWindowIsPressed())

    def addButtonInMainWindowIsPressed(self):
        self.noteWindow.noteTabTittle.setText("Add note")
        self.noteWindow.addOrEditButton.setText("Add")
        self.noteWindow.show()

    def editButtonInMainWindowIsPressed(self):
        self.noteWindow.noteTabTittle.setText("Edit note")
        self.noteWindow.addOrEditButton.setText("Edit")
        self.noteWindow.show()
