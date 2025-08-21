from sqlalchemy import Column, Integer, String, Boolean, DateTime, Numeric
from app.infrastructure.base import Base


class SubscripcionORM(Base):
    __tablename__ = "subscripciones"

    id = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String(100))
    precio = Column(Numeric(10, 2))
    anuncios = Column(String(150), default='N')
    prioridad_listado = Column(String(150), default='N')
    ubicaciones = Column(String(150), default='N')
    estadisticas = Column(String(150), default='N')
    soporte = Column(String(150), default='N')
    extras = Column(String(150), default='N')
    creado = Column(DateTime)
    creado_por = Column(String(255))
    activo = Column(Boolean, default=True)

