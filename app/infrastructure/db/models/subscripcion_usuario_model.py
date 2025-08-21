from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey
from app.infrastructure.base import Base


class SubscripcionUsuarioORM(Base):
    __tablename__ = "subscripcion_usuario"

    id = Column(Integer, primary_key=True, autoincrement=True)
    id_subscripcion = Column(Integer, ForeignKey("subscripciones.id"), nullable=False)
    id_usuario = Column(Integer, ForeignKey("usuario.id"), nullable=False)
    activo = Column(Boolean, default=True)
    creado = Column(DateTime)
    creado_por = Column(String(250))

