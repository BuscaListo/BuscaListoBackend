from sqlalchemy.orm import Session, joinedload
from sqlalchemy import func
from app.infrastructure.db.models.product import ProductORM
from app.infrastructure.db.models.brand import BrandORM
from app.infrastructure.db.models.subcategory import SubCategoryORM
from app.infrastructure.db.models.category import CategoryORM
from app.infrastructure.db.models.branch import BranchORM
from app.infrastructure.db.models.company import CompanyORM
from app.infrastructure.db.models.location import LocationORM
from app.infrastructure.db.models.offer import OfferORM
from app.infrastructure.db.models.image import ImageORM
from app.application.dto.product_dto import ProductDetailDTO, ProductInfoDTO, PricingDTO, CompanyDTO, MetaDTO, MockCommentDTO
from typing import Optional


def get_product_detail_use_case(db: Session, product_id: int) -> Optional[ProductDetailDTO]:
    """
    Obtiene los detalles completos de un producto incluyendo todas las relaciones
    """
    result = db.query(
        ProductORM,
        BrandORM.name.label('brand_name'),
        SubCategoryORM.name.label('subcategory_name'),
        CategoryORM.name.label('category_name'),
        BranchORM.name.label('branch_name'),
        CompanyORM.name.label('company_name'),
        CompanyORM.phone.label('company_phone'),
        LocationORM.name.label('location_name'),
        OfferORM.description.label('offer_description'),
        OfferORM.discount_percent.label('discount_percent')
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
    ).join(
        LocationORM, BranchORM.location_id == LocationORM.id
    ).outerjoin(
        OfferORM, ProductORM.id == OfferORM.product_id
    ).filter(
        ProductORM.id == product_id,
        ProductORM.active == 1
    ).first()

    if not result:
        return None

    product, brand_name, subcategory_name, category_name, branch_name, company_name, company_phone, location_name, offer_description, discount_percent = result

    images = db.query(ImageORM.url).filter(
        ImageORM.product_id == product_id,
        ImageORM.active == True
    ).all()
    
    image_urls = [img.url for img in images] if images else []
    if not image_urls and product.images:
        image_urls = [img.strip() for img in product.images.split(',') if img.strip()]

    price_offer_usd = None
    price_offer_bs = None
    if discount_percent and float(discount_percent) > 0:
        discount_factor = 1 - float(discount_percent) / 100
        price_offer_usd = product.price_usd * discount_factor if product.price_usd else None
        price_offer_bs = product.price_bs * discount_factor

    product_url = f"https://buscalisto.com/product/{product_id}"
    mock_comments = []
    # Updtae views count
    product.views = (product.views or 0) + 1
    db.commit()

    product_info = ProductInfoDTO(
        id=product.id,
        name=product.name,
        brand_id=product.brand_id,
        price_bs=product.price_bs,
        price_usd=product.price_usd,
        subcategory_id=product.subcategory_id,
        in_stock=product.in_stock,
        branch_id=product.branch_id,
        active=bool(product.active),
        views=product.views or 0,
        created_at=product.created_at,
        code=product.code,
        brand_name=brand_name,
        subcategory_name=subcategory_name,
        category=category_name,
        imagenes=image_urls,
        characteristics=product.features,
        advancedCharacteristics=product.advanced_features,
        accessories=None,
        highlightedFeatures=None,
        pros=None,
        cons=None
    )

    pricing_info = PricingDTO(
        price_bs=product.price_bs,
        price_usd=product.price_usd,
        price_offer_usd=price_offer_usd,
        price_offer_bs=price_offer_bs,
        discount_percent=float(discount_percent) if discount_percent else None,
        offer_description=offer_description
    )

    company_info = CompanyDTO(
        supplier_id=product.branch_id,
        supplier_name=company_name,
        supplier_branch=branch_name,
        supplier_address=location_name,
        supplier_phone=company_phone,
        supplier_email=None,
        supplier_website=None,
        supplier_hours=None,
        supplier_rating=None,
        supplier_reviews=None
    )

    meta_info = MetaDTO(
        views=product.views,
        created_at=product.created_at,
        url=product_url,
        mockComments=mock_comments
    )

    product_detail = ProductDetailDTO(
        product=product_info,
        pricing=pricing_info,
        company=company_info,
        meta=meta_info
    )
    
    return product_detail
