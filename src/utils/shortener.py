import string
import secrets  
from datetime import datetime, timedelta
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession 
from fastapi import Depends 
from src.database import get_db
from src.models.url_model import Url
from src.schemas.url import ShortUrlResponse 

class Shortener:
    def __init__(self, session: AsyncSession, base_url ="http://localhost:8000", code_length=6):
        self.chars = string.ascii_letters + string.digits
        self.base_url = base_url
        self.code_length = code_length
        self.session = session  

    
    async def generate_short_url(self, def_address: str):
        
        code = self.__generate_code()
        unical = await self.__is_code_unique(code=code)

        while not unical:
            code = self.__generate_code()
            unical = await self.__is_code_unique(code=code) 

        created_at = datetime.now()
        expires_at = created_at + timedelta(hours=24)
        url = f"{self.base_url}/{code}"
        
        return ShortUrlResponse(
            code=code,
            url=url,
            def_address=def_address,
            created_at=created_at.strftime("%d.%m.%Y, %H:%M"),
            expires_at=expires_at.strftime("%d.%m.%Y, %H:%M"),
        )
        

    def __generate_code(self):
        return ''.join(secrets.choice(self.chars) for _ in range(self.code_length))

    async def __is_code_unique(self, code: str):
        query = (
            select(Url)
            .filter(Url.code == code)
        )
        res = await self.session.execute(query)

        code_result = res.scalar_one_or_none()

        if not code_result:
            return True 

        return False

async def get_urlshortener(session: AsyncSession = Depends(get_db)):
    return Shortener(session)
