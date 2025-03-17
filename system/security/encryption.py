import hashlib
import base64
from cryptography.fernet import Fernet


class Encryption:
    """Класс для шифрования и хеширования данных"""

    @staticmethod
    def generate_key():
        """Генерирует новый ключ для шифрования"""
        return Fernet.generate_key()

    @staticmethod
    def encrypt_data(data: str, key: bytes) -> str:
        """Шифрует данные"""
        fernet = Fernet(key)
        encrypted = fernet.encrypt(data.encode())
        return encrypted.decode()

    @staticmethod
    def decrypt_data(encrypted_data: str, key: bytes) -> str:
        """Расшифровывает данные"""
        fernet = Fernet(key)
        decrypted = fernet.decrypt(encrypted_data.encode())
        return decrypted.decode()

    @staticmethod
    def hash_password(password: str) -> str:
        """Хеширует пароль с использованием SHA-256"""
        return hashlib.sha256(password.encode()).hexdigest()
