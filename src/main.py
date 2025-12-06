from fastapi import FastAPI 
from src.create_db import create_db
from contextlib import asynccontextmanager 
from fastapi.middleware.cors import CORSMiddleware
from src.routers.urlshorted import UrlRouter 
from src.routers.redirect import RedirectRouter

@asynccontextmanager
async def lifespan(app: FastAPI):
    await create_db()
    yield 

app = FastAPI(lifespan=lifespan)


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
redirect_router = RedirectRouter()
url_router = UrlRouter()

app.include_router(url_router.router)
app.include_router(redirect_router.router)
