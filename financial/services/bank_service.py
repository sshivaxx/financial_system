from financial.entities.bank import Bank
from financial.repositories.bank_repository import BankRepository

class BankService:
    """Сервис управления банками"""

    def __init__(self, bank_repo: BankRepository):
        self.bank_repo = bank_repo

    def register_bank(self, name: str, bic: str, address: str) -> Bank:
        """Создаёт и регистрирует новый банк"""
        bank = Bank(name=name, bic=bic, address=address)
        self.bank_repo.add(bank)
        return bank

    def get_bank_info(self, bank_id: str) -> Bank:
        """Получает информацию о банке"""
        bank = self.bank_repo.get(bank_id)
        if not bank:
            raise ValueError("Банк не найден")
        return bank

    def update_bank_info(self, bank_id: str, name: str = None, address: str = None):
        """Обновляет информацию о банке"""
        bank = self.bank_repo.get(bank_id)
        if not bank:
            raise ValueError("Банк не найден")
        if name:
            bank.name = name
        if address:
            bank.address = address
        self.bank_repo.update(bank)

    def delete_bank(self, bank_id: str):
        """Удаляет банк"""
        self.bank_repo.delete(bank_id)

    def list_banks(self):
        """Возвращает список всех банков"""
        return self.bank_repo.get_all()
