from sqlalchemy import Column, Integer, String, Text, Boolean, DateTime, ForeignKey
from app.infrastructure.base import Base


class SucursalORM(Base):
    __tablename__ = "sucursales"

    id = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String, nullable=False)
    imagenes = Column(Text)
    id_empresa = Column(Integer, ForeignKey("empresa.id"), nullable=False)
    id_ubicacion = Column(Integer, ForeignKey("ubicaciones.id"), nullable=False)
    id_usuario = Column(Integer, nullable=False)
    creado = Column(DateTime)
    creado_por = Column(String(255))
    activo = Column(Boolean, default=True)

