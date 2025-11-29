from database import Base, intpk, created_at, updated_at
from sqlalchemy.orm import Mapped, mapped_column 

class Url(Base):
    __tablename__ = "url"

    id: Mapped[intpk]
    def_address: Mapped[str]
    code: Mapped[str]

