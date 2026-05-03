# main.py
from person import Person  # Импортируем класс Person из файла person.py

def main():
    """Основная функция для демонстрации работы класса Person."""
    # Создаём экземпляр класса Person
    person = Person("Иван", 30, "ivan@mail.com")

    # Выводим начальную информацию
    print("Начальная информация:")
    print(person.display_info())

    # Изменяем данные через сеттеры
    print("\nИзменяем данные:")
    person.set_name("Пётр")
    person.set_age(35)
    person.set_email("petr@mail.com")

    # Выводим обновлённую информацию
    print(person.display_info())

    # Показываем работу с ошибками
    print("\nПопытка установить некорректные данные:")
    try:
        person.set_age(-10)  # Попытка установить отрицательный возраст
    except ValueError as e:
        print(f"Ошибка: {e}")  # Выводим сообщение об ошибке

if __name__ == '__main__':
    main()  # Запускаем основную функцию, если файл запущен напрямую
