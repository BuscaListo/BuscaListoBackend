"""
Router de ofertas
"""

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List
from app.application.dto.offer_product_dto import (
    OfferProductResponseDTO
)
from app.application.use_cases.list_offer_products import list_offer_products_use_case

from app.infrastructure.session import get_db

router = APIRouter(prefix="/offers", tags=["Offers"])


@router.get("/products", response_model=List[OfferProductResponseDTO])
def list_offers_products(db: Session = Depends(get_db)):
    """
    List all offers products.
    """
    offers_product = list_offer_products_use_case(db)
    for offer in offers_product:
        print(offer.__dict__)
    return [OfferProductResponseDTO.model_validate(offer) for offer in offers_product]
