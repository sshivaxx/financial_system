from users.repositories.user_repository import UserRepository
from users.exceptions.auth_error import UserNotFoundError, InvalidCredentialsError


class AuthService:
    """Сервис аутентификации пользователей"""

    def __init__(self, user_repo: UserRepository):
        self.user_repo = user_repo

    def authenticate(self, email: str, password: str):
        """Проверяет учетные данные пользователя"""
        user = self.user_repo.get_by_email(email)
        if not user:
            raise UserNotFoundError()
        if user.password != password:
            raise InvalidCredentialsError()
        return user

    def change_password(self, user_id: str, old_password: str, new_password: str):
        """Изменяет пароль пользователя"""
        user = self.user_repo.get_by_id(user_id)
        if not user:
            raise UserNotFoundError()
        if user.password != old_password:
            raise InvalidCredentialsError()
        user.password = new_password
        self.user_repo.update(user)
