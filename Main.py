from Model import Model
from View import View
from ViewModel import ViewModel
from PyQt6.QtWidgets import QApplication
from Database import DatabaseCreator
import sys

class Main():
    def __init__(self) -> None:
        self.model = Model()
        self.viewModel = ViewModel(self.model)
        self.view = View(self.viewModel)
        self.database_creator = DatabaseCreator()

def start():
    if __name__ == "__main__":
        app = QApplication(sys.argv)
        main = Main()
        main.database_creator.create_database()
        sys.exit(app.exec())

start()
