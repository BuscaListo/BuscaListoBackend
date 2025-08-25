from sqlalchemy import Column, Integer, String, Text, Boolean, DateTime, ForeignKey, Numeric
from app.infrastructure.base import Base


class OfferORM(Base):
    __tablename__ = "ofertas"

    # Campos de identificación
    id = Column(Integer, primary_key=True, autoincrement=True)
    
    # Campos de información
    description = Column("descripcion", Text, nullable=False)
    percentage = Column("porcentaje", Numeric(5, 2))
    
    # Campos de relaciones
    product_id = Column("id_producto", Integer, ForeignKey("producto.id"))
    category_id = Column("id_categoria", Integer, ForeignKey("categorias.id"))
    subcategory_id = Column("id_sub_categoria", Integer, ForeignKey("subcategorias.id"))
    
    # Campos de auditoría
    created_at = Column("creado", DateTime)
    created_by = Column("creado_por", String(255))
    active = Column("activo", Boolean, default=True)
