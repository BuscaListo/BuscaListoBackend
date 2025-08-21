from sqlalchemy import Column, Integer, String, Text, Boolean, DateTime, ForeignKey, Numeric
from app.infrastructure.base import Base


class OfertaORM(Base):
    __tablename__ = "ofertas"

    id = Column(Integer, primary_key=True, autoincrement=True)
    descripcion = Column(Text, nullable=False)
    porcentaje = Column(Numeric(5, 2))
    id_producto = Column(Integer, ForeignKey("producto.id"))
    id_categoria = Column(Integer, ForeignKey("categorias.id"))
    id_sub_categoria = Column(Integer, ForeignKey("subcategorias.id"))
    creado = Column(DateTime)
    creado_por = Column(String(255))
    activo = Column(Boolean, default=True)

