from sqlalchemy import Column, Integer, String, Text, DateTime
from app.infrastructure.base import Base


class WebServiceLogORM(Base):
    __tablename__ = "webservice_log"

    # Campos de identificación
    id = Column(Integer, primary_key=True, autoincrement=True)
    
    # Campos de relaciones
    web_service_id = Column("id_web_service", Integer, nullable=False)
    
    # Campos de información
    input_data = Column("input", Text)
    error = Column("error", Text)
    
    # Campos de auditoría
    created_at = Column("creado", DateTime)
    created_by = Column("creado_por", String(255))
