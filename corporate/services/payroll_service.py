from corporate.repositories.enterprise_repository import EnterpriseRepository
from financial.repositories.account_repository import AccountRepository
from users.repositories.user_repository import UserRepository
from users.exceptions.auth_error import UserNotFoundError
from corporate.entities.enterprise import Enterprise


class PayrollService:
    """Сервис управления зарплатными проектами"""

    def __init__(self, enterprise_repo: EnterpriseRepository, user_repo: UserRepository,
                 account_repo: AccountRepository):
        self.enterprise_repo = enterprise_repo
        self.user_repo = user_repo
        self.account_repo = account_repo

    def request_payroll_project(self, enterprise_id: str, operator_id: str):
        """Запрос на подключение зарплатного проекта (требует подтверждения оператора)"""
        enterprise = self.enterprise_repo.get_by_id(enterprise_id)
        if not enterprise:
            raise ValueError("Предприятие не найдено")

        print(f"Зарплатный проект для {enterprise.name} запрошен оператором {operator_id}.")

    def approve_payroll_project(self, enterprise_id: str, operator_id: str):
        """Оператор подтверждает зарплатный проект"""
        enterprise = self.enterprise_repo.get_by_id(enterprise_id)
        if not enterprise:
            raise ValueError("Предприятие не найдено")

        print(f"Оператор {operator_id} подтвердил зарплатный проект для {enterprise.name}.")

    def process_salary_payment(self, enterprise_id: str, employee_id: str, amount: float):
        """Перечисление зарплаты сотруднику"""
        enterprise = self.enterprise_repo.get_by_id(enterprise_id)
        if not enterprise:
            raise ValueError("Предприятие не найдено")

        employee = self.user_repo.get_by_id(employee_id)
        if not employee:
            raise UserNotFoundError()

        # Получаем счет предприятия и сотрудника
        enterprise_account = self.account_repo.get_account_by_enterprise(enterprise_id)
        employee_account = self.account_repo.get_account_by_user(employee_id)

        if not enterprise_account or not employee_account:
            raise ValueError("Не найдены счета для перевода зарплаты")

        # Переводим средства
        if enterprise_account.balance < amount:
            raise ValueError("Недостаточно средств на счету предприятия")

        enterprise_account.balance -= amount
        employee_account.balance += amount

        print(f"Переведено {amount} BYN сотруднику {employee.full_name} от предприятия {enterprise.name}.")
