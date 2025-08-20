from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.application.dto.producto_dto import ProductResponseDTO
from app.application.use_cases.get_product import get_product_use_case
from app.infrastructure.session import get_db

router = APIRouter(prefix="/productos", tags=["Productos"])

@router.get("/{product_id}", response_model=ProductResponseDTO)
def get_product(product_id: int, db: Session = Depends(get_db)):
    producto = get_product_use_case(db, product_id)
    if not producto:
        raise HTTPException(status_code=404, detail="Producto no encontrado")
    
    return ProductResponseDTO.model_validate(producto)
