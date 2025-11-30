from fastapi import APIRouter 
from src.schemas.url import GetDefAddress
from src.services.urlshorted_servies import UrlShortServies, get_urlshort_service

class UrlRouter:
    def __init__(self):
        self.router = APIRouter(tags=["UrlShortener"], prefix="/urlshort")
        self._setup_routers()

    def _setup_routers(self):
        self.router.post("get_def_address")(self.create_url_short)

    async def create_url_short(self, def_address: GetDefAddress):

        return def_address.def_address
