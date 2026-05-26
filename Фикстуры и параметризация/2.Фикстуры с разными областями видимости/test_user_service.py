import pytest
from user_service import UserService

# scope="session" — создаётся один раз для всей сессии тестов
@pytest.fixture(scope="session")
def session_logger():
    print("\n--- Начало тестовой сессии ---")
    logger = {"tests_run": 0, "users_created": 0}
    yield logger
    print(f"\n--- Конец сессии. Всего создано пользователей: {logger['users_created']} ---")

# scope="module" — создаётся один раз на модуль (файл с тестами)
@pytest.fixture(scope="module")
def user_service():
    print("Инициализация UserService для модуля")
    service = UserService()
    yield service
    print("Завершение работы UserService")

# scope="class" — создаётся для каждого тестового класса
@pytest.fixture(scope="class")
def sample_users():
    return [
        {"name": "Alice", "email": "alice@example.com"},
        {"name": "Bob", "email": "bob@example.com"}
    ]

# scope="function" — создаётся перед каждым тестом
@pytest.fixture(scope="function")
def fresh_user():
    return {"name": "Test User", "email": "test@example.com"}

class TestUserCreation:
    @pytest.mark.usefixtures("session_logger")
    def test_create_user(self, user_service, fresh_user, session_logger):
        user = user_service.create_user(**fresh_user)
        assert user["name"] == fresh_user["name"]
        assert user["email"] == fresh_user["email"]
        session_logger["users_created"] += 1

    def test_create_multiple_users(self, user_service, sample_users):
        created_users = []
        for user_data in sample_users:
            created_users.append(user_service.create_user(**user_data))
        assert len(created_users) == 2
        assert created_users[0]["name"] == "Alice"
        assert created_users[1]["name"] == "Bob"

class TestUserRetrieval:
    def test_get_existing_user(self, user_service):
        # Создаём пользователя для теста
        test_user = user_service.create_user("Charlie", "charlie@example.com")
        retrieved_user = user_service.get_user(test_user["id"])
        assert retrieved_user == test_user

    def test_get_nonexistent_user(self, user_service):
        nonexistent_user = user_service.get_user(999)
        assert nonexistent_user is None

def test_delete_user(user_service, session_logger):
    # Создаём и удаляем пользователя
    user = user_service.create_user("David", "david@example.com")
    session_logger["users_created"] += 1
    result = user_service.delete_user(user["id"])
    assert result is True
    assert user_service.get_user(user["id"]) is None

def test_list_users(user_service, sample_users):
    # Заполняем сервис пользователями
    for user_data in sample_users:
        user_service.create_user(**user_data)
    users_list = user_service.list_users()
    assert len(users_list) == 2
    assert users_list[0]["name"] in ["Alice", "Bob"]



'''понимание жизненного цикла фикстур разных областей действия;

практику изоляции тестов (когда нужна изоляция, а когда можно делиться ресурсами);

работу с yield в фикстурах (код после yield выполняется после тестов);

использование @pytest.mark.usefixtures для применения фикстур без передачи параметров;

структуру тестового класса и отдельных функций-тестов.'''
















