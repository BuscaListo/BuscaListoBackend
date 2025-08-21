from sqlalchemy import Column, Integer, String, Float, Text, Boolean, ForeignKey, DateTime
from app.infrastructure.base import Base

class ProductORM(Base):
    __tablename__ = "producto"

    id = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String, nullable=False)
    descripcion = Column(Text)
    precio_bs = Column(Float, nullable=False)
    precio_dls = Column(Float)
    imagenes = Column(Text)
    codigo = Column(String(150))
    in_stock = Column(Boolean, default=True)
    id_sub_categoria = Column(Integer, ForeignKey("subcategorias.id"), nullable=False)
    id_sucursal = Column(Integer, ForeignKey("sucursales.id"), nullable=False)
    id_marca = Column(Integer, ForeignKey("marcas.id"), nullable=False)
    creado = Column(DateTime)
    views = Column(Integer, default=0)
    creado_por = Column(String(250))
    activo = Column(Boolean, default=True)
    caracteristicas = Column(Text)
    caracteristicas_avanzada = Column(Text)
