from datetime import datetime
from typing import Optional
from pydantic import BaseModel

class ProductResponseDTO(BaseModel):
    id: int
    name: str
    brand: int
    price: float
    category: str
    precio_dls: Optional[float]
    imageUrl: Optional[str]
    stock: bool
    offerDescription: Optional[str]
    supplier: Optional[int]
    availableOnline: bool
    views: int
    activo: bool
    creado: datetime

    class Config:
        from_attributes = True
