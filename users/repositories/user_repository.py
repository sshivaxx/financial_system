from typing import Dict, Optional
from users.entities.user import User


class UserRepository:
    """Хранилище пользователей (In-Memory)"""

    def __init__(self):
        self.users: Dict[str, User] = {}

    def add(self, user: User):
        """Добавляет пользователя"""
        self.users[user.user_id] = user

    def get_by_id(self, user_id: str) -> Optional[User]:
        """Ищет пользователя по ID"""
        return self.users.get(user_id)

    def get_by_email(self, email: str) -> Optional[User]:
        """Ищет пользователя по email"""
        return next((user for user in self.users.values() if user.email == email), None)

    def update(self, user: User):
        """Обновляет пользователя"""
        if user.user_id in self.users:
            self.users[user.user_id] = user

    def delete(self, user_id: str):
        """Удаляет пользователя"""
        if user_id in self.users:
            del self.users[user_id]

    def get_all(self):
        """Возвращает всех пользователей"""
        return list(self.users.values())
