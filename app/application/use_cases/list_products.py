from typing import List
from sqlalchemy.orm import Session
from app.infrastructure.db.models import ProductORM


def list_products_use_case(db: Session) -> List[ProductORM]:
    productos_orm = db.query(ProductORM).all()
    return productos_orm

