from typing import List
from financial.entities.transaction import Transaction


class TransactionRepository:
    """Хранилище транзакций (In-Memory)"""

    def __init__(self):
        self.transactions: List[Transaction] = []

    def add(self, transaction: Transaction):
        """Добавляет транзакцию"""
        self.transactions.append(transaction)

    def get_all(self) -> List[Transaction]:
        """Возвращает список всех транзакций"""
        return self.transactions
