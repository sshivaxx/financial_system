class AuthError(Exception):
    """Базовая ошибка аутентификации"""

    def __init__(self, message="Ошибка аутентификации"):
        super().__init__(message)


class UserNotFoundError(AuthError):
    """Ошибка: пользователь не найден"""

    def __init__(self):
        super().__init__("Пользователь не найден")


class InvalidCredentialsError(AuthError):
    """Ошибка: неверные учетные данные"""

    def __init__(self):
        super().__init__("Неверный email или пароль")


class PermissionDeniedError(AuthError):
    """Ошибка: недостаточно прав"""

    def __init__(self):
        super().__init__("У вас нет прав для выполнения этого действия")
