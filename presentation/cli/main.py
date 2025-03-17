from presentation.cli.menu import Menu


def main():
    """Точка входа в консольное приложение"""
    print("\n💰 Добро пожаловать в систему управления финансами! 💰")
    menu = Menu()
    menu.run()


if __name__ == "__main__":
    main()
