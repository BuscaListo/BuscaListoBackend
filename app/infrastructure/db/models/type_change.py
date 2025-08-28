from sqlalchemy import Column, Numeric
from app.infrastructure.base import Base


class TypeChange(Base):
    __tablename__ = "type_changes"

    dolar = Column("dolar", Numeric, nullable=True)
    rublo = Column("rublo", Numeric, nullable=True)
    lira = Column("lira", Numeric, nullable=True)
    yuan = Column("yuan", Numeric, nullable=True)
    euro = Column("euro", Numeric, nullable=True)
    