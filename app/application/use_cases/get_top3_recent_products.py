from typing import List
from sqlalchemy.orm import Session
from app.domain.models.product import Product
from app.infrastructure.db.models.product_model import ProductORM


def get_top3_recent_products_use_case(db: Session) -> List[Product]:
    productos_orm = (
        db.query(ProductORM)
        .order_by(ProductORM.creado.desc())
        .limit(3)
        .all()
    )

    productos: List[Product] = []
    for p in productos_orm:
        productos.append(
            Product(
                id=p.id,
                name=p.nombre,
                brand=p.id_marca,
                price=p.precio_bs,
                category=p.sub_categoria.nombre,
                imageUrl=p.imagenes,
                stock=p.in_stock,
                offerDescription="",
                supplier=p.id_sucursal,
                availableOnline=p.activo,
                views=p.views if p.views else 0,
                creado=p.creado,
                precio_dls=p.precio_dls if p.precio_dls else None,
                activo=p.activo,
            )
        )
    return productos

