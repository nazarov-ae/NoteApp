from MainWindow import Ui_MainWindow
from NoteWindow import Ui_NoteWindow
from ViewModel import ViewModel
from PyQt6.QtWidgets import QMainWindow
import pretty_errors

class MainWindowUI(Ui_MainWindow, QMainWindow):
    def __init__(self):
        super(Ui_MainWindow, self).__init__()
        super(QMainWindow, self).__init__()

class NoteWindowUI(Ui_NoteWindow, QMainWindow):
    def __init__(self):
        super(Ui_NoteWindow, self).__init__()
        super(QMainWindow, self).__init__()

class View():
    def __init__(self, viewModel: ViewModel) -> None:
        self.mainWindow = MainWindowUI()
        self.mainWindow.setupUi(self.mainWindow)

        self.noteWindow = NoteWindowUI()
        self.noteWindow.setupUi(self.noteWindow)

        self.showMainWindow()

    def showMainWindow(self):
        self.mainWindow.show()

    def addButtonIsPressed(self):
        self.noteWindow.show()
