from Database import Database
from User import User


class Model():
    def __init__(self) -> None:
        # Почему не просто self.database?
        # Вообще по MVVM вся логика Database должна быть здесь, в модели
        # Название должно отобразить суть сущности. Model - слишком обще, лучше
        # UserModel, ну и сам класс User лучше перетащить сюда.
        # То есть модель содержит данные и логику их обработки (по MVVM)
        self.database_creator = Database()
        self.user = User()
