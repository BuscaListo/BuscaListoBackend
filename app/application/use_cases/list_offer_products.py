from typing import List
from sqlalchemy import func
from sqlalchemy.orm import Session,aliased
from app.infrastructure.db.models import OfferORM, ProductORM
from app.application.dto.offer_product_dto import OfferProductResponseDTO
import pdb
def list_offer_products_use_case(db: Session) -> List[OfferORM]:
    # Get all offers more recent by product
    offers_cte = (
        db.query(
            OfferORM.product_id.label("id_producto"),
            OfferORM.id.label("offer_id"),
            OfferORM.discount_percent.label("discount_percent"),
            OfferORM.description.label("offer_description"),
            OfferORM.start_date,
            OfferORM.end_date,
            func.row_number()
            .over(
                partition_by=OfferORM.product_id,
                order_by=OfferORM.start_date.desc()
            )
            .label("rn"),
        )
        .filter(
            OfferORM.active == True,
            func.now() <= OfferORM.end_date,
            func.now() >= OfferORM.start_date,
        )
        .cte("offers_cte")
    )

    offers_alias = aliased(offers_cte)

    # Productos + última oferta
    products = (
        db.query(
            ProductORM,
            offers_alias.c.discount_percent,
            offers_alias.c.start_date,
            offers_alias.c.end_date,
            offers_alias.c.offer_id,
            offers_alias.c.offer_description
        )
        .join(offers_alias, offers_alias.c.id_producto == ProductORM.id)
        .filter(offers_alias.c.rn == 1)
        .all()
    )
    print("Total products with offers:", len(products))
    response = []
    for product, discount, start_date, end_date, offer_id, offer_description in products:
        print(f"Product ID: {product.id}, Discount: {discount}")
        calc = float(1 - discount / 100) if discount else 0.0
        usd_discount = float(product.price_usd * calc) if discount else None
        bs_discount  = float(product.price_bs * calc) if discount else None
        dto = OfferProductResponseDTO(
            id=product.id,
            name=product.name,
            brand_id=product.brand_id,
            price_bs=product.price_bs,
            subcategory_id=product.subcategory_id,
            price_usd=product.price_usd,
            in_stock=product.in_stock,
            branch_id=product.branch_id,
            active=product.active,
            views=product.views,
            created_at=product.created_at,
            image_url=product.images,
            offer_description=offer_description,
            offer_id=offer_id,
            id_product=product.id,
            discount_percent=discount,
            offer_start_date=start_date,
            offer_end_date=end_date,
            price_offer_usd=usd_discount,
            price_offer_bs=bs_discount,
        )
        response.append(dto)
    return response