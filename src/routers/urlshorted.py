from fastapi import APIRouter, Depends
from src.schemas.url import GetDefAddress
from src.services.urlshorted_servies import UrlShortServies, get_urlshort_service

class UrlRouter:
    def __init__(self):
        self.router = APIRouter(tags=["UrlShortener"], prefix="/urlshort")
        self._setup_routers()

    def _setup_routers(self):
        self.router.post("/create_short_url")(self.create_short_url)

    async def create_short_url(self, def_address: GetDefAddress, urlshort_servies: UrlShortServies = Depends(get_urlshort_service)):
        info_url = await urlshort_servies.create_url_short(def_address=str(def_address.def_address))
        return info_url



        
