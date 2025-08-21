from sqlalchemy import Column, Integer, String, Text, Boolean, DateTime
from app.infrastructure.base import Base


class MarcaORM(Base):
    __tablename__ = "marcas"

    id = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String, nullable=False)
    descripcion = Column(Text)
    imagenes = Column(Text)
    logo = Column(Text)
    creado = Column(DateTime)
    creado_por = Column(String(255))
    activo = Column(Boolean, default=True)

