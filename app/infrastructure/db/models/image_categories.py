from sqlalchemy import (
    Column,
    BigInteger,
    String,
    Integer,
    Boolean,
    ForeignKey,
    DateTime,
    func,
)
from app.infrastructure.base import Base
from sqlalchemy.orm import relationship
from app.infrastructure.db.models import CategoryORM

class ImageCategoryORM(Base):
    __tablename__ = "imagenes_categorias"

    # Campos de identificación
    id = Column(BigInteger, primary_key=True, autoincrement=True)
    
    # Campos de información
    url = Column("url", String(250), nullable=False)
    category_id = Column("id_categoria", BigInteger, ForeignKey("categorias.id"), nullable=False)

    # Campos de auditoría
    created_at = Column("creado", DateTime, default=func.now())
    created_by = Column("creado_por", String(255))
    active = Column("activo", Boolean, default=True)

    # Relación opcional con CategoryORM
    category = relationship("CategoryORM", back_populates="images_categories_rel")