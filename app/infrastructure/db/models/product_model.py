from sqlalchemy import Column, Integer, String, Float, Text, Boolean, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from app.infrastructure.base import Base
from app.infrastructure.db.models.subcategorias_model import SubCategoriaORM
from app.infrastructure.db.models.marcas_model import MarcaORM
from app.infrastructure.db.models.sucursales_model import SucursalORM

class ProductORM(Base):
    __tablename__ = "producto"

    id = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String, nullable=False)
    descripcion = Column(Text)
    precio_bs = Column(Float, nullable=False)
    precio_dls = Column(Float)
    imagenes = Column(Text)
    codigo = Column(String(150))
    in_stock = Column(Integer, default=1)
    id_sub_categoria = Column(Integer, ForeignKey("subcategorias.id"), nullable=False)
    id_sucursal = Column(Integer, ForeignKey("sucursales.id"), nullable=False)
    id_marca = Column(Integer, ForeignKey("marcas.id"), nullable=False)
    views = Column(Integer, default=0)
    creado = Column(DateTime)
    creado_por = Column(String(250))
    activo = Column(Integer, default=1)
    caracteristicas = Column(Text)
    caracteristicas_avanzada = Column(Text)

    sub_categoria = relationship("SubCategoriaORM", back_populates="productos")