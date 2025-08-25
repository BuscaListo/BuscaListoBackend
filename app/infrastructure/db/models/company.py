from sqlalchemy import Column, Integer, String, Text, Boolean, DateTime, ForeignKey
from app.infrastructure.base import Base


class CompanyORM(Base):
    __tablename__ = "empresa"

    # Campos de identificación
    id = Column(Integer, primary_key=True, autoincrement=True)
    
    # Campos de información
    name = Column("nombre", String, nullable=False)
    phone = Column("telefono", String(20))
    location_id = Column("id_ubicacion", Integer, ForeignKey("ubicaciones.id"), nullable=False)
    logo = Column("logo", Text)
    
    # Campos de auditoría
    created_at = Column("creado", DateTime)
    created_by = Column("creado_por", String(255))
    active = Column("activo", Boolean, default=True)
