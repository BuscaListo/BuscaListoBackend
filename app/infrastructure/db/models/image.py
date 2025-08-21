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
from app.infrastructure.db.models.product_model import ProductORM
from app.infrastructure.base import Base  # tu Base declarada en el proyecto


class ImageORM(Base):
    __tablename__ = "imagenes"

    id = Column(BigInteger, primary_key=True, autoincrement=True)
    url = Column(String(150), nullable=False)
    id_producto = Column(BigInteger, ForeignKey("producto.id"), nullable=False)
    creado = Column(DateTime, default=func.now())
    creado_por = Column(String(255))
    activo = Column(Boolean, default=True)

    # Relación opcional con ProductORM
    producto = relationship("ProductORM", back_populates="imagenes")