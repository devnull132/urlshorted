from src.models.url_model import Url
from src.utils.shortener import get_urlshortener, Shortener
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import HTTPException, Depends 
from src.database import get_db

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
    
    

async def get_urlshort_service(session: AsyncSession = Depends(get_db)):
    return UrlShortServies(session)
