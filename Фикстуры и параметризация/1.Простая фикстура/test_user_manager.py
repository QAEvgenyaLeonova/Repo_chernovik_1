import pytest
from user_manager import UserManager

@pytest.fixture
def user_manager():
    """Фикстура создаёт экземпляр UserManager и добавляет двух тестовых пользователей."""
    manager = UserManager()
    manager.add_user('User_1', 25)
    manager.add_user('User_2', 30)
    return manager

def test_user_count(user_manager):
    assert user_manager.get_user_count() == 2

def test_add_new_user(user_manager):
    """Тест добавляет нового пользователя и проверяет счётчик."""
    user_manager.add_user("Мария", 28)
    assert user_manager.get_user_count() == 3







