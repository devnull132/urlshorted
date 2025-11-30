from pydantic import BaseModel, HttpUrl  
from datetime import datetime 

class UrlShortedResponse(BaseModel):
    def_address: str 
    url: str 
    expires_at: datetime 
    url_from_stat: str 

class GetDefAddress(BaseModel):
    def_address: HttpUrl
