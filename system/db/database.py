import json
import os


class Database:
    """Класс для работы с файлами JSON в качестве хранилища данных"""

    def __init__(self, file_path: str):
        self.file_path = file_path
        if not os.path.exists(file_path):
            self._initialize_db()

    def _initialize_db(self):
        """Создает новый JSON-файл при его отсутствии"""
        with open(self.file_path, "w") as file:
            json.dump({}, file)

    def read_data(self):
        """Читает данные из JSON-файла"""
        with open(self.file_path, "r") as file:
            return json.load(file)

    def write_data(self, data):
        """Записывает данные в JSON-файл"""
        with open(self.file_path, "w") as file:
            json.dump(data, file, indent=4)
