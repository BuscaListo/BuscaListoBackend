from datetime import datetime
from sqlalchemy.orm import Session
from app.infrastructure.db.models import ProductORM
from app.application.dto.product_dto import ProductCreateDTO


def create_product_use_case(db: Session, product_data: ProductCreateDTO) -> ProductORM:
    nuevo_producto = ProductORM(
        name=product_data.name,
        description=product_data.description,
        price_bs=product_data.price_bs,
        price_usd=product_data.price_usd,
        images=product_data.images,
        code=product_data.code,
        in_stock=product_data.in_stock if product_data.in_stock is not None else 1,
        subcategory_id=product_data.subcategory_id,
        branch_id=product_data.branch_id,
        brand_id=product_data.brand_id,
        created_at=datetime.utcnow(),
        created_by=product_data.created_by,
        features=product_data.features,
        advanced_features=product_data.advanced_features,
        active=1
    )

    db.add(nuevo_producto)
    db.commit()
    db.refresh(nuevo_producto)

    return nuevo_producto

