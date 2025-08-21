from typing import List
from sqlalchemy.orm import Session
from sqlalchemy.orm import joinedload


from app.domain.models.product import Product
from app.domain.models.image import Image
from app.infrastructure.db.models.product_model import ProductORM
from app.infrastructure.db.models.image import ImageORM


def get_top3_recent_products_use_case(db: Session) -> List[Product]:

    # Subconsulta para obtener una imagen por producto
    productos_orm = (
        db.query(ProductORM, ImageORM)
        .join(ImageORM, ImageORM.id_producto == ProductORM.id)
        .distinct(ProductORM.id)  # Para evitar duplicados de productos
        .all()
    )

    productos: List[Product] = []
    for p in productos_orm:

        # Objeto de la imagen
        i = p[1]

        # Objeto de producto
        p = p[0]

        productos.append(
            Product(
                id=p.id,
                name=p.nombre,
                brand=p.id_marca,
                price=p.precio_bs,
                category=p.sub_categoria.nombre,
                stock=p.in_stock,
                offerDescription="",
                supplier=p.id_sucursal,
                availableOnline=p.activo,
                views=p.views if p.views else 0,
                creado=p.creado,
                precio_dls=p.precio_dls if p.precio_dls else None,
                activo=p.activo,
                image=i.url if i else None,
            )
        )
    return productos
