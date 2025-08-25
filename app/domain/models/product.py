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
    price_usd: Optional[float]
    stock: bool
    offerDescription: Optional[str]
    supplier: Optional[int]
    availableOnline: bool
    views: int
    active: bool
    created_at: datetime
    imageUrl: Optional[str]
