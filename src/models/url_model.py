from src.database import Base, intpk, created_at, updated_at
from sqlalchemy.orm import Mapped

class Url(Base):
    __tablename__ = "url"

    id: Mapped[intpk]
    def_address: Mapped[str]
    code: Mapped[str]
    created_at: Mapped[created_at]
    updated_at: Mapped[updated_at] 
