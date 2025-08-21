from sqlalchemy.orm import Session
from app.domain.models.product import Product
from app.infrastructure.db.models.product_model import ProductORM
from app.application.dto.producto_dto import ProductUpdateDTO


def update_product_use_case(db: Session, product_id: int, updates: ProductUpdateDTO) -> Product | None:
    producto_orm: ProductORM | None = db.query(ProductORM).filter(ProductORM.id == product_id).first()
    if not producto_orm:
        return None

    update_data = updates.model_dump(exclude_unset=True)
    for field_name, field_value in update_data.items():
        setattr(producto_orm, field_name, field_value)

    db.commit()
    db.refresh(producto_orm)

    return Product(
        id=producto_orm.id,
        name=producto_orm.nombre,
        brand=producto_orm.id_marca,
        price=producto_orm.precio_bs,
        category=producto_orm.sub_categoria.nombre,
        imageUrl=producto_orm.imagenes,
        stock=producto_orm.in_stock,
        offerDescription="",
        supplier=producto_orm.id_sucursal,
        availableOnline=producto_orm.activo,
        views=producto_orm.views if producto_orm.views else 0,
        creado=producto_orm.creado,
        precio_dls=producto_orm.precio_dls if producto_orm.precio_dls else None,
        activo=producto_orm.activo,
    )

