from financial.entities.account import Account, AccountStatus
from financial.repositories.account_repository import AccountRepository


class AccountService:
    def __init__(self, account_repo: AccountRepository):
        self.account_repo = account_repo

    def create_account(self, owner_id: str, initial_balance: float = 0.0) -> Account:
        """Создаёт новый банковский счёт"""
        account = Account(owner_id, initial_balance)
        self.account_repo.add(account)
        return account

    def deposit(self, account_number: str, amount: float):
        """Пополняет счёт"""
        account = self.account_repo.get(account_number)
        if not account:
            raise ValueError("Счёт не найден")
        account.deposit(amount)
        self.account_repo.update(account)

    def withdraw(self, account_number: str, amount: float):
        """Снимает деньги со счёта"""
        account = self.account_repo.get(account_number)
        if not account:
            raise ValueError("Счёт не найден")
        account.withdraw(amount)
        self.account_repo.update(account)

    def freeze_account(self, account_number: str):
        """Замораживает счёт"""
        account = self.account_repo.get(account_number)
        if not account:
            raise ValueError("Счёт не найден")
        account.freeze()
        self.account_repo.update(account)

    def block_account(self, account_number: str):
        """Блокирует счёт"""
        account = self.account_repo.get(account_number)
        if not account:
            raise ValueError("Счёт не найден")
        account.block()
        self.account_repo.update(account)
