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
from sqlalchemy.orm import relationship
from app.infrastructure.db.models import ProductORM
from app.infrastructure.base import Base  # tu Base declarada en el proyecto


class ImageORM(Base):
    __tablename__ = "imagenes"

    # Campos de identificación
    id = Column(BigInteger, primary_key=True, autoincrement=True)
    
    # Campos de información
    url = Column("url", String(150), nullable=False)
    product_id = Column("id_producto", BigInteger, ForeignKey("producto.id"), nullable=False)
    
    # Campos de auditoría
    created_at = Column("creado", DateTime, default=func.now())
    created_by = Column("creado_por", String(255))
    active = Column("activo", Boolean, default=True)

    # Relación opcional con ProductORM
    product = relationship("ProductORM", back_populates="images_rel")