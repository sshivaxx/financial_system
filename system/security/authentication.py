from system.security.encryption import Encryption
from users.repositories.user_repository import UserRepository
from users.exceptions.auth_error import AuthenticationError


class Authentication:
    """Сервис аутентификации пользователей"""

    def __init__(self, user_repo: UserRepository):
        self.user_repo = user_repo

    def login(self, email: str, password: str) -> dict:
        """Аутентифицирует пользователя по email и паролю"""
        user = self.user_repo.get_by_email(email)
        if not user:
            raise AuthenticationError("Пользователь не найден")

        hashed_password = Encryption.hash_password(password)
        if hashed_password != user.password_hash:
            raise AuthenticationError("Неверный пароль")

        return {"user_id": user.user_id, "role": user.role.value}

    def register(self, full_name: str, email: str, password: str, role: str):
        """Регистрирует нового пользователя"""
        if self.user_repo.get_by_email(email):
            raise AuthenticationError("Пользователь с таким email уже существует")

        password_hash = Encryption.hash_password(password)
        new_user = self.user_repo.create(full_name, email, password_hash, role)
        return {"user_id": new_user.user_id, "role": new_user.role.value}
