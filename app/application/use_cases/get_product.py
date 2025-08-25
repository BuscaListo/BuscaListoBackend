from sqlalchemy.orm import Session
from app.infrastructure.db.models import ProductORM

def get_product_use_case(db: Session, product_id: int) -> ProductORM:
    producto_orm = db.query(ProductORM).filter(ProductORM.id == product_id).first()
    if not producto_orm:
        return None
    
    return producto_orm
