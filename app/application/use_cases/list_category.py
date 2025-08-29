from typing import List
from sqlalchemy.orm import Session
from app.infrastructure.db.models import CategoryORM, ImageCategoryORM

def list_categories_use_case(db: Session) -> List[CategoryORM]:
    # Get all categories
    categorias_orm = db.query(CategoryORM).all()
    ids_categories = [c.id for c in categorias_orm]
    # Get images for categories
    images_orm = (
        db.query(ImageCategoryORM)
        .filter(ImageCategoryORM.category_id.in_(ids_categories))
        .all()
    )
    # Get all
    categories_response: List[CategoryORM] = []
    for category in categorias_orm:
        category.image_urls = [
            image.url for image in images_orm if image.category_id == category.id
        ]
        categories_response.append(category)
    return categories_response
