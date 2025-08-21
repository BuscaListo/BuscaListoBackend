from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey
from app.infrastructure.base import Base


class PermisosUsuariosORM(Base):
    __tablename__ = "permisos_usuarios"

    id = Column(Integer, primary_key=True, autoincrement=True)
    id_usuario = Column(Integer, ForeignKey("usuario.id"))
    id_catalogo_permiso = Column(Integer, ForeignKey("catalogo_permisos.id"))
    read = Column(Boolean, default=False)
    write = Column(Boolean, default=False)
    delete = Column(Boolean, default=False)
    edit = Column(Boolean, default=False)
    creado = Column(DateTime)
    creado_por = Column(String(255))
    activo = Column(Boolean, default=True)

