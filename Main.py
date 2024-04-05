from Model import Model
from View import View
from ViewModel import ViewModel
from PyQt6.QtWidgets import QApplication
import sys

class Main():
    def __init__(self) -> None:
        self.model = Model()
        self.viewModel = ViewModel()
        self.view = View(self.viewModel)

def start():
    if __name__ == "__main__":
        app = QApplication(sys.argv)
        main = Main()
        sys.exit(app.exec())

start()
