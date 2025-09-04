"""
Router de productos refactorizado para usar alias en inglés.
Este es el router original pero usando los nuevos alias y mapeadores.
"""

from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from typing import List, Optional
from app.application.dto.product_dto import (
    ProductResponseDTO,
    RecentProductResponseDTO,
    ProductCreateDTO,
    ProductUpdateDTO,
    ProductDetailDTO,
    SearchResponseDTO,
    SearchSuggestionsDTO,
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
from app.application.use_cases.get_products_by_company import (
    get_products_by_company_use_case,
)
from app.application.use_cases.search_products import (
    search_products_use_case,
    get_search_suggestions_use_case,
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


@router.get("/search", response_model=SearchResponseDTO)
def search_products(
    q: str = Query(..., min_length=2, description="Término de búsqueda (mínimo 2 caracteres)"),
    categoria: Optional[str] = Query(None, description="Categoría para filtrar (opcional)"),
    page: int = Query(1, ge=1, description="Número de página"),
    limit: int = Query(20, ge=1, le=100, description="Número de resultados por página"),
    sort_by: str = Query("relevance", description="Campo para ordenar: relevance, price, views, created_at"),
    sort_order: str = Query("desc", description="Orden: asc o desc"),
    db: Session = Depends(get_db)
):
    """
    Buscar productos por término de búsqueda con filtros y paginación.
    
    Este endpoint permite buscar productos usando múltiples criterios:
    - Nombre del producto
    - Marca
    - Descripción
    - Nombre de la empresa
    - Categoría/Subcategoría
    
    Args:
        q: Término de búsqueda (mínimo 2 caracteres)
        categoria: Categoría para filtrar (opcional)
        page: Número de página (empezando en 1)
        limit: Número de resultados por página (1-100)
        sort_by: Campo para ordenar (relevance, price, views, created_at)
        sort_order: Orden (asc o desc)
    
    Returns:
        Respuesta con productos encontrados, metadatos de paginación y filtros aplicados
    """
    
    # Validar parámetros de ordenamiento
    valid_sort_fields = ["relevance", "price", "views", "created_at"]
    if sort_by not in valid_sort_fields:
        raise HTTPException(
            status_code=400, 
            detail=f"sort_by debe ser uno de: {', '.join(valid_sort_fields)}"
        )
    
    valid_sort_orders = ["asc", "desc"]
    if sort_order not in valid_sort_orders:
        raise HTTPException(
            status_code=400, 
            detail=f"sort_order debe ser uno de: {', '.join(valid_sort_orders)}"
        )
    
    # Calcular offset para paginación
    offset = (page - 1) * limit
    
    # Ejecutar búsqueda
    products, total_count = search_products_use_case(
        db=db,
        search_term=q,
        category=categoria,
        limit=limit,
        offset=offset,
        sort_by=sort_by,
        sort_order=sort_order
    )
    
    # Calcular total de páginas
    total_pages = (total_count + limit - 1) // limit
    # Convertir productos a DTOs
    product_dtos = []
    for product_result in products:
        # Obtener información relacionada desde el resultado de búsqueda
        product = product_result.product
        brand_name = product_result.brand_name
        subcategory_name = product_result.subcategory_name
        category_name = product_result.category_name
        company_name = product_result.company_name
        
        # Construir URL de imagen (usar la primera imagen si existe)
        image_url = None
        if product.images:
            # Asumir que las imágenes están separadas por comas
            image_urls = product.images.split(',')
            if image_urls:
                image_url = image_urls[0].strip()
        
        product_dto = {
            "id": product.id,
            "name": product.name,
            "brand_name": brand_name,
            "price_bs": product.price_bs,
            "price_usd": product.price_usd,
            "image_url": image_url,
            "subcategory_name": subcategory_name,
            "category_name": category_name,
            "company_name": company_name,
            "views": product.views,
            "created_at": product.created_at,
            "in_stock": product.in_stock,
            "offer_description": None  # TODO: Implementar lógica de ofertas
        }
        product_dtos.append(product_dto)
    
    # Construir respuesta
    response = {
        "products": product_dtos,
        "total": total_count,
        "page": page,
        "limit": limit,
        "total_pages": total_pages,
        "search_term": q,
        "category": categoria,
        "sort_by": sort_by,
        "sort_order": sort_order
    }
    
    return response


@router.get("/search/suggestions", response_model=SearchSuggestionsDTO)
def get_search_suggestions(
    q: str = Query(..., min_length=2, description="Término de búsqueda para sugerencias"),
    limit: int = Query(10, ge=1, le=20, description="Número máximo de sugerencias"),
    db: Session = Depends(get_db)
):
    """
    Obtener sugerencias de búsqueda basadas en productos existentes.
    
    Este endpoint proporciona sugerencias de autocompletado para mejorar
    la experiencia de búsqueda del usuario.
    
    Args:
        q: Término de búsqueda parcial (mínimo 2 caracteres)
        limit: Número máximo de sugerencias (1-20)
    
    Returns:
        Lista de sugerencias basadas en nombres de productos, marcas y categorías
    """
    
    suggestions = get_search_suggestions_use_case(
        db=db,
        search_term=q,
        limit=limit
    )
    
    return {
        "suggestions": suggestions,
        "search_term": q
    }


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


@router.get("/company/{company_name}", response_model=List[ProductResponseDTO])
def get_products_by_company(
    company_name: str,
    category_id: Optional[int] = Query(None, description="ID de la categoría para filtrar"),
    db: Session = Depends(get_db)
):
    """
    Obtiene todos los productos de una empresa específica.
    
    Args:
        company_name: Nombre de la empresa
        category_id: ID de la categoría para filtrar (opcional)
    
    Returns:
        Lista de productos de la empresa
    """
    products = get_products_by_company_use_case(db, company_name, category_id)
    
    if not products:
        raise HTTPException(
            status_code=404, 
            detail=f"No se encontraron productos para la empresa '{company_name}'"
        )
    
    return [ProductResponseDTO.model_validate(p) for p in products]
