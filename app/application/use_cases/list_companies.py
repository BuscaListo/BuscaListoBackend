from typing import List
from sqlalchemy.orm import Session
from sqlalchemy import func, distinct
from app.infrastructure.db.models import (
    CompanyORM, 
    BranchORM,
    ProductORM,
    LocationORM
)


def list_companies_use_case(db: Session) -> List[CompanyORM]:
    """
    Obtiene todas las empresas activas con información adicional como:
    - Número de sucursales
    - Número de productos
    - Ubicación principal
    
    Args:
        db: Sesión de base de datos
    
    Returns:
        Lista de empresas con información enriquecida
    """
    
    # Subconsulta para contar sucursales por empresa
    branches_count_subq = (
        db.query(
            BranchORM.company_id.label("company_id"),
            func.count(BranchORM.id).label("branches_count")
        )
        .filter(BranchORM.active == True)
        .group_by(BranchORM.company_id)
        .subquery()
    )
    
    # Subconsulta para contar productos por empresa
    products_count_subq = (
        db.query(
            BranchORM.company_id.label("company_id"),
            func.count(ProductORM.id).label("products_count")
        )
        .join(ProductORM, ProductORM.branch_id == BranchORM.id)
        .filter(
            BranchORM.active == True,
            ProductORM.active == 1
        )
        .group_by(BranchORM.company_id)
        .subquery()
    )
    
    # Consulta principal con joins
    query = (
        db.query(
            CompanyORM,
            LocationORM.name.label("location_name"),
            func.coalesce(branches_count_subq.c.branches_count, 0).label("branches_count"),
            func.coalesce(products_count_subq.c.products_count, 0).label("products_count")
        )
        .join(LocationORM, LocationORM.id == CompanyORM.location_id)
        .outerjoin(branches_count_subq, branches_count_subq.c.company_id == CompanyORM.id)
        .outerjoin(products_count_subq, products_count_subq.c.company_id == CompanyORM.id)
        .filter(CompanyORM.active == True)
        .order_by(CompanyORM.name.asc())
    )
    
    # Ejecutar consulta
    rows = query.all()
    
    # Procesar resultados
    companies: List[CompanyORM] = []
    for company_orm, location_name, branches_count, products_count in rows:
        # Crear un nuevo objeto con los atributos adicionales
        company_data = CompanyORM()
        company_data.id = company_orm.id
        company_data.name = company_orm.name
        company_data.phone = company_orm.phone
        company_data.logo = company_orm.logo
        company_data.location_id = company_orm.location_id
        company_data.created_at = company_orm.created_at
        company_data.created_by = company_orm.created_by
        company_data.active = company_orm.active
        
        # Asignar valores adicionales
        company_data.location_name = location_name
        company_data.branches_count = branches_count
        company_data.products_count = products_count
        
        companies.append(company_data)
    
    return companies
