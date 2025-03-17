from input_handler import InputHandler
from ui_components import print_header, print_error
from presentation.exceptions.navigation_error import NavigationError


class Menu:
    def __init__(self):
        self.input_handler = InputHandler()

    def display_menu(self):
        print_header("Главное меню")
        print("1. Войти")
        print("2. Зарегистрироваться")
        print("3. Выйти")

    def run(self):
        while True:
            try:
                self.display_menu()
                choice = input("Выберите действие: ").strip()
                match choice:
                    case "1":
                        self.input_handler.login()
                    case "2":
                        self.input_handler.register()
                    case "3":
                        print("Выход из системы.")
                        break
                    case _:
                        raise NavigationError("Некорректный ввод. Попробуйте снова.")
            except NavigationError as e:
                print_error(str(e))
