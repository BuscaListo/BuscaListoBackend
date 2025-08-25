from sqlalchemy import Column, Integer, String, Boolean, DateTime
from app.infrastructure.base import Base


class UserORM(Base):
    __tablename__ = "usuario"

    # Campos de identificación
    id = Column(Integer, primary_key=True, autoincrement=True)
    
    # Campos de información
    name = Column("nombre", String(100))
    email = Column("email", String(255), unique=True)
    password = Column("password", String(255))
    
    # Campos de auditoría
    created_at = Column("creado", DateTime)
    created_by = Column("creado_por", String(255))
    active = Column("activo", Boolean, default=True)
