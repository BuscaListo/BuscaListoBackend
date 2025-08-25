from sqlalchemy import Column, Integer, String, Boolean, DateTime
from app.infrastructure.base import Base


class PermissionCatalogORM(Base):
    __tablename__ = "catalogo_permisos"

    # Campos de identificación
    id = Column(Integer, primary_key=True, autoincrement=True)
    
    # Campos de información
    name = Column("nombre", String(100))
    
    # Campos de auditoría
    created_at = Column("creado", DateTime)
    created_by = Column("creado_por", String(255))
    active = Column("activo", Boolean, default=True)
