from enum import Enum


class UserRole(Enum):
    """Роли пользователей в системе"""
    CLIENT = "Клиент"
    OPERATOR = "Оператор"
    MANAGER = "Менеджер"
    ENTERPRISE_SPECIALIST = "Специалист предприятия"
    ADMIN = "Администратор"
