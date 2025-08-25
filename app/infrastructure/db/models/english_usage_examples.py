"""
Ejemplos de uso de los nuevos campos en inglés en los modelos.
Ahora puedes usar nombres en inglés directamente en el código.
"""

from sqlalchemy.orm import Session
from . import (
    Product, Category, SubCategory, Brand, Branch, Company, Location,
    User, Stock, Offer, Advertisement, Subscription, UserSubscription,
    UserPermission, PermissionCatalog, WebService, WebServiceLog, 
    PriceHistory, AdStatistics, Image, Currency
)


def example_english_field_usage(db: Session):
    """
    Ejemplos de uso de campos en inglés directamente.
    """
    
    # 1. Crear un producto usando campos en inglés
    new_product = Product(
        name="iPhone 15 Pro",
        description="El último iPhone con características avanzadas",
        price_bs=15000.0,
        price_usd=2000.0,
        code="IPH15PRO",
        in_stock=10,
        subcategory_id=1,
        branch_id=1,
        brand_id=1,
        features="Cámara profesional, chip A17 Pro",
        active=1
    )
    
    # 2. Crear una categoría usando campos en inglés
    new_category = Category(
        name="Electrónicos",
        images="electronics.jpg",
        active=True
    )
    
    # 3. Crear una subcategoría usando campos en inglés
    new_subcategory = SubCategory(
        name="Smartphones",
        images="smartphones.jpg",
        category_id=1,
        active=True
    )
    
    # 4. Crear una marca usando campos en inglés
    new_brand = Brand(
        name="Apple",
        description="Empresa líder en tecnología",
        images="apple.jpg",
        logo="apple_logo.png",
        active=True
    )
    
    # 5. Crear una sucursal usando campos en inglés
    new_branch = Branch(
        name="Centro Comercial Galerías",
        images="galerias.jpg",
        company_id=1,
        location_id=1,
        user_id=1,
        active=True
    )
    
    return {
        "new_product": new_product,
        "new_category": new_category,
        "new_subcategory": new_subcategory,
        "new_brand": new_brand,
        "new_branch": new_branch
    }


def example_english_queries(db: Session):
    """
    Ejemplos de consultas usando campos en inglés.
    """
    
    # 1. Buscar productos por nombre
    products_by_name = db.query(Product).filter(Product.name.ilike('%iPhone%')).all()
    
    # 2. Buscar productos activos por precio
    expensive_products = db.query(Product)\
        .filter(Product.active == 1)\
        .filter(Product.price_bs > 10000)\
        .all()
    
    # 3. Buscar categorías activas
    active_categories = db.query(Category).filter(Category.active == True).all()
    
    # 4. Buscar marcas con logo
    brands_with_logo = db.query(Brand)\
        .filter(Brand.logo.isnot(None))\
        .filter(Brand.active == True)\
        .all()
    
    # 5. Buscar sucursales por empresa
    branches_by_company = db.query(Branch)\
        .filter(Branch.company_id == 1)\
        .filter(Branch.active == True)\
        .all()
    
    return {
        "products_by_name": products_by_name,
        "expensive_products": expensive_products,
        "active_categories": active_categories,
        "brands_with_logo": brands_with_logo,
        "branches_by_company": branches_by_company
    }


def example_english_joins(db: Session):
    """
    Ejemplos de joins usando campos en inglés.
    """
    
    # 1. Productos con información de categoría y subcategoría
    products_with_categories = db.query(
        Product.id,
        Product.name,
        Product.price_bs,
        Product.price_usd,
        SubCategory.name.label('subcategory_name'),
        Category.name.label('category_name')
    ).join(SubCategory).join(Category)\
     .filter(Product.active == 1)\
     .all()
    
    # 2. Productos con información de marca y sucursal
    products_with_brand_branch = db.query(
        Product.id,
        Product.name,
        Product.price_bs,
        Brand.name.label('brand_name'),
        Branch.name.label('branch_name')
    ).join(Brand).join(Branch)\
     .filter(Product.active == 1)\
     .all()
    
    # 3. Sucursales con información de empresa y ubicación
    branches_with_company_location = db.query(
        Branch.id,
        Branch.name,
        Company.name.label('company_name'),
        Location.name.label('location_name')
    ).join(Company).join(Location)\
     .filter(Branch.active == True)\
     .all()
    
    return {
        "products_with_categories": products_with_categories,
        "products_with_brand_branch": products_with_brand_branch,
        "branches_with_company_location": branches_with_company_location
    }


def example_english_updates(db: Session):
    """
    Ejemplos de actualizaciones usando campos en inglés.
    """
    
    # 1. Actualizar el precio de un producto
    product_to_update = db.query(Product).filter(Product.id == 1).first()
    if product_to_update:
        product_to_update.price_bs = 16000.0
        product_to_update.price_usd = 2100.0
    
    # 2. Actualizar el stock de un producto
    product_stock = db.query(Product).filter(Product.id == 1).first()
    if product_stock:
        product_stock.in_stock = 15
    
    # 3. Actualizar el estado de una categoría
    category_to_update = db.query(Category).filter(Category.id == 1).first()
    if category_to_update:
        category_to_update.active = False
    
    # 4. Actualizar las vistas de un producto
    product_views = db.query(Product).filter(Product.id == 1).first()
    if product_views:
        product_views.views += 1
    
    return {
        "product_updated": product_to_update is not None,
        "stock_updated": product_stock is not None,
        "category_updated": category_to_update is not None,
        "views_updated": product_views is not None
    }


def example_english_inserts(db: Session):
    """
    Ejemplos de inserciones usando campos en inglés.
    """
    
    # 1. Insertar un nuevo usuario
    new_user = User(
        name="Juan Pérez",
        email="juan.perez@email.com",
        password="hashed_password_here",
        active=True
    )
    
    # 2. Insertar un nuevo stock
    new_stock = Stock(
        product_id=1,
        total_quantity=100,
        sold_quantity=0,
        offered_quantity=0,
        active=True
    )
    
    # 3. Insertar una nueva oferta
    new_offer = Offer(
        description="Descuento del 20% en smartphones",
        percentage=20.0,
        product_id=1,
        active=True
    )
    
    # 4. Insertar una nueva publicidad
    new_ad = Advertisement(
        branch_id=1,
        ad_images="ad_image.jpg",
        destination_link="https://example.com",
        priority=1,
        start_date="2024-01-01",
        end_date="2024-12-31",
        active=True
    )
    
    return {
        "new_user": new_user,
        "new_stock": new_stock,
        "new_offer": new_offer,
        "new_ad": new_ad
    }


# Función principal para ejecutar todos los ejemplos
def run_english_examples(db: Session):
    """
    Ejecuta todos los ejemplos de uso en inglés.
    
    Args:
        db: Sesión de base de datos
        
    Returns:
        Diccionario con todos los resultados
    """
    return {
        "field_usage": example_english_field_usage(db),
        "queries": example_english_queries(db),
        "joins": example_english_joins(db),
        "updates": example_english_updates(db),
        "inserts": example_english_inserts(db)
    }
