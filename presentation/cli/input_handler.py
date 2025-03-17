from users.services.auth_service import AuthService
from users.services.user_service import UserService
from users.enums.user_role import UserRole
from presentation.exceptions.input_error import InputError


class InputHandler:
    """Обрабатывает ввод пользователя"""

    def __init__(self):
        self.auth_service = AuthService()
        self.user_service = UserService()

    def login(self):
        """Авторизация пользователя"""
        print("\n🔑 Вход в систему")
        email = input("Введите email: ").strip()
        password = input("Введите пароль: ").strip()

        try:
            user = self.auth_service.authenticate(email, password)
            print(f"✅ Успешный вход! Добро пожаловать, {user.full_name} ({user.role.value})")
        except InputError as e:
            print(f"❌ Ошибка: {e}")

    def register(self):
        """Регистрация нового пользователя"""
        print("\n📝 Регистрация нового пользователя")
        full_name = input("Введите ФИО: ").strip()
        passport_number = input("Введите серию и номер паспорта: ").strip()
        id_number = input("Введите идентификационный номер: ").strip()
        phone = input("Введите телефон: ").strip()
        email = input("Введите email: ").strip()
        password = input("Введите пароль: ").strip()

        role_options = {str(i): role for i, role in enumerate(UserRole, 1)}
        print("\nВыберите роль:")
        for key, role in role_options.items():
            print(f"{key}. {role.value}")

        role_choice = input("\nВведите номер роли: ").strip()
        role = role_options.get(role_choice)

        if not role:
            print("❌ Ошибка: Некорректный выбор роли!")
            return

        try:
            user = self.user_service.create_user(full_name, passport_number, id_number, phone, email, password, role)
            print(f"✅ Регистрация успешна! Теперь вы можете войти в систему.")
        except InputError as e:
            print(f"❌ Ошибка: {e}")
