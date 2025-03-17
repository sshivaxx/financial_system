import os


def clear_screen():
    """Очистка экрана (работает для Windows и Unix-подобных ОС)."""
    os.system('cls' if os.name == 'nt' else 'clear')


def print_header(title: str):
    """Выводит стилизованный заголовок."""
    print("\n" + "=" * 40)
    print(f"📌 {title}")
    print("=" * 40)


def print_success(message: str):
    """Выводит сообщение об успехе."""
    print(f"✅ {message}")


def print_error(message: str):
    """Выводит сообщение об ошибке."""
    print(f"❌ Ошибка: {message}")


def print_warning(message: str):
    """Выводит предупреждение."""
    print(f"⚠️ {message}")
