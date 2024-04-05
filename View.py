from MainWindow import Ui_MainWindow
from NoteWindow import Ui_NoteWindow
from PyQt6.QtWidgets import QMainWindow

class MainWindowUI(Ui_MainWindow, QMainWindow):
    def __init__(self):
        super(Ui_MainWindow, self).__init__()
        super(QMainWindow, self).__init__()

class NoteWindowUI(Ui_NoteWindow, QMainWindow):
    def __init__(self):
        super(Ui_NoteWindow, self).__init__()
        super(QMainWindow, self).__init__()

