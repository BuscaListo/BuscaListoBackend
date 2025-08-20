from dataclasses import dataclass
from datetime import datetime
from typing import Optional

@dataclass
class Product:
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