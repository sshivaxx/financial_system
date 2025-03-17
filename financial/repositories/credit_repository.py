from typing import Dict, Optional
from financial.entities.credit import Credit


class CreditRepository:
    """Хранилище кредитов (In-Memory)"""

    def __init__(self):
        self.credits: Dict[str, Credit] = {}

    def add(self, credit: Credit):
        """Добавляет новый кредит"""
        self.credits[credit.credit_id] = credit

    def get(self, credit_id: str) -> Optional[Credit]:
        """Получает кредит по ID"""
        return self.credits.get(credit_id)

    def update(self, credit: Credit):
        """Обновляет данные кредита"""
        if credit.credit_id in self.credits:
            self.credits[credit.credit_id] = credit

    def delete(self, credit_id: str):
        """Удаляет кредит"""
        if credit_id in self.credits:
            del self.credits[credit_id]
