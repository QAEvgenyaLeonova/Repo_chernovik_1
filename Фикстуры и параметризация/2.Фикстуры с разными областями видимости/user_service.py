class UserService:
    def __init__(self):
        self.users = {}
        self._next_id = 1

    def create_user(self, name: str, email: str) -> dict:
        user_id = self._next_id
        self.users[user_id] = {"id": user_id, "name": name, "email": email}
        self._next_id += 1
        return self.users[user_id]

    def get_user(self, user_id: int) -> dict | None:
        return self.users.get(user_id)

    def delete_user(self, user_id: int) -> bool:
        if user_id in self.users:
            del self.users[user_id]
            return True
        return False

    def list_users(self) -> list:
        return list(self.users.values())
