from financial.entities.credit import Credit, CreditStatus
from financial.repositories.credit_repository import CreditRepository

class CreditService:
    def __init__(self, credit_repo: CreditRepository):
        self.credit_repo = credit_repo

    def apply_for_credit(self, client_id: str, amount: float, interest_rate: float, months: int) -> Credit:
        """Клиент подаёт заявку на кредит"""
        credit = Credit(client_id, amount, interest_rate, months)
        self.credit_repo.add(credit)
        return credit

    def approve_credit(self, credit_id: str):
        """Менеджер подтверждает кредит"""
        credit = self.credit_repo.get(credit_id)
        if not credit:
            raise ValueError("Кредит не найден")
        credit.approve()
        self.credit_repo.update(credit)

    def reject_credit(self, credit_id: str):
        """Менеджер отклоняет кредит"""
        credit = self.credit_repo.get(credit_id)
        if not credit:
            raise ValueError("Кредит не найден")
        credit.reject()
        self.credit_repo.update(credit)

    def close_credit(self, credit_id: str):
        """Закрытие кредита"""
        credit = self.credit_repo.get(credit_id)
        if not credit:
            raise ValueError("Кредит не найден")
        credit.close()
        self.credit_repo.update(credit)
