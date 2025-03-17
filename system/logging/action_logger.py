import logging


class ActionLogger:
    """Класс для логирования действий в системе"""

    def __init__(self, log_file="logs/actions.log"):
        self.logger = logging.getLogger("ActionLogger")
        self.logger.setLevel(logging.INFO)

        handler = logging.FileHandler(log_file)
        formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
        handler.setFormatter(formatter)
        self.logger.addHandler(handler)

    def log_action(self, message: str):
        """Записывает информацию о действии"""
        self.logger.info(message)
