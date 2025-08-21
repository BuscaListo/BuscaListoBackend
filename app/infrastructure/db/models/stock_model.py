from sqlalchemy import Column, Integer, String, Text, Boolean, DateTime, ForeignKey
from app.infrastructure.base import Base


class StockORM(Base):
    __tablename__ = "stock"

    id = Column(Integer, primary_key=True, autoincrement=True)
    id_producto = Column(Integer, ForeignKey("producto.id"), nullable=False)
    cantidad_total = Column(Integer)
    cantidad_vendida = Column(Integer)
    cantidad_ofertada = Column(Integer)
    creado = Column(DateTime)
    creado_por = Column(String(255))
    activo = Column(Boolean, default=True)

