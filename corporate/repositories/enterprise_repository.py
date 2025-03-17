from typing import Dict, Optional
from corporate.entities.enterprise import Enterprise


class EnterpriseRepository:
    """Хранилище предприятий (In-Memory)"""

    def __init__(self):
        self.enterprises: Dict[str, Enterprise] = {}

    def add(self, enterprise: Enterprise):
        """Добавляет предприятие в систему"""
        self.enterprises[enterprise.enterprise_id] = enterprise

    def get_by_id(self, enterprise_id: str) -> Optional[Enterprise]:
        """Возвращает предприятие по ID"""
        return self.enterprises.get(enterprise_id)

    def get_by_unp(self, unp: str) -> Optional[Enterprise]:
        """Возвращает предприятие по УНП"""
        return next((e for e in self.enterprises.values() if e.unp == unp), None)

    def update(self, enterprise: Enterprise):
        """Обновляет данные предприятия"""
        if enterprise.enterprise_id in self.enterprises:
            self.enterprises[enterprise.enterprise_id] = enterprise

    def delete(self, enterprise_id: str):
        """Удаляет предприятие"""
        if enterprise_id in self.enterprises:
            del self.enterprises[enterprise_id]

    def get_all(self):
        """Возвращает список всех предприятий"""
        return list(self.enterprises.values())
