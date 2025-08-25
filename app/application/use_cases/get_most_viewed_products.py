from typing import List
from sqlalchemy.orm import Session
from sqlalchemy import func

from app.infrastructure.db.models import ProductORM, ImageORM, BrandORM, SubCategoryORM


def get_most_viewed_products_use_case(db: Session) -> List[ProductORM]:
    # Subconsulta para elegir una única imagen por producto (la de menor id)
    image_per_product_subq = (
        db.query(
            ImageORM.product_id.label("id_producto"),
            func.min(ImageORM.id).label("min_image_id"),
        )
        .group_by(ImageORM.product_id)
        .subquery()
    )

    # Consulta optimizada con joins necesarios y límite de 3 productos más recientes
    rows = (
        db.query(
            ProductORM,
            BrandORM.name.label("brand_name"),
            SubCategoryORM.name.label("subcategory_name"),
            ImageORM.url.label("image_url"),
        )
        .join(BrandORM, BrandORM.id == ProductORM.brand_id)
        .join(SubCategoryORM, SubCategoryORM.id == ProductORM.subcategory_id)
        .outerjoin(image_per_product_subq, image_per_product_subq.c.id_producto == ProductORM.id)
        .outerjoin(ImageORM, ImageORM.id == image_per_product_subq.c.min_image_id)
        .order_by(ProductORM.views.desc())
        .limit(5)
        .all()
    )

    productos: List[ProductORM] = []
    for producto_orm, brand_name, subcategory_name, image_url in rows:
        # Asignar valores adicionales al objeto ProductORM
        producto_orm.brand_name = brand_name
        producto_orm.subcategory_name = subcategory_name
        producto_orm.image_url = image_url
        productos.append(producto_orm)
    
    return productos
