# Сначала генерируем набор символов для сокращения ссылки, проверяем его на уникальность и даем время которое он будет "жить" и потом удалится
import string
import secrets  
from datetime import datetime, timedelta 

class Shortener:
    def __init__(self, base_url: str = "http://localhost:8000", code_length: int = 6):
        self.chars = string.ascii_letters + string.digits
        self.base_url = base_url
        self.code_length = code_length
    
    def generate_short_url(self):
        """
        генерирует короткую ссылку и возвращает информацию о ней
        """
        code = self.__generate_code()
        created_at = datetime.now()
        expires_at = created_at + timedelta(hours=24)
        url = f"{self.base_url}/{code}"
        
        return {
            "code": code, 
            "url": url,
            "created_at": created_at,
            "expires_at": expires_at 
        }

    def __generate_code(self):
        return ''.join(secrets.choice(self.chars) for _ in range(self.code_length))


