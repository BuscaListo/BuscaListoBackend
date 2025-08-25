from sqlalchemy import Column, Integer, String, DateTime, Numeric, ForeignKey
from app.infrastructure.base import Base


class PriceHistoryORM(Base):
    __tablename__ = "bitacora_precio_producto"

    # Campos de identificación
    id = Column(Integer, primary_key=True, autoincrement=True)
    
    # Campos de relaciones
    product_id = Column("id_producto", Integer, ForeignKey("producto.id"), nullable=False)
    
    # Campos de información
    current_price = Column("precio_actualizado", Numeric(10, 2))
    new_price = Column("precio_nuevo", Numeric(10, 2))
    percentage = Column("porcentaje", Numeric(5, 2))
    
    # Campos de auditoría
    created_at = Column("creado", DateTime)
    created_by = Column("creado_por", String(255))
