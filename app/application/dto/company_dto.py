from datetime import datetime
from typing import Optional
from pydantic import BaseModel


class CompanyResponseDTO(BaseModel):
    """DTO para respuesta de empresas con información enriquecida"""
    id: int
    name: str
    phone: Optional[str] = None
    logo: Optional[str] = None
    location_name: Optional[str] = None
    branches_count: int = 0
    products_count: int = 0
    created_at: Optional[datetime] = None
    active: bool = True

    class Config:
        from_attributes = True
