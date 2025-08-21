from sqlalchemy import Column, Integer, String, Boolean, DateTime, Date, ForeignKey
from app.infrastructure.base import Base


class EstadisticasPublicidadORM(Base):
    __tablename__ = "estadisticas_publicidad"

    id = Column(Integer, primary_key=True, autoincrement=True)
    id_publicidad = Column(Integer, ForeignKey("publicidades.id"))
    impresiones = Column(Integer)
    clics = Column(Integer)
    fecha = Column(Date)
    creado = Column(DateTime)
    creado_por = Column(String(255))
    activo = Column(Boolean, default=True)

