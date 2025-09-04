"""
Router de empresas/tiendas
"""

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app.application.dto.company_dto import CompanyResponseDTO
from app.application.use_cases.list_companies import list_companies_use_case

from app.infrastructure.session import get_db

router = APIRouter(prefix="/companies", tags=["Companies"])


@router.get("/", response_model=List[CompanyResponseDTO])
def list_companies(db: Session = Depends(get_db)):
    """
    Lista todas las empresas/tiendas activas con información adicional.
    
    Returns:
        Lista de empresas con número de sucursales y productos
    """
    companies = list_companies_use_case(db)
    
    if not companies:
        raise HTTPException(
            status_code=404, 
            detail="No se encontraron empresas activas"
        )
    
    return [CompanyResponseDTO.model_validate(company) for company in companies]
