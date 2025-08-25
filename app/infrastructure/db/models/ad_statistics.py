from sqlalchemy import Column, Integer, String, Boolean, DateTime, Date, ForeignKey
from app.infrastructure.base import Base


class AdStatisticsORM(Base):
    __tablename__ = "estadisticas_publicidad"

    # Campos de identificación
    id = Column(Integer, primary_key=True, autoincrement=True)
    
    # Campos de relaciones
    advertisement_id = Column("id_publicidad", Integer, ForeignKey("publicidades.id"))
    
    # Campos de métricas
    impressions = Column("impresiones", Integer)
    clicks = Column("clics", Integer)
    date = Column("fecha", Date)
    
    # Campos de auditoría
    created_at = Column("creado", DateTime)
    created_by = Column("creado_por", String(255))
    active = Column("activo", Boolean, default=True)
