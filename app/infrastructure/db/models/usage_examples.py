"""
Ejemplos de uso de los alias en inglés para consultas directas.
Este archivo muestra cómo usar los nuevos alias en lugar de los nombres originales en español.
"""

from sqlalchemy.orm import Session
# Importar directamente desde los archivos de modelo para evitar importación circular
from .product import ProductORM as Product
from .category import CategoryORM as Category
from .subcategory import SubCategoryORM as SubCategory
from .brand import BrandORM as Brand
from .branch import BranchORM as Branch
from .company import CompanyORM as Company
from .location import LocationORM as Location
from .user import UserORM as User
from .stock import StockORM as Stock
from .offer import OfferORM as Offer
from .advertisement import AdvertisementORM as Advertisement
from .subscription import SubscriptionORM as Subscription
from .user_subscription import UserSubscriptionORM as UserSubscription
from .user_permission import UserPermissionORM as UserPermission
from .permission_catalog import PermissionCatalogORM as PermissionCatalog
from .web_service import WebServiceORM as WebService
from .web_service_log import WebServiceLogORM as WebServiceLog
from .price_history import PriceHistoryORM as PriceHistory
from .ad_statistics import AdStatisticsORM as AdStatistics
from .image import ImageORM as Image
from .currency import CurrencyORM as Currency


def example_product_queries(db: Session):
    """
    Ejemplos de consultas de productos usando alias en inglés.
    """
    
    # 1. Obtener todos los productos activos
    active_products = db.query(Product).filter(Product.active == True).all()
    
    # 2. Obtener productos por precio
    expensive_products = db.query(Product).filter(Product.price_bs > 1000).all()
    
    # 3. Obtener productos con stock disponible
    available_products = db.query(Product).filter(Product.in_stock > 0).all()
    
    # 4. Obtener productos más vistos
    popular_products = db.query(Product).order_by(Product.views.desc()).limit(10).all()
    
    # 5. Obtener productos por código
    product_by_code = db.query(Product).filter(Product.code == "ABC123").first()
    
    return {
        "active_products": active_products,
        "expensive_products": expensive_products,
        "available_products": available_products,
        "popular_products": popular_products,
        "product_by_code": product_by_code
    }


def example_category_queries(db: Session):
    """
    Ejemplos de consultas de categorías usando alias en inglés.
    """
    
    # 1. Obtener todas las categorías activas
    active_categories = db.query(Category).filter(Category.active == True).all()
    
    # 2. Obtener categoría por nombre
    category_by_name = db.query(Category).filter(Category.name == "Electrónicos").first()
    
    # 3. Obtener categorías con imágenes
    categories_with_images = db.query(Category).filter(Category.images.isnot(None)).all()
    
    return {
        "active_categories": active_categories,
        "category_by_name": category_by_name,
        "categories_with_images": categories_with_images
    }


def example_subcategory_queries(db: Session):
    """
    Ejemplos de consultas de subcategorías usando alias en inglés.
    """
    
    # 1. Obtener subcategorías por categoría
    subcategories_by_category = db.query(SubCategory)\
        .filter(SubCategory.category_id == 1)\
        .filter(SubCategory.active == True)\
        .all()
    
    # 2. Obtener subcategoría por nombre
    subcategory_by_name = db.query(SubCategory)\
        .filter(SubCategory.name == "Smartphones")\
        .first()
    
    return {
        "subcategories_by_category": subcategories_by_category,
        "subcategory_by_name": subcategory_by_name
    }


def example_brand_queries(db: Session):
    """
    Ejemplos de consultas de marcas usando alias en inglés.
    """
    
    # 1. Obtener todas las marcas activas
    active_brands = db.query(Brand).filter(Brand.active == True).all()
    
    # 2. Obtener marca por nombre
    brand_by_name = db.query(Brand).filter(Brand.name == "Samsung").first()
    
    # 3. Obtener marcas con logo
    brands_with_logo = db.query(Brand).filter(Brand.logo.isnot(None)).all()
    
    return {
        "active_brands": active_brands,
        "brand_by_name": brand_by_name,
        "brands_with_logo": brands_with_logo
    }


def example_branch_queries(db: Session):
    """
    Ejemplos de consultas de sucursales usando alias en inglés.
    """
    
    # 1. Obtener todas las sucursales activas
    active_branches = db.query(Branch).filter(Branch.active == True).all()
    
    # 2. Obtener sucursales por empresa
    branches_by_company = db.query(Branch)\
        .filter(Branch.company_id == 1)\
        .all()
    
    # 3. Obtener sucursales por ubicación
    branches_by_location = db.query(Branch)\
        .filter(Branch.location_id == 1)\
        .all()
    
    return {
        "active_branches": active_branches,
        "branches_by_company": branches_by_company,
        "branches_by_location": branches_by_location
    }


