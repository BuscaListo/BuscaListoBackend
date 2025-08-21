from dataclasses import dataclass
from datetime import datetime
from typing import Optional

@dataclass
class Product:
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
    creado_por: Optional[str]