from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey
from app.infrastructure.base import Base


class UserSubscriptionORM(Base):
    __tablename__ = "subscripcion_usuario"

    # Campos de identificación
    id = Column(Integer, primary_key=True, autoincrement=True)
    
    # Campos de relaciones
    subscription_id = Column("id_subscripcion", Integer, ForeignKey("subscripciones.id"), nullable=False)
    user_id = Column("id_usuario", Integer, ForeignKey("usuario.id"), nullable=False)
    
    # Campos de auditoría
    active = Column("activo", Boolean, default=True)
    created_at = Column("creado", DateTime)
    created_by = Column("creado_por", String(250))
