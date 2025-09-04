from typing import List, Optional
from sqlalchemy.orm import Session
from sqlalchemy import func
import re
import unicodedata
from app.infrastructure.db.models import (
    ProductORM, 
    BrandORM, 
    SubCategoryORM, 
    CategoryORM,
    BranchORM,
    CompanyORM,
    ImageORM
)


def slugify(text: str) -> str:
    """Convierte un texto a una clave slug (sin espacios, caracteres especiales, etc.)"""
    text = unicodedata.normalize("NFKD", text).encode("ascii", "ignore").decode("utf-8")
    text = text.lower()
    text = re.sub(r'[^a-z0-9\s]', '', text)
    return text.replace(" ", "")


def get_products_by_company_use_case(
    db: Session, 
    company_name: str, 
    category_id: Optional[int] = None
) -> List[ProductORM]:
    """
    Obtiene todos los productos de una empresa específica, opcionalmente filtrados por categoría.
    
    Args:
        db: Sesión de base de datos
        company_name: Nombre de la empresa
        category_id: ID de la categoría para filtrar (opcional)
    
    Returns:
        Lista de productos de la empresa
    """
    
    # Subconsulta para elegir una única imagen por producto (la de menor id)
    image_per_product_subq = (
        db.query(
            ImageORM.product_id.label("id_producto"),
            func.min(ImageORM.id).label("min_image_id"),
        )
        .group_by(ImageORM.product_id)
        .subquery()
    )

    # Consulta base con joins necesarios
    query = (
        db.query(
            ProductORM,
            BrandORM.name.label("brand_name"),
            SubCategoryORM.name.label("subcategory_name"),
            CategoryORM.name.label("category_name"),
            CategoryORM.id.label("category_id"),
            CompanyORM.name.label("company_name"),
            BranchORM.name.label("branch_name"),
            ImageORM.url.label("image_url"),
        )
        .join(BrandORM, BrandORM.id == ProductORM.brand_id)
        .join(SubCategoryORM, SubCategoryORM.id == ProductORM.subcategory_id)
        .join(CategoryORM, CategoryORM.id == SubCategoryORM.category_id)
        .join(BranchORM, BranchORM.id == ProductORM.branch_id)
        .join(CompanyORM, CompanyORM.id == BranchORM.company_id)
        .outerjoin(image_per_product_subq, image_per_product_subq.c.id_producto == ProductORM.id)
        .outerjoin(ImageORM, ImageORM.id == image_per_product_subq.c.min_image_id)
        .filter(
            CompanyORM.name.ilike(f"%{company_name}%"),
            ProductORM.active == 1,
            CompanyORM.active == True
        )
    )
    
    # Aplicar filtro de categoría si se proporciona
    if category_id:
        query = query.filter(CategoryORM.id == category_id)
    
    # Ordenar por fecha de creación (más recientes primero)
    query = query.order_by(ProductORM.created_at.desc())
    
    # Ejecutar consulta
    rows = query.all()
    
    # Procesar resultados
    products: List[ProductORM] = []
    for product_orm, brand_name, subcategory_name, category_name, cat_id, company_name, branch_name, image_url in rows:
        # Asignar valores adicionales al objeto ProductORM
        product_orm.brand_name = brand_name
        product_orm.subcategory_name = subcategory_name
        product_orm.category_name = category_name
        product_orm.category_key = slugify(category_name) if category_name else None
        product_orm.category_id = cat_id
        product_orm.company_name = company_name
        product_orm.branch_name = branch_name
        product_orm.image_url = image_url
        products.append(product_orm)
    
    return products
