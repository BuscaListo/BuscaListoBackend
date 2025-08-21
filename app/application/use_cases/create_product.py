from datetime import datetime
from sqlalchemy.orm import Session
from app.domain.models.product import Product
from app.infrastructure.db.models.product_model import ProductORM
from app.application.dto.producto_dto import ProductCreateDTO


def create_product_use_case(db: Session, product_data: ProductCreateDTO) -> Product:
    nuevo_producto = ProductORM(
        nombre=product_data.nombre,
        descripcion=product_data.descripcion,
        precio_bs=product_data.precio_bs,
        precio_dls=product_data.precio_dls,
        imagenes=product_data.imagenes,
        codigo=product_data.codigo,
        in_stock=product_data.in_stock if product_data.in_stock is not None else True,
        id_sub_categoria=product_data.id_sub_categoria,
        id_sucursal=product_data.id_sucursal,
        id_marca=product_data.id_marca,
        creado=product_data.creado or datetime.utcnow(),
        creado_por=None,
        activo=product_data.activo if product_data.activo is not None else True,
        caracteristicas=product_data.caracteristicas,
        caracteristicas_avanzada=product_data.caracteristicas_avanzada,
    )

    db.add(nuevo_producto)
    db.commit()
    db.refresh(nuevo_producto)

    return Product(
        id=nuevo_producto.id,
        name=nuevo_producto.nombre,
        brand=nuevo_producto.id_marca,
        price=nuevo_producto.precio_bs,
        category=nuevo_producto.sub_categoria.nombre,
        imageUrl=nuevo_producto.imagenes,
        stock=nuevo_producto.in_stock,
        offerDescription="",
        supplier=nuevo_producto.id_sucursal,
        availableOnline=nuevo_producto.activo,
        views=nuevo_producto.views if nuevo_producto.views else 0,
        creado=nuevo_producto.creado,
        precio_dls=nuevo_producto.precio_dls if nuevo_producto.precio_dls else None,
        activo=nuevo_producto.activo,
    )

