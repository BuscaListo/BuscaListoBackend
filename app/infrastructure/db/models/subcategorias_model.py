from sqlalchemy import Column, Integer, String, Text, Boolean, DateTime, ForeignKey
from app.infrastructure.base import Base


class SubCategoriaORM(Base):
    __tablename__ = "subcategorias"

    id = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String, nullable=False)
    imagenes = Column(Text)
    id_categoria = Column(Integer, ForeignKey("categorias.id"), nullable=False)
    creado = Column(DateTime)
    creado_por = Column(String(255))
    activo = Column(Boolean, default=True)

