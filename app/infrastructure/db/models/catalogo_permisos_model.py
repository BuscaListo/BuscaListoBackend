from sqlalchemy import Column, Integer, String, Boolean, DateTime
from app.infrastructure.base import Base


class CatalogoPermisosORM(Base):
    __tablename__ = "catalogo_permisos"

    id = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String(100))
    creado = Column(DateTime)
    creado_por = Column(String(255))
    activo = Column(Boolean, default=True)

