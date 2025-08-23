from typing import List
from sqlalchemy.orm import Session
from sqlalchemy import func

from app.domain.models.product import Product
from app.infrastructure.db.models.product_model import ProductORM
from app.infrastructure.db.models.image import ImageORM
from app.infrastructure.db.models.marcas_model import MarcaORM
from app.infrastructure.db.models.subcategorias_model import SubCategoriaORM


def get_most_viewed_products_use_case(db: Session) -> List[Product]:
    # Subconsulta para elegir una única imagen por producto (la de menor id)
    image_per_product_subq = (
        db.query(
            ImageORM.id_producto.label("id_producto"),
            func.min(ImageORM.id).label("min_image_id"),
        )
        .group_by(ImageORM.id_producto)
        .subquery()
    )

    # Consulta optimizada con joins necesarios y límite de 3 productos más recientes
    rows = (
        db.query(
            ProductORM,
            MarcaORM.nombre.label("brand_name"),
            SubCategoriaORM.nombre.label("subcategory_name"),
            ImageORM.url.label("image_url"),
        )
        .join(MarcaORM, MarcaORM.id == ProductORM.id_marca)
        .join(SubCategoriaORM, SubCategoriaORM.id == ProductORM.id_sub_categoria)
        .outerjoin(image_per_product_subq, image_per_product_subq.c.id_producto == ProductORM.id)
        .outerjoin(ImageORM, ImageORM.id == image_per_product_subq.c.min_image_id)
        .order_by(ProductORM.views.desc())
        .limit(5)
        .all()
    )

    productos: List[Product] = []
    for producto_orm, brand_name, subcategory_name, image_url in rows:
        productos.append(
            Product(
                id=producto_orm.id,
                name=producto_orm.nombre,
                brand=brand_name,  # ahora nombre de marca
                price=producto_orm.precio_bs,
                category=subcategory_name,
                stock=producto_orm.in_stock,
                offerDescription="",
                supplier=producto_orm.id_sucursal,
                availableOnline=producto_orm.activo,
                views=producto_orm.views if producto_orm.views else 0,
                creado=producto_orm.creado,
                precio_dls=producto_orm.precio_dls if producto_orm.precio_dls else None,
                activo=producto_orm.activo,
                imageUrl=image_url,
            )
        )
    return productos
