from sqlalchemy import Column, Integer, String, Text, Boolean, DateTime, ForeignKey
from app.infrastructure.base import Base


class StockORM(Base):
    __tablename__ = "stock"

    # Campos de identificación
    id = Column(Integer, primary_key=True, autoincrement=True)
    
    # Campos de relaciones
    product_id = Column("id_producto", Integer, ForeignKey("producto.id"), nullable=False)
    
    # Campos de cantidad
    total_quantity = Column("cantidad_total", Integer)
    sold_quantity = Column("cantidad_vendida", Integer)
    offered_quantity = Column("cantidad_ofertada", Integer)
    
    # Campos de auditoría
    created_at = Column("creado", DateTime)
    created_by = Column("creado_por", String(255))
    active = Column("activo", Boolean, default=True)
