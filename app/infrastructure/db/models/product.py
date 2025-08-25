from sqlalchemy import Column, Integer, String, Float, Text, Boolean, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from app.infrastructure.base import Base
from app.infrastructure.db.models.subcategory import SubCategoryORM
from app.infrastructure.db.models.brand import BrandORM
from app.infrastructure.db.models.branch import BranchORM
# from app.infrastructure.db.models.image import ImageORM

class ProductORM(Base):
    __tablename__ = "producto"

    # Campos de identificación
    id = Column(Integer, primary_key=True, autoincrement=True)
    
    # Campos de información del producto
    name = Column("nombre", String, nullable=False)
    description = Column("descripcion", Text)
    price_bs = Column("precio_bs", Float, nullable=False)
    price_usd = Column("precio_dls", Float)
    images = Column("imagenes", Text)
    code = Column("codigo", String(150))
    in_stock = Column("in_stock", Integer, default=1)
    
    # Campos de relaciones
    subcategory_id = Column("id_sub_categoria", Integer, ForeignKey("subcategorias.id"), nullable=False)
    branch_id = Column("id_sucursal", Integer, ForeignKey("sucursales.id"), nullable=False)
    brand_id = Column("id_marca", Integer, ForeignKey("marcas.id"), nullable=False)
    
    # Campos de métricas
    views = Column("views", Integer, default=0)
    
    # Campos de auditoría
    created_at = Column("creado", DateTime)
    created_by = Column("creado_por", String(250))
    active = Column("activo", Integer, default=1)
    
    # Campos de características
    features = Column("caracteristicas", Text)
    advanced_features = Column("caracteristicas_avanzada", Text)

    # Relaciones
    subcategory = relationship("SubCategoryORM", back_populates="products")
    images_rel = relationship("ImageORM", back_populates="product")
