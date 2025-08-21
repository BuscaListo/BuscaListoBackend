from sqlalchemy import Column, Integer, String, Boolean, DateTime, Numeric
from app.infrastructure.base import Base


class UbicacionORM(Base):
    __tablename__ = "ubicaciones"

    id = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String, nullable=False)
    latitud = Column(Numeric(10, 8), nullable=False)
    longitud = Column(Numeric(10, 8), nullable=False)
    creado = Column(DateTime)
    creado_por = Column(String(255))
    activo = Column(Boolean, default=True)