def example_join_queries(db: Session):
    """
    Ejemplos de consultas con joins usando alias en inglés.
    """
    
    # 1. Obtener productos con información de categoría y subcategoría
    products_with_categories = db.query(
        Product.id,
        Product.name,
        Product.price_bs,
        SubCategory.name.label('subcategory_name'),
        Category.name.label('category_name')
    ).join(SubCategory).join(Category).filter(Product.active == True).all()
    
    # 2. Obtener productos con información de marca y sucursal
    products_with_brand_branch = db.query(
        Product.id,
        Product.name,
        Product.price_bs,
        Brand.name.label('brand_name'),
        Branch.name.label('branch_name')
    ).join(Brand).join(Branch).filter(Product.active == True).all()
    
    # 3. Obtener sucursales con información de empresa y ubicación
    branches_with_company_location = db.query(
        Branch.id,
        Branch.name,
        Company.name.label('company_name'),
        Location.name.label('location_name')
    ).join(Company).join(Location).filter(Branch.active == True).all()
    
    return {
        "products_with_categories": products_with_categories,
        "products_with_brand_branch": products_with_brand_branch,
        "branches_with_company_location": branches_with_company_location
    }


def example_complex_queries(db: Session):
    """
    Ejemplos de consultas complejas usando alias en inglés.
    """
    
    # 1. Obtener productos más caros por categoría
    from sqlalchemy import func
    
    expensive_by_category = db.query(
        Category.name.label('category_name'),
        func.max(Product.price_bs).label('max_price'),
        func.count(Product.id).label('product_count')
    ).join(SubCategory).join(Product)\
     .filter(Product.active == True)\
     .group_by(Category.id, Category.name)\
     .all()
    
    # 2. Obtener marcas con más productos
    brands_with_product_count = db.query(
        Brand.name.label('brand_name'),
        func.count(Product.id).label('product_count'),
        func.avg(Product.price_bs).label('avg_price')
    ).join(Product)\
     .filter(Product.active == True)\
     .group_by(Brand.id, Brand.name)\
     .order_by(func.count(Product.id).desc())\
     .all()
    
    # 3. Obtener sucursales con más productos
    branches_with_product_count = db.query(
        Branch.name.label('branch_name'),
        func.count(Product.id).label('product_count'),
        func.sum(Product.views).label('total_views')
    ).join(Product)\
     .filter(Product.active == True)\
     .group_by(Branch.id, Branch.name)\
     .order_by(func.count(Product.id).desc())\
     .all()
    
    return {
        "expensive_by_category": expensive_by_category,
        "brands_with_product_count": brands_with_product_count,
        "branches_with_product_count": branches_with_product_count
    }


def example_filter_queries(db: Session):
    """
    Ejemplos de consultas con filtros usando alias en inglés.
    """
    
    # 1. Obtener productos con filtros múltiples
    filtered_products = db.query(Product)\
        .filter(Product.active == True)\
        .filter(Product.price_bs.between(100, 1000))\
        .filter(Product.in_stock > 0)\
        .filter(Product.views > 10)\
        .order_by(Product.price_bs.asc())\
        .all()
    
    # 2. Obtener productos por rango de precios y categoría
    products_by_price_category = db.query(Product)\
        .join(SubCategory)\
        .filter(Product.price_bs >= 500)\
        .filter(SubCategory.category_id == 1)\
        .filter(Product.active == True)\
        .all()
    
    # 3. Obtener productos con búsqueda por nombre
    from sqlalchemy import or_
    
    search_products = db.query(Product)\
        .filter(Product.active == True)\
        .filter(or_(
            Product.name.ilike('%phone%'),
            Product.name.ilike('%smartphone%'),
            Product.description.ilike('%phone%')
        ))\
        .all()
    
    return {
        "filtered_products": filtered_products,
        "products_by_price_category": products_by_price_category,
        "search_products": search_products
    }


# Función principal para ejecutar todos los ejemplos
def run_all_examples(db: Session):
    """
    Ejecuta todos los ejemplos de consultas.
    
    Args:
        db: Sesión de base de datos
        
    Returns:
        Diccionario con todos los resultados
    """
    return {
        "product_queries": example_product_queries(db),
        "category_queries": example_category_queries(db),
        "subcategory_queries": example_subcategory_queries(db),
        "brand_queries": example_brand_queries(db),
        "branch_queries": example_branch_queries(db),
        "join_queries": example_join_queries(db),
        "complex_queries": example_complex_queries(db),
        "filter_queries": example_filter_queries(db)
    }
