from ViewModel import ViewModel
from PyQt6.QtWidgets import QApplication
from View import MainWindowUI
import sys
import pretty_errors

class Model():
    def __init__(self) -> None:
        self.viewModel = ViewModel()

def main():
    model = Model()
    openWindow(model)

def openWindow(model):
    if __name__ == "__main__":
        app = QApplication(sys.argv)
        mainWindow = MainWindowUI()
        mainWindow.setupUi(mainWindow)
        mainWindow.show()
        sys.exit(app.exec())

main()
