from users.entities.user import User
from users.enums.user_role import UserRole
from users.repositories.user_repository import UserRepository
from users.exceptions.auth_error import UserNotFoundError


class UserService:
    """Сервис управления пользователями"""

    def __init__(self, user_repo: UserRepository):
        self.user_repo = user_repo

    def register_user(self, full_name: str, passport_number: str, id_number: str, phone: str, email: str,
                      role: UserRole, password: str) -> User:
        """Регистрирует нового пользователя"""
        if self.user_repo.get_by_email(email):
            raise ValueError("Пользователь с таким email уже существует")
        user = User(full_name, passport_number, id_number, phone, email, role, password)
        self.user_repo.add(user)
        return user

    def get_user(self, user_id: str) -> User:
        """Получает информацию о пользователе"""
        user = self.user_repo.get_by_id(user_id)
        if not user:
            raise UserNotFoundError()
        return user

    def update_user_info(self, user_id: str, full_name: str = None, phone: str = None, email: str = None):
        """Обновляет информацию о пользователе"""
        user = self.user_repo.get_by_id(user_id)
        if not user:
            raise UserNotFoundError()
        if full_name:
            user.full_name = full_name
        if phone:
            user.phone = phone
        if email:
            user.email = email
        self.user_repo.update(user)

    def delete_user(self, user_id: str):
        """Удаляет пользователя"""
        if not self.user_repo.get_by_id(user_id):
            raise UserNotFoundError()
        self.user_repo.delete(user_id)
