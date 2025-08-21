from sqlalchemy import Column, Integer, String, Boolean, DateTime
from app.infrastructure.base import Base


class WebServiceORM(Base):
    __tablename__ = "web_service"

    id = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String(100))
    descripcion = Column(String(255))
    url = Column(String(255))
    creado = Column(DateTime)
    creado_por = Column(String(255))
    activo = Column(Boolean, default=True)

