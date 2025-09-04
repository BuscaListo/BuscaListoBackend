"""
Use case para búsqueda de productos con filtros y paginación.
"""

from sqlalchemy.orm import Session, joinedload
from sqlalchemy import and_, or_, func, desc, asc
from typing import List, Optional, Tuple, NamedTuple
from app.infrastructure.db.models.product import ProductORM
from app.infrastructure.db.models.brand import BrandORM
from app.infrastructure.db.models.subcategory import SubCategoryORM
from app.infrastructure.db.models.category import CategoryORM
from app.infrastructure.db.models.branch import BranchORM
from app.infrastructure.db.models.company import CompanyORM


class ProductSearchResult(NamedTuple):
    product: ProductORM
    brand_name: str
    subcategory_name: str
    category_name: str
    company_name: str
    branch_name: str


def search_products_use_case(
    db: Session,
    search_term: str,
    category: Optional[str] = None,
    limit: int = 20,
    offset: int = 0,
    sort_by: str = "relevance",
    sort_order: str = "desc"
) -> Tuple[List[ProductSearchResult], int]:
    """
    Buscar productos por término de búsqueda con filtros opcionales.
    
    Args:
        db: Sesión de base de datos
        search_term: Término de búsqueda
        category: Categoría para filtrar (opcional)
        limit: Número máximo de resultados
        offset: Desplazamiento para paginación
        sort_by: Campo para ordenar (relevance, price, views, created_at)
        sort_order: Orden (asc, desc)
    
    Returns:
        Tupla con (lista de productos, total de resultados)
    """
    
    # Validar entrada
    if not search_term or len(search_term.strip()) < 2:
        return [], 0
    
    search_term = search_term.strip()
    
    # Construir query base con joins para búsqueda - retornar todos los datos necesarios
    query = db.query(
        ProductORM,
        BrandORM.name.label('brand_name'),
        SubCategoryORM.name.label('subcategory_name'),
        CategoryORM.name.label('category_name'),
        CompanyORM.name.label('company_name'),
        BranchORM.name.label('branch_name')
    ).join(
        BrandORM, ProductORM.brand_id == BrandORM.id
    ).join(
        SubCategoryORM, ProductORM.subcategory_id == SubCategoryORM.id
    ).join(
        CategoryORM, SubCategoryORM.category_id == CategoryORM.id
    ).join(
        BranchORM, ProductORM.branch_id == BranchORM.id
    ).join(
        CompanyORM, BranchORM.company_id == CompanyORM.id
    )
    
    # Construir condiciones de búsqueda
    search_conditions = or_(
        # Búsqueda en nombre del producto (mayor relevancia)
        func.lower(ProductORM.name).contains(func.lower(search_term)),
        # Búsqueda en marca
        func.lower(BrandORM.name).contains(func.lower(search_term)),
        # Búsqueda en descripción
        func.lower(ProductORM.description).contains(func.lower(search_term)),
        # Búsqueda en nombre de la empresa
        func.lower(CompanyORM.name).contains(func.lower(search_term)),
        # Búsqueda en subcategoría
        func.lower(SubCategoryORM.name).contains(func.lower(search_term)),
        # Búsqueda en categoría
        func.lower(CategoryORM.name).contains(func.lower(search_term))
    )
    
    # Aplicar filtro de categoría si se especifica
    if category and category.lower() != "all":
        category_condition = or_(
            func.lower(CategoryORM.name) == func.lower(category),
            func.lower(SubCategoryORM.name) == func.lower(category)
        )
        query = query.filter(and_(search_conditions, category_condition))
    else:
        query = query.filter(search_conditions)
    
    # Filtrar solo productos activos
    query = query.filter(ProductORM.active == 1)
    
    # Contar total de resultados
    total_count = query.count()
    
    # Aplicar ordenamiento
    if sort_by == "relevance":
        # Ordenar por relevancia (coincidencias exactas primero)
        query = query.order_by(
            # Coincidencias exactas en nombre tienen mayor prioridad
            desc(func.lower(ProductORM.name).like(func.lower(f"{search_term}%"))),
            # Luego por coincidencias en nombre
            desc(func.lower(ProductORM.name).contains(func.lower(search_term))),
            # Luego por coincidencias en marca
            desc(func.lower(BrandORM.name).contains(func.lower(search_term))),
            # Finalmente por popularidad y fecha
            desc(ProductORM.views),
            desc(ProductORM.created_at)
        )
    elif sort_by == "price":
        if sort_order == "asc":
            query = query.order_by(asc(ProductORM.price_bs))
        else:
            query = query.order_by(desc(ProductORM.price_bs))
    elif sort_by == "views":
        if sort_order == "asc":
            query = query.order_by(asc(ProductORM.views))
        else:
            query = query.order_by(desc(ProductORM.views))
    elif sort_by == "created_at":
        if sort_order == "asc":
            query = query.order_by(asc(ProductORM.created_at))
        else:
            query = query.order_by(desc(ProductORM.created_at))
    else:
        # Ordenamiento por defecto
        query = query.order_by(desc(ProductORM.views), desc(ProductORM.created_at))
    
    # Aplicar paginación
    results = query.offset(offset).limit(limit).all()
    
    # Convertir resultados a ProductSearchResult
    products = []
    for result in results:
        product_result = ProductSearchResult(
            product=result[0],  # ProductORM
            brand_name=result[1] or "",  # brand_name
            subcategory_name=result[2] or "",  # subcategory_name
            category_name=result[3] or "",  # category_name
            company_name=result[4] or "",  # company_name
            branch_name=result[5] or ""  # branch_name
        )
        products.append(product_result)
    
    return products, total_count


def get_search_suggestions_use_case(
    db: Session,
    search_term: str,
    limit: int = 10
) -> List[str]:
    """
    Obtener sugerencias de búsqueda basadas en productos existentes.
    
    Args:
        db: Sesión de base de datos
        search_term: Término de búsqueda parcial
        limit: Número máximo de sugerencias
    
    Returns:
        Lista de sugerencias
    """
    
    if not search_term or len(search_term.strip()) < 2:
        return []
    
    search_term = search_term.strip()
    suggestions = set()
    
    # Buscar en nombres de productos
    product_names = db.query(ProductORM.name).filter(
        and_(
            ProductORM.active == 1,
            func.lower(ProductORM.name).like(func.lower(f"{search_term}%"))
        )
    ).limit(limit).all()
    
    for name, in product_names:
        suggestions.add(name)
    
    # Buscar en marcas
    brand_names = db.query(BrandORM.name).join(
        ProductORM, BrandORM.id == ProductORM.brand_id
    ).filter(
        and_(
            ProductORM.active == 1,
            func.lower(BrandORM.name).like(func.lower(f"{search_term}%"))
        )
    ).limit(limit).all()
    
    for name, in brand_names:
        suggestions.add(name)
    
    # Buscar en categorías
    category_names = db.query(CategoryORM.name).join(
        SubCategoryORM, CategoryORM.id == SubCategoryORM.category_id
    ).join(
        ProductORM, SubCategoryORM.id == ProductORM.subcategory_id
    ).filter(
        and_(
            ProductORM.active == 1,
            func.lower(CategoryORM.name).like(func.lower(f"{search_term}%"))
        )
    ).limit(limit).all()
    
    for name, in category_names:
        suggestions.add(name)
    
    # Convertir a lista y limitar
    suggestions_list = list(suggestions)[:limit]
    
    return suggestions_list
