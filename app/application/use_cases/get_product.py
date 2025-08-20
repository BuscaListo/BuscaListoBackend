from sqlalchemy.orm import Session
from app.domain.models.product import Product
from app.infrastructure.db.models.product_model import ProductORM

def get_product_use_case(db: Session, product_id: int) -> Product:
    producto_orm = db.query(ProductORM).filter(ProductORM.id == product_id).first()
    if not producto_orm:
        return None
    
    return Product(
        id=producto_orm.id,
        name=producto_orm.nombre,
        brand=producto_orm.id_marca,
        price=producto_orm.precio_bs,
        subcategory=producto_orm.id_sub_categoria,
        imageUrl=producto_orm.imagenes,
        stock=producto_orm.in_stock,
        offerDescription="",
        requirePrescription=False,
        supplier="",
        availableOnline=producto_orm.activo,
        views=0,
        creado=producto_orm.creado
    )
