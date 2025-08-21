from sqlalchemy import Column, Integer, String, Text, Boolean, DateTime, Date, ForeignKey
from app.infrastructure.base import Base


class PublicidadORM(Base):
    __tablename__ = "publicidades"

    id = Column(Integer, primary_key=True, autoincrement=True)
    id_sucursal = Column(Integer, ForeignKey("sucursales.id"), nullable=False)
    imagenes_publicidad = Column(Text)
    link_destino = Column(String(300))
    prioridad = Column(Integer)
    fecha_inicio = Column(Date)
    fecha_fin = Column(Date)
    activo = Column(Boolean, default=True)
    creado = Column(DateTime)

