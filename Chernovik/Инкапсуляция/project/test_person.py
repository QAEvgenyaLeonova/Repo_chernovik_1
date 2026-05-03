# test_person.py
import unittest  # Импортируем модуль unittest для создания тестов
from person import Person  # Импортируем класс Person из файла person.py

class TestPerson(unittest.TestCase):
    """Класс тестов для проверки функциональности класса Person."""

    def setUp(self):
        """
        Метод setUp вызывается перед каждым тестом.
        Создаёт экземпляр Person для использования в тестах.
        """
        self.person = Person("Анна", 25, "anna@mail.com")  # Создаём объект Person с тестовыми данными

    def test_get_name(self):
        """Тест для проверки геттера get_name."""
        self.assertEqual(self.person.get_name(), "Анна")  # Проверяем, что геттер возвращает правильное имя

    def test_set_name_valid(self):
        """Тест установки корректного имени."""
        self.person.set_name("Мария")  # Устанавливаем новое имя
        self.assertEqual(self.person.get_name(), "Мария")  # Проверяем, что имя изменилось

    def test_set_name_invalid(self):
        """Тест попытки установить пустое имя."""
        with self.assertRaises(ValueError):  # Ожидаем ошибку ValueError
            self.person.set_name("")  # Пытаемся установить пустое имя

    def test_get_age(self):
        """Тест для проверки геттера get_age."""
        self.assertEqual(self.person.get_age(), 25)  # Проверяем, что геттер возвращает правильный возраст

    def test_set_age_valid(self):
        """Тест установки корректного возраста."""
        self.person.set_age(30)  # Устанавливаем новый возраст
        self.assertEqual(self.person.get_age(), 30)  # Проверяем, что возраст изменился

    def test_set_age_invalid(self):
        """Тест попытки установить некорректный возраст."""
        with self.assertRaises(ValueError):  # Ожидаем ошибку ValueError
            self.person.set_age(-5)  # Пытаемся установить отрицательный возраст

    def test_get_email(self):
        """Тест для проверки геттера get_email."""
        self.assertEqual(self.person.get_email(), "anna@mail.com")  # Проверяем, что геттер возвращает правильный email

    def test_set_email_valid(self):
        """Тест установки корректного email."""
        self.person.set_email("maria@mail.com")  # Устанавливаем новый email
        self.assertEqual(self.person.get_email(), "maria@mail.com")  # Проверяем, что email изменился

    def test_set_email_invalid(self):
        """Тест попытки установить некорректный email."""
        with self.assertRaises(ValueError):  # Ожидаем ошибку ValueError
            self.person.set_email("invalid-email")  # Пытаемся установить email без @

    def test_display_info(self):
        """Тест метода display_info."""
        expected = "Имя: Анна, Возраст: 25, Email: anna@mail.com"  # Ожидаемая строка
        self.assertEqual(self.person.display_info(), expected)  # Проверяем, что метод возвращает правильную строку

if __name__ == '__main__':
    unittest.main()  # Запускаем тесты, если файл запущен напрямую
