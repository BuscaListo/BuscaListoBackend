from sqlalchemy import Column, Integer, String, Float, DateTime, Boolean
from app.infrastructure.base import Base


class CurrencyORM(Base):
    __tablename__ = "moneda"

    # Campos de identificación
    id = Column(Integer, primary_key=True, autoincrement=True)
    
    # Campos de información
    currency = Column("divisa", String(50), nullable=False)
    price_bs = Column("precio_bs", Float, nullable=False)
    
    # Campos de auditoría
    created_at = Column("creado", DateTime)
    created_by = Column("creado_por", String(255))
    active = Column("activo", Boolean, default=True)
