from sqlalchemy import select
from src.models.url_model import Url
from src.utils.shortener import Shortener
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import HTTPException, Depends 
from src.database import get_db
from datetime import datetime

class UrlShortServies:
    def __init__(self, session: AsyncSession):
        self.session = session
        

    async def create_url_short(self, def_address: str):
        shortener = Shortener(self.session)
        url_info = await shortener.generate_short_url(def_address=def_address)
        url_entry = Url(
        url=url_info.url,
        code=url_info.code,
        def_address=url_info.def_address,
        created_at=url_info.created_at,
        expires_at=url_info.expires_at
    )
    
        self.session.add(url_entry)
        await self.session.commit()
        return url_info
    
    async def redirect_by_code(self, code: str):
        query = select(Url).filter(Url.code == code)
        result = await self.session.execute(query)
        url_entry = result.scalar_one_or_none()
        
        if not url_entry:
            raise HTTPException(status_code=404, detail="Ссылка не найдена")
        
        expires_at = datetime.strptime(url_entry.expires_at, "%d.%m.%Y, %H:%M")
        current_time = datetime.now()

        if current_time > expires_at:
            await self.session.delete(url_entry)
            await self.session.commit()
            raise HTTPException(
                status_code=410, 
                detail="Ссылка истекла и была удалена"
            )
        
        return url_entry.def_address

async def get_urlshort_service(session: AsyncSession = Depends(get_db)):
    return UrlShortServies(session)
