from enum import Enum
import uuid


class CreditStatus(Enum):
    PENDING = "pending"
    APPROVED = "approved"
    REJECTED = "rejected"
    ACTIVE = "active"
    CLOSED = "closed"


class Credit:
    def __init__(self, client_id: str, amount: float, interest_rate: float, months: int):
        self.credit_id = str(uuid.uuid4())[:12]
        self.client_id = client_id
        self.amount = amount
        self.interest_rate = interest_rate
        self.months = months
        self.status = CreditStatus.PENDING

    def approve(self):
        """Подтверждает кредит"""
        self.status = CreditStatus.APPROVED

    def reject(self):
        """Отклоняет кредит"""
        self.status = CreditStatus.REJECTED

    def activate(self):
        """Активирует кредит"""
        self.status = CreditStatus.ACTIVE

    def close(self):
        """Закрывает кредит"""
        self.status = CreditStatus.CLOSED

    def __repr__(self):
        return f"Credit({self.credit_id}, Client={self.client_id}, Amount={self.amount}, Status={self.status.value})"
