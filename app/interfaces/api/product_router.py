from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app.application.dto.producto_dto import (
    ProductResponseDTO,
    RecentProductResponseDTO,
    ProductCreateDTO,
    ProductUpdateDTO,
)
from app.application.use_cases.get_product import get_product_use_case
from app.application.use_cases.list_products import list_products_use_case
from app.application.use_cases.create_product import create_product_use_case
from app.application.use_cases.update_product import update_product_use_case
from app.application.use_cases.delete_product import delete_product_use_case
from app.application.use_cases.get_top3_recent_products import (
    get_top3_recent_products_use_case,
)
from app.infrastructure.session import get_db

router = APIRouter(prefix="/productos", tags=["Productos"])

@router.get("/", response_model=List[ProductResponseDTO])
def list_products(db: Session = Depends(get_db)):
    productos = list_products_use_case(db)
    return [ProductResponseDTO.model_validate(p) for p in productos]

@router.get("/{product_id}", response_model=ProductResponseDTO)
def get_product(product_id: int, db: Session = Depends(get_db)):
    producto = get_product_use_case(db, product_id)
    if not producto:
        raise HTTPException(status_code=404, detail="Producto no encontrado")
    
    return ProductResponseDTO.model_validate(producto)

@router.post("/", response_model=ProductResponseDTO, status_code=201)
def create_product(payload: ProductCreateDTO, db: Session = Depends(get_db)):
    producto = create_product_use_case(db, payload)
    return ProductResponseDTO.model_validate(producto)

@router.patch("/{product_id}", response_model=ProductResponseDTO)
def update_product(product_id: int, payload: ProductUpdateDTO, db: Session = Depends(get_db)):
    producto = update_product_use_case(db, product_id, payload)
    if not producto:
        raise HTTPException(status_code=404, detail="Producto no encontrado")
    return ProductResponseDTO.model_validate(producto)

@router.put("/{product_id}", response_model=ProductResponseDTO)
def replace_product(product_id: int, payload: ProductCreateDTO, db: Session = Depends(get_db)):
    updates = ProductUpdateDTO(**payload.model_dump())
    producto = update_product_use_case(db, product_id, updates)
    if not producto:
        raise HTTPException(status_code=404, detail="Producto no encontrado")
    return ProductResponseDTO.model_validate(producto)

@router.delete("/{product_id}", status_code=204)
def delete_product(product_id: int, db: Session = Depends(get_db)):
    eliminado = delete_product_use_case(db, product_id)
    if not eliminado:
        raise HTTPException(status_code=404, detail="Producto no encontrado")
    return None

@router.get("/top/recientes", response_model=List[RecentProductResponseDTO])
def get_top3_recent_products(db: Session = Depends(get_db)):
    productos = get_top3_recent_products_use_case(db)
    return [RecentProductResponseDTO.model_validate(p) for p in productos]
