from pydantic import BaseModel, HttpUrl  

class ShortUrlResponse(BaseModel):
    code: str
    url: str 
    def_address: str
    created_at: str    
    expires_at: str

class GetDefAddress(BaseModel):
    def_address: HttpUrl
