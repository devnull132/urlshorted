from fastapi import APIRouter, Depends
from starlette.responses import RedirectResponse 
from src.services.urlshorted_servies import UrlShortServies, get_urlshort_service

class RedirectRouter:
    def __init__(self):
        self.router = APIRouter(tags=["Redirect"])
        self._setup_routers()

    def _setup_routers(self):
        self.router.get("/{code}")(self.redirect_to_url)

    async def redirect_to_url(self, code: str, urlshort_servies: UrlShortServies = Depends(get_urlshort_service)):
        target_url = await urlshort_servies.redirect_by_code(code)
        return RedirectResponse(
            url=target_url,
            status_code=307
        )
