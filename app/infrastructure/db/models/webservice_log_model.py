from sqlalchemy import Column, Integer, String, Text, DateTime
from app.infrastructure.base import Base


class WebServiceLogORM(Base):
    __tablename__ = "webservice_log"

    id = Column(Integer, primary_key=True, autoincrement=True)
    id_web_service = Column(Integer, nullable=False)
    input = Column(Text)
    error = Column(Text)
    creado = Column(DateTime)
    creado_por = Column(String(255))

