from src.utils.shortener import get_urlshortener, Shortener
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import HTTPException, Depends 
from src.database import get_db
from src.schemas.url import GetDefAddress

class UrlShortServies:
    def __init__(self, session: AsyncSession):
        self.session = session
        

    async def create_url_short(self, def_address: GetDefAddress, urlshortener: Shortener = Depends(get_urlshortener)):

        return def_address.def_address

async def get_urlshort_service(session: AsyncSession = Depends(get_db)):
    return UrlShortServies(session)
