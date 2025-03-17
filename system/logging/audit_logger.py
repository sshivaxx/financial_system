import logging


class AuditLogger:
    """Класс для логирования важных событий (например, попыток взлома)"""

    def __init__(self, log_file="logs/audit.log"):
        self.logger = logging.getLogger("AuditLogger")
        self.logger.setLevel(logging.WARNING)

        handler = logging.FileHandler(log_file)
        formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
        handler.setFormatter(formatter)
        self.logger.addHandler(handler)

    def log_security_issue(self, message: str):
        """Логирует проблемы безопасности"""
        self.logger.warning(message)
