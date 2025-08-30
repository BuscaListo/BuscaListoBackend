from datetime import datetime
from typing import Optional
from pydantic import BaseModel


class OfferProductResponseDTO(BaseModel):
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
    offer_id: Optional[int] = None
    discount_percent: Optional[float] = None
    offer_start_date: Optional[datetime] = None
    offer_end_date: Optional[datetime] = None
    price_offer_usd: Optional[float] = None
    price_offer_bs: Optional[float] = None

    class Config:
        from_attributes = True