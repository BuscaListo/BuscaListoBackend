from sqlalchemy import Column, Integer, String, Boolean, DateTime
from app.infrastructure.base import Base


class WebServiceORM(Base):
    __tablename__ = "web_service"

    # Campos de identificación
    id = Column(Integer, primary_key=True, autoincrement=True)
    
    # Campos de información
    name = Column("nombre", String(100))
    description = Column("descripcion", String(255))
    url = Column("url", String(255))
    
    # Campos de auditoría
    created_at = Column("creado", DateTime)
    created_by = Column("creado_por", String(255))
    active = Column("activo", Boolean, default=True)
