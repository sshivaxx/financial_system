from financial.entities.transaction import Transaction
from financial.repositories.account_repository import AccountRepository
from financial.repositories.transaction_repository import TransactionRepository

class TransactionService:
    def __init__(self, account_repo: AccountRepository, transaction_repo: TransactionRepository):
        self.account_repo = account_repo
        self.transaction_repo = transaction_repo

    def transfer(self, from_account_number: str, to_account_number: str, amount: float):
        """Переводит деньги между счетами"""
        from_account = self.account_repo.get(from_account_number)
        to_account = self.account_repo.get(to_account_number)

        if not from_account or not to_account:
            raise ValueError("Один из счетов не найден")
        if from_account.status != "active" or to_account.status != "active":
            raise ValueError("Один из счетов не активен")
        if from_account.balance < amount:
            raise ValueError("Недостаточно средств")

        # Выполняем перевод
        from_account.withdraw(amount)
        to_account.deposit(amount)

        # Сохраняем изменения
        self.account_repo.update(from_account)
        self.account_repo.update(to_account)

        # Создаём транзакцию
        transaction = Transaction(from_account_number, to_account_number, amount)
        self.transaction_repo.add(transaction)

        return transaction
