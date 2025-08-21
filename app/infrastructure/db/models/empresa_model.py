from sqlalchemy import Column, Integer, String, Text, Boolean, DateTime, ForeignKey
from app.infrastructure.base import Base


class EmpresaORM(Base):
    __tablename__ = "empresa"

    id = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String, nullable=False)
    telefono = Column(String(20))
    id_ubicacion = Column(Integer, ForeignKey("ubicaciones.id"), nullable=False)
    logo = Column(Text)
    creado = Column(DateTime)
    creado_por = Column(String(255))
    activo = Column(Boolean, default=True)

