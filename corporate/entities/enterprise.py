from uuid import uuid4


class Enterprise:
    """Модель предприятия"""

    def __init__(self, name: str, type_: str, unp: str, bic: str, address: str, bank_id: str):
        self.enterprise_id = str(uuid4())  # Уникальный идентификатор
        self.name = name  # Название предприятия
        self.type = type_  # Тип (ИП, ООО, ЗАО и т.д.)
        self.unp = unp  # УНП (Уникальный номер предприятия)
        self.bic = bic  # БИК банка, в котором предприятие обслуживается
        self.address = address  # Юридический адрес
        self.bank_id = bank_id  # ID банка, с которым работает предприятие
        self.accounts = []  # Список счетов предприятия

    def add_account(self, account_id: str):
        """Добавляет новый счет предприятию"""
        self.accounts.append(account_id)

    def remove_account(self, account_id: str):
        """Удаляет счет предприятия"""
        self.accounts.remove(account_id)

    def __repr__(self):
        return f"Enterprise({self.name}, {self.type}, {self.unp})"
