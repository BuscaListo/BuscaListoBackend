from sqlalchemy import Column, Integer, String, DateTime, Numeric, ForeignKey
from app.infrastructure.base import Base


class BitacoraPrecioProductoORM(Base):
    __tablename__ = "bitacora_precio_producto"

    id = Column(Integer, primary_key=True, autoincrement=True)
    id_producto = Column(Integer, ForeignKey("producto.id"), nullable=False)
    precio_actualizado = Column(Numeric(10, 2))
    precio_nuevo = Column(Numeric(10, 2))
    porcentaje = Column(Numeric(5, 2))
    creado = Column(DateTime)
    creado_por = Column(String(255))

