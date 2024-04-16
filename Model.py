import pretty_errors
from Database import DatabaseCreator
from User import User


class Model():
    def __init__(self) -> None:
        self.database_creator = DatabaseCreator()
        self.user = User()
