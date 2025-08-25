from datetime import datetime
from typing import Optional
from pydantic import BaseModel


class ProductResponseDTO(BaseModel):
    id: int
    name: str
    brand_id: int
    price_bs: float
    subcategory_id: int
    price_usd: Optional[float]
    in_stock: Optional[int]
    branch_id: Optional[int]
    active: bool
    views: int
    created_at: datetime
    # Campos que a veces no están:
    image_url: Optional[str] = None
    offer_description: Optional[str] = ""

    class Config:
        from_attributes = True


class RecentProductResponseDTO(BaseModel):
    id: int
    name: str
    brand_name: str  # nombre de la marca
    price_bs: float
    subcategory_name: str
    price_usd: Optional[float]
    in_stock: Optional[int]
    offer_description: Optional[str] = ""
    branch_id: Optional[int]
    active: bool
    views: int
    image_url: Optional[str]
    created_at: datetime

    class Config:
        from_attributes = True


class ProductCreateDTO(BaseModel):
    name: str
    description: Optional[str] = None
    price_bs: float
    price_usd: Optional[float] = None
    images: Optional[str] = None
    code: Optional[str] = None
    in_stock: Optional[int] = None
    subcategory_id: int
    branch_id: int
    brand_id: int
    created_by: Optional[str] = None
    features: Optional[str] = None
    advanced_features: Optional[str] = None


class ProductUpdateDTO(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    price_bs: Optional[float] = None
    price_usd: Optional[float] = None
    images: Optional[str] = None
    code: Optional[str] = None
    in_stock: Optional[int] = None
    subcategory_id: Optional[int] = None
    branch_id: Optional[int] = None
    brand_id: Optional[int] = None
    created_at: Optional[datetime] = None
    features: Optional[str] = None
    advanced_features: Optional[str] = None
