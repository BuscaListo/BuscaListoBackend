from typing import List
from sqlalchemy.orm import Session
from app.infrastructure.db.models import CategoryORM, ImageCategoryORM
import re
import unicodedata

def slugify(text: str) -> str:
    text = unicodedata.normalize("NFKD", text).encode("ascii", "ignore").decode("utf-8")
    text = text.lower()
    text = re.sub(r'[^a-z0-9\s]', '', text)
    return text.replace(" ", "")


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
        image_urls = [
            image.url for image in images_orm if image.category_id == category.id
        ]

        categories_response.append({
            "id": category.id,
            "name": category.name,
            "description": category.description,
            "image_urls": image_urls,
            "key": slugify(category.name),
        })
    return categories_response
