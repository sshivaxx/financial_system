# financial/entities/account.py
import uuid
from enum import Enum


class AccountStatus(Enum):
    ACTIVE = "active"
    FROZEN = "frozen"
    BLOCKED = "blocked"


class Account:
    def __init__(self, owner_id: str, initial_balance: float = 0.0):
        self.account_number = str(uuid.uuid4())[:12]  # Генерация уникального номера
        self.owner_id = owner_id
        self.balance = initial_balance
        self.status = AccountStatus.ACTIVE

    def deposit(self, amount: float):
        """Пополняет счёт"""
        if self.status != AccountStatus.ACTIVE:
            raise ValueError("Нельзя пополнить неактивный счёт")
        self.balance += amount

    def withdraw(self, amount: float):
        """Снимает деньги со счёта"""
        if self.status != AccountStatus.ACTIVE:
            raise ValueError("Нельзя снять с неактивного счёта")
        if amount > self.balance:
            raise ValueError("Недостаточно средств")
        self.balance -= amount

    def freeze(self):
        """Замораживает счёт"""
        self.status = AccountStatus.FROZEN

    def block(self):
        """Блокирует счёт"""
        self.status = AccountStatus.BLOCKED

    def __repr__(self):
        return f"Account({self.account_number}, Owner={self.owner_id}, Balance={self.balance}, Status={self.status.value})"
