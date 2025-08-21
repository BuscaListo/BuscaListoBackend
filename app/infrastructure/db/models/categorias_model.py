from sqlalchemy import Column, Integer, String, Text, Boolean, DateTime
from app.infrastructure.base import Base


class CategoriaORM(Base):
    __tablename__ = "categorias"

    id = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String, nullable=False)
    imagenes = Column(Text)
    creado = Column(DateTime)
    creado_por = Column(String(255))
    activo = Column(Boolean, default=True)

