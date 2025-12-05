from src.database import Base, intpk
from sqlalchemy.orm import Mapped

class Url(Base):
    __tablename__ = "url"

    id: Mapped[intpk]
    url: Mapped[str]
    def_address: Mapped[str]
    code: Mapped[str]
    created_at: Mapped[str]
    expires_at: Mapped[str] 
