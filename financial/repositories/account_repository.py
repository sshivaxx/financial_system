from typing import Dict, Optional
from financial.entities.account import Account

class AccountRepository:
    """Хранилище счетов (In-Memory)"""

    def __init__(self):
        self.accounts: Dict[str, Account] = {}

    def add(self, account: Account):
        """Добавляет новый счёт"""
        self.accounts[account.account_number] = account

    def get(self, account_number: str) -> Optional[Account]:
        """Получает счёт по номеру"""
        return self.accounts.get(account_number)

    def update(self, account: Account):
        """Обновляет данные счёта"""
        if account.account_number in self.accounts:
            self.accounts[account.account_number] = account

    def delete(self, account_number: str):
        """Удаляет счёт"""
        if account_number in self.accounts:
            del self.accounts[account_number]
