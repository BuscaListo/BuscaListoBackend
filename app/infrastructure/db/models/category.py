from sqlalchemy import Column, Integer, String, Text, Boolean, DateTime
from app.infrastructure.base import Base


class CategoryORM(Base):
    __tablename__ = "categorias"

    # Campos de identificación
    id = Column(Integer, primary_key=True, autoincrement=True)
    
    # Campos de información
    name = Column("nombre", String, nullable=False)
    images = Column("imagenes", Text)
    
    # Campos de auditoría
    created_at = Column("creado", DateTime)
    created_by = Column("creado_por", String(255))
    active = Column("activo", Boolean, default=True)
