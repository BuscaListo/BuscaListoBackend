from sqlalchemy import Column, Integer, String, Boolean, DateTime, Numeric
from app.infrastructure.base import Base


class SubscriptionORM(Base):
    __tablename__ = "subscripciones"

    # Campos de identificación
    id = Column(Integer, primary_key=True, autoincrement=True)
    
    # Campos de información
    name = Column("nombre", String(100))
    price = Column("precio", Numeric(10, 2))
    ads = Column("anuncios", String(150), default='N')
    listing_priority = Column("prioridad_listado", String(150), default='N')
    locations = Column("ubicaciones", String(150), default='N')
    statistics = Column("estadisticas", String(150), default='N')
    support = Column("soporte", String(150), default='N')
    extras = Column("extras", String(150), default='N')
    
    # Campos de auditoría
    created_at = Column("creado", DateTime)
    created_by = Column("creado_por", String(255))
    active = Column("activo", Boolean, default=True)
