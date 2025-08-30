"""
Router de categorias
"""

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app.application.dto.category_dto import (
    CategoryResponseDTO
)
from app.application.use_cases.list_category import list_categories_use_case

from app.infrastructure.session import get_db

router = APIRouter(prefix="/categories", tags=["Categories"])


@router.get("/", response_model=List[CategoryResponseDTO])
def list_categories(db: Session = Depends(get_db)):
    """
    List all categories.
    """
    categories = list_categories_use_case(db)
    for c in categories:
        print(c)
    return [CategoryResponseDTO.model_validate(c) for c in categories]
