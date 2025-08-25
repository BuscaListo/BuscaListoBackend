from sqlalchemy import Column, Integer, String, Text, Boolean, DateTime, Date, ForeignKey
from app.infrastructure.base import Base


class AdvertisementORM(Base):
    __tablename__ = "publicidades"

    # Campos de identificación
    id = Column(Integer, primary_key=True, autoincrement=True)
    
    # Campos de relaciones
    branch_id = Column("id_sucursal", Integer, ForeignKey("sucursales.id"), nullable=False)
    
    # Campos de información
    ad_images = Column("imagenes_publicidad", Text)
    destination_link = Column("link_destino", String(300))
    priority = Column("prioridad", Integer)
    start_date = Column("fecha_inicio", Date)
    end_date = Column("fecha_fin", Date)
    
    # Campos de auditoría
    active = Column("activo", Boolean, default=True)
    created_at = Column("creado", DateTime)
