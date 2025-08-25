from sqlalchemy.orm import Session
from app.infrastructure.db.models import ProductORM
from app.application.dto.product_dto import ProductUpdateDTO


def update_product_use_case(db: Session, product_id: int, updates: ProductUpdateDTO) -> ProductORM | None:
    producto_orm: ProductORM | None = db.query(ProductORM).filter(ProductORM.id == product_id).first()
    if not producto_orm:
        return None

    update_data = updates.model_dump(exclude_unset=True)
    for field_name, field_value in update_data.items():
        setattr(producto_orm, field_name, field_value)

    db.commit()
    db.refresh(producto_orm)

    return producto_orm

