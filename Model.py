from Database import Database
from User import User


class Model():
    def __init__(self) -> None:
        self.database_creator = Database()
        self.user = User()
