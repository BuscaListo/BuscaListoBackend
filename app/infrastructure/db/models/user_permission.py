from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey
from app.infrastructure.base import Base


class UserPermissionORM(Base):
    __tablename__ = "permisos_usuarios"

    # Campos de identificación
    id = Column(Integer, primary_key=True, autoincrement=True)
    
    # Campos de relaciones
    user_id = Column("id_usuario", Integer, ForeignKey("usuario.id"))
    permission_catalog_id = Column("id_catalogo_permiso", Integer, ForeignKey("catalogo_permisos.id"))
    
    # Campos de permisos
    read = Column("read", Boolean, default=False)
    write = Column("write", Boolean, default=False)
    delete = Column("delete", Boolean, default=False)
    edit = Column("edit", Boolean, default=False)
    
    # Campos de auditoría
    created_at = Column("creado", DateTime)
    created_by = Column("creado_por", String(255))
    active = Column("activo", Boolean, default=True)
