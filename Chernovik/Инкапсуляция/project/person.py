class Person:
    def __init__(self, name, str, age: int, email: str):
        self.name = name
        self.str = str
        self.age = age
        self.email = email


    def get_name(self) -> str:#Геттер для получения имени. Возвращает приватное поле __name
        return self.__name

    def set_name(self, ):