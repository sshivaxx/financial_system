from typing import List
from account import Account


class Bank:
    def __init__(self, name: str, bic: str):
        self.name = name
        self.bic = bic
        self.accounts: List[Account] = []

    def add_account(self, account: Account):
        """Добавляет счёт в банк"""
        self.accounts.append(account)

    def find_account(self, account_number: str) -> Account | None:
        """Находит счёт по номеру"""
        return next((acc for acc in self.accounts if acc.account_number == account_number), None)

    def __repr__(self):
        return f"Bank(name={self.name}, bic={self.bic}, accounts={len(self.accounts)})"
