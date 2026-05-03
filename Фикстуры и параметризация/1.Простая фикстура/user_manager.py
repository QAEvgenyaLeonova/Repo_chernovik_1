class UserManager:
    def __init__(self):
        self.users = []

    def add_user(self, name, age):
        self.users.append({'name': name, 'age': age})

    def get_user_count(self):
        return len(self.users)
