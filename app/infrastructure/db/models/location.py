from sqlalchemy import Column, Integer, String, Boolean, DateTime, Numeric
from app.infrastructure.base import Base


class LocationORM(Base):
    __tablename__ = "ubicaciones"

    # Campos de identificación
    id = Column(Integer, primary_key=True, autoincrement=True)
    
    # Campos de información
    name = Column("nombre", String, nullable=False)
    latitude = Column("latitud", Numeric(10, 8), nullable=False)
    longitude = Column("longitud", Numeric(10, 8), nullable=False)
    
    # Campos de auditoría
    created_at = Column("creado", DateTime)
    created_by = Column("creado_por", String(255))
    active = Column("activo", Boolean, default=True)
