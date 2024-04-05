from MainWindow import Ui_MainWindow
from PyQt6.QtWidgets import QMainWindow

class MainWindowUI(Ui_MainWindow, QMainWindow):
    def __init__(self):
        super(Ui_MainWindow, self).__init__()
        super(QMainWindow, self).__init__()

