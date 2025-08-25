from sqlalchemy.orm import Session
from app.infrastructure.db.models import ProductORM


def delete_product_use_case(db: Session, product_id: int) -> bool:
    producto_orm = db.query(ProductORM).filter(ProductORM.id == product_id).first()
    if not producto_orm:
        return False
    db.delete(producto_orm)
    db.commit()
    return True

