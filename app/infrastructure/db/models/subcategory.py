from sqlalchemy import Column, Integer, String, Text, Boolean, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from app.infrastructure.base import Base

class SubCategoryORM(Base):
    __tablename__ = "subcategorias"

    # Campos de identificación
    id = Column(Integer, primary_key=True, autoincrement=True)
    
    # Campos de información
    name = Column("nombre", String, nullable=False)
    images = Column("imagenes", Text)
    category_id = Column("id_categoria", Integer, ForeignKey("categorias.id"), nullable=False)
    
    # Campos de auditoría
    created_at = Column("creado", DateTime)
    created_by = Column("creado_por", String(255))
    active = Column("activo", Boolean, default=True)

    # Relaciones
    products = relationship("ProductORM", back_populates="subcategory")
