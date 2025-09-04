from sqlalchemy import Column, Integer, String, Text, Boolean, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from app.infrastructure.base import Base


class BranchORM(Base):
    __tablename__ = "sucursales"

    # Campos de identificación
    id = Column(Integer, primary_key=True, autoincrement=True)
    
    # Campos de información
    name = Column("nombre", String, nullable=False)
    images = Column("imagenes", Text)
    
    # Campos de relaciones
    company_id = Column("id_empresa", Integer, ForeignKey("empresa.id"), nullable=False)
    location_id = Column("id_ubicacion", Integer, ForeignKey("ubicaciones.id"), nullable=False)
    user_id = Column("id_usuario", Integer, nullable=False)
    
    # Campos de auditoría
    created_at = Column("creado", DateTime)
    created_by = Column("creado_por", String(255))
    active = Column("activo", Boolean, default=True)
