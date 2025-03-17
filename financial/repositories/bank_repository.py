from typing import Dict, Optional
from financial.entities.bank import Bank

class BankRepository:
    """Хранилище банков (In-Memory)"""

    def __init__(self):
        self.banks: Dict[str, Bank] = {}

    def add(self, bank: Bank):
        """Добавляет новый банк"""
        self.banks[bank.bank_id] = bank

    def get(self, bank_id: str) -> Optional[Bank]:
        """Получает банк по ID"""
        return self.banks.get(bank_id)

    def update(self, bank: Bank):
        """Обновляет данные банка"""
        if bank.bank_id in self.banks:
            self.banks[bank.bank_id] = bank

    def delete(self, bank_id: str):
        """Удаляет банк"""
        if bank_id in self.banks:
            del self.banks[bank_id]

    def get_all(self):
        """Возвращает список всех банков"""
        return list(self.banks.values())
