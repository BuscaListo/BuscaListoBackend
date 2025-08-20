from datetime import datetime
from typing import Optional
from pydantic import BaseModel

class ProductResponseDTO(BaseModel):
    id: int
    name: str
    brand: int
    price: float
    # category
    subcategory: int
    # precio_dls: Optional[float]
    imageUrl: Optional[str]
    stock: bool
    # url
    offerDescription: Optional[str]
    requirePrescription: Optional[bool]
    supplier: Optional[str]
    availableOnline: bool
    views: int
    # activo: bool
    creado: datetime

    class Config:
        from_attributes = True
