from uuid import uuid4
from users.enums.user_role import UserRole
from system.security.encryption import Encryption


class User:
    """Модель пользователя"""

    def __init__(
        self,
        full_name: str,
        passport_number: str,
        id_number: str,
        phone: str,
        email: str,
        role: UserRole,
        password: str,
        user_id: str = None
    ):
        self.user_id = user_id if user_id else str(uuid4())  # Уникальный идентификатор пользователя
        self.full_name = full_name
        self.passport_number = passport_number
        self.id_number = id_number
        self.phone = phone
        self.email = email
        self.role = role
        self.password_hash = Encryption.hash_password(password)  # Хешируем пароль

    def check_password(self, password: str) -> bool:
        """Проверяет соответствие пароля"""
        return self.password_hash == Encryption.hash_password(password)

    def to_dict(self) -> dict:
        """Конвертирует объект в словарь (для хранения в JSON)"""
        return {
            "user_id": self.user_id,
            "full_name": self.full_name,
            "passport_number": self.passport_number,
            "id_number": self.id_number,
            "phone": self.phone,
            "email": self.email,
            "role": self.role.value,
            "password_hash": self.password_hash
        }

    @classmethod
    def from_dict(cls, data: dict):
        """Создает объект User из словаря"""
        return cls(
            full_name=data["full_name"],
            passport_number=data["passport_number"],
            id_number=data["id_number"],
            phone=data["phone"],
            email=data["email"],
            role=UserRole(data["role"]),
            password=data["password_hash"],  # Уже захешированное значение
            user_id=data["user_id"]
        )

    def __repr__(self):
        return f"User({self.full_name}, {self.role.value})"
