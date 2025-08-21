from sqlalchemy import Column, Integer, String, Boolean, DateTime
from app.infrastructure.base import Base


class UsuarioORM(Base):
    __tablename__ = "usuario"

    id = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String(100))
    email = Column(String(255), unique=True)
    password = Column(String(255))
    creado = Column(DateTime)
    creado_por = Column(String(255))
    activo = Column(Boolean, default=True)

