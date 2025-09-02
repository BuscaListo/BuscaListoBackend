"""
Router de productos refactorizado para usar alias en inglés.
Este es el router original pero usando los nuevos alias y mapeadores.
"""

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app.application.dto.product_dto import (
    ProductResponseDTO,
    RecentProductResponseDTO,
    ProductCreateDTO,
    ProductUpdateDTO,
    ProductDetailDTO,
)
from app.application.dto.offer_product_dto import OfferProductResponseDTO
from app.application.use_cases.get_product import get_product_use_case
from app.application.use_cases.list_products import list_products_use_case
from app.application.use_cases.create_product import create_product_use_case
from app.application.use_cases.update_product import update_product_use_case
from app.application.use_cases.delete_product import delete_product_use_case
from app.application.use_cases.get_product_detail import get_product_detail_use_case
from app.application.use_cases.get_top_recent_products import (
    get_top_recent_products_use_case,
)
from app.application.use_cases.get_most_viewed_products import (
    get_most_viewed_products_use_case,
)
from app.application.use_cases.list_offer_products import (
    list_offer_products_use_case,
)

from app.infrastructure.session import get_db


router = APIRouter(prefix="/products", tags=["Products"])


@router.get("/", response_model=List[ProductResponseDTO])
def list_products(db: Session = Depends(get_db)):
    """
    List all products.
    """
    products = list_products_use_case(db)
    for p in products:
        print(p.__dict__)
    return [ProductResponseDTO.model_validate(p) for p in products]


@router.get("/deals", response_model=List[OfferProductResponseDTO])
def list_offers_products_v2(db: Session = Depends(get_db)):
    """
    List all offers products.
    """

    offers_product = list_offer_products_use_case(db)
    for offer in offers_product:
        print(offer.__dict__)
    return [
        OfferProductResponseDTO.model_validate(offer)
        for offer in offers_product
    ]


@router.get("/{product_id}", response_model=ProductResponseDTO)
def get_product(product_id: int, db: Session = Depends(get_db)):
    """
    Get a specific product by ID.
    """
    product = get_product_use_case(db, product_id)
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")

    return ProductResponseDTO.model_validate(product)


@router.get("/{product_id}/detail", response_model=ProductDetailDTO)
def get_product_detail(product_id: int, db: Session = Depends(get_db)):
    """
    Get detailed information of a specific product by ID including all related data.
    This endpoint returns comprehensive product information including:
    - Product details
    - Brand information
    - Category and subcategory
    - Company/supplier information
    - Images
    - Offers
    - Mock comments
    """
    product_detail = get_product_detail_use_case(db, product_id)
    if not product_detail:
        raise HTTPException(status_code=404, detail="Product not found")

    return product_detail


@router.post("/", response_model=ProductResponseDTO, status_code=201)
def create_product(payload: ProductCreateDTO, db: Session = Depends(get_db)):
    """
    Create a new product.
    """
    product = create_product_use_case(db, payload)
    return ProductResponseDTO.model_validate(product)


@router.patch("/{product_id}", response_model=ProductResponseDTO)
def update_product(
    product_id: int, payload: ProductUpdateDTO, db: Session = Depends(get_db)
):
    """
    Update an existing product.
    """
    product = update_product_use_case(db, product_id, payload)
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    return ProductResponseDTO.model_validate(product)


@router.put("/{product_id}", response_model=ProductResponseDTO)
def replace_product(
    product_id: int, payload: ProductCreateDTO, db: Session = Depends(get_db)
):
    """
    Replace a product completely.
    """
    updates = ProductUpdateDTO(**payload.model_dump())
    product = update_product_use_case(db, product_id, updates)
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    return ProductResponseDTO.model_validate(product)


@router.delete("/{product_id}", status_code=204)
def delete_product(product_id: int, db: Session = Depends(get_db)):
    """
    Delete a product.
    """
    deleted = delete_product_use_case(db, product_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Product not found")
    return None


@router.get("/top/newest", response_model=List[RecentProductResponseDTO])
def get_top_recent_products(db: Session = Depends(get_db), items: int = 3):
    """
    Get the top n most recent products.
    """
    products = get_top_recent_products_use_case(db, items)
    for p in products:
        print(p.__dict__)

    return [RecentProductResponseDTO.model_validate(p) for p in products]


@router.get("/top/most-viewed", response_model=List[RecentProductResponseDTO])
def get_most_viewed_products(db: Session = Depends(get_db), items: int = 5):
    """
    Get the top n most viewed products.
    """
    products = get_most_viewed_products_use_case(db, items)
    return [RecentProductResponseDTO.model_validate(p) for p in products]
