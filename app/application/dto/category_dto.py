from datetime import datetime
from typing import Optional
from pydantic import BaseModel


class CategoryResponseDTO(BaseModel):
    id: int
    name: str
    description: str
    image_urls: Optional[list[str]] = []

    class Config:
        from_attributes = True
