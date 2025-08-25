# Guía de Refactor para Campos en Inglés

## Descripción

Este refactor permite mantener la compatibilidad con la base de datos en español mientras se programa completamente en inglés. Se han refactorizado todos los modelos para usar nombres de campos en inglés, pero mantienen la compatibilidad con la base de datos a través de mapeos de columnas.

## Estructura de Archivos

### 1. `app/infrastructure/db/models/__init__.py`
Contiene todos los alias de modelos en inglés:
- `Product` → `ProductORM`
- `Category` → `CategoriaORM`
- `SubCategory` → `SubCategoriaORM`
- `Brand` → `MarcaORM`
- `Branch` → `SucursalORM`
- `Company` → `EmpresaORM`
- `Location` → `UbicacionORM`
- `User` → `UsuarioORM`
- Y muchos más...

### 2. **Modelos Refactorizados** (Archivos individuales)
Todos los modelos ahora tienen campos en inglés que mapean a columnas en español y **nombres de archivo en inglés**:

**Archivos de Modelos:**
- `product.py` - Modelo de productos
- `category.py` - Modelo de categorías  
- `subcategory.py` - Modelo de subcategorías
- `brand.py` - Modelo de marcas
- `branch.py` - Modelo de sucursales
- `company.py` - Modelo de empresas
- `location.py` - Modelo de ubicaciones
- `user.py` - Modelo de usuarios
- `stock.py` - Modelo de stock
- `offer.py` - Modelo de ofertas
- `advertisement.py` - Modelo de publicidades
- `subscription.py` - Modelo de subscripciones
- `user_subscription.py` - Modelo de subscripciones de usuario
- `user_permission.py` - Modelo de permisos de usuario
- `permission_catalog.py` - Modelo de catálogo de permisos
- `web_service.py` - Modelo de web services
- `web_service_log.py` - Modelo de logs de web service
- `price_history.py` - Modelo de historial de precios
- `ad_statistics.py` - Modelo de estadísticas de publicidad
- `image.py` - Modelo de imágenes
- `currency.py` - Modelo de monedas

**Campos en Inglés:**
- `Product.name` → columna `"nombre"`
- `Product.description` → columna `"descripcion"`
- `Product.price_bs` → columna `"precio_bs"`
- `Product.subcategory_id` → columna `"id_sub_categoria"`
- Y muchos más...

### 3. `app/infrastructure/db/models/english_usage_examples.py`
Ejemplos de uso directo de campos en inglés.

## Cómo Usar

### Importar Modelos con Alias

```python
# Antes (usando nombres en español)
from app.infrastructure.db.models.product_model import ProductORM
from app.infrastructure.db.models.categorias_model import CategoriaORM

# Después (usando alias en inglés)
from app.infrastructure.db.models import Product, Category, SubCategory, Brand, Branch
```

### Consultas con Campos en Inglés

```python
# Antes
productos = db.query(ProductORM).filter(ProductORM.activo == True).all()

# Después - ¡Ahora puedes usar campos en inglés directamente!
productos = db.query(Product).filter(Product.active == True).all()

# O usando el alias directamente
from app.infrastructure.db.models import Product
productos = db.query(Product).filter(Product.active == True).all()
```

### Uso Directo de Campos en Inglés

```python
# Ahora puedes usar campos en inglés directamente en los modelos
new_product = Product(
    name="iPhone 15 Pro",
    description="El último iPhone con características avanzadas",
    price_bs=15000.0,
    price_usd=2000.0,
    code="IPH15PRO",
    in_stock=10,
    subcategory_id=1,
    branch_id=1,
    brand_id=1,
    features="Cámara profesional, chip A17 Pro",
    active=1
)

# Las consultas también son más claras
expensive_products = db.query(Product)\
    .filter(Product.active == 1)\
    .filter(Product.price_bs > 10000)\
    .all()
```

### Campos Refactorizados Disponibles

```python
# Producto
Product.name              # → columna "nombre"
Product.description       # → columna "descripcion"
Product.price_bs          # → columna "precio_bs"
Product.price_usd         # → columna "precio_dls"
Product.subcategory_id    # → columna "id_sub_categoria"
Product.branch_id         # → columna "id_sucursal"
Product.brand_id          # → columna "id_marca"
Product.features          # → columna "caracteristicas"
Product.active            # → columna "activo"

# Categoría
Category.name             # → columna "nombre"
Category.images           # → columna "imagenes"
Category.active           # → columna "activo"

# Marca
Brand.name                # → columna "nombre"
Brand.description         # → columna "descripcion"
Brand.logo                # → columna "logo"
Brand.active              # → columna "activo"

# Sucursal
Branch.name               # → columna "nombre"
Branch.company_id         # → columna "id_empresa"
Branch.location_id        # → columna "id_ubicacion"
Branch.active             # → columna "activo"
```

## Ejemplos de Uso en Routers

### Router Refactorizado

```python
from app.infrastructure.db.models import Product, Category

@router.post("/", response_model=ProductResponseDTO)
def create_product(payload: ProductCreateDTO, db: Session = Depends(get_db)):
    # ¡Ahora puedes usar campos en inglés directamente!
    new_product = Product(
        name=payload.name,
        description=payload.description,
        price_bs=payload.price_bs,
        subcategory_id=payload.subcategory_id,
        branch_id=payload.branch_id,
        brand_id=payload.brand_id,
        active=1
    )
    
    # O usar el use case existente
    producto = create_product_use_case(db, payload.model_dump())
    return ProductResponseDTO.model_validate(producto)
```

### Consultas con Joins

```python
from app.infrastructure.db.models import Product, SubCategory, Category

# Consulta usando campos en inglés
productos = db.query(Product)\
    .join(SubCategory)\
    .join(Category)\
    .filter(Category.name == "Electrónicos")\
    .filter(Product.active == True)\
    .all()

# También puedes usar campos en inglés en las consultas
expensive_products = db.query(Product)\
    .filter(Product.price_bs > 10000)\
    .filter(Product.active == 1)\
    .order_by(Product.price_bs.desc())\
    .all()
```

## Ventajas del Refactor

1. **Campos en Inglés**: Ahora puedes usar `Product.name` en lugar de `Product.nombre`
2. **Compatibilidad Total**: La base de datos mantiene sus nombres en español
3. **Mantenibilidad**: Código más legible y estándar
4. **Sin Mapeo**: No necesitas funciones de mapeo, usa campos en inglés directamente
5. **Escalabilidad**: Fácil agregar nuevos campos en inglés
6. **SQLAlchemy Nativo**: Usa el mapeo nativo de SQLAlchemy con `Column("nombre", String)`

## Migración Gradual

Puedes migrar gradualmente:

1. **Fase 1**: Usar campos en inglés en nuevos endpoints (ej: `Product.name`)
2. **Fase 2**: Refactorizar endpoints existentes para usar campos en inglés
3. **Fase 3**: Actualizar DTOs para usar nombres en inglés
4. **Fase 4**: Actualizar use cases y repositorios para usar campos en inglés

## Consideraciones

- Los nombres de tabla en la BD permanecen en español
- Los campos en la BD permanecen en español
- Los campos en el código ahora están en inglés
- SQLAlchemy mapea automáticamente entre ambos
- No hay impacto en el rendimiento
- No necesitas funciones de mapeo adicionales

## Archivos de Ejemplo

- `product_router_refactored.py`: Ejemplo completo de router refactorizado
- `product_router_english.py`: Tu router original refactorizado
- `english_usage_examples.py`: Ejemplos de uso de campos en inglés
- `__init__.py`: Todos los alias disponibles
- Todos los modelos individuales ahora tienen campos en inglés

## Próximos Pasos

1. Revisar los ejemplos de uso en inglés
2. Implementar campos en inglés en tu router actual
3. Actualizar DTOs para usar nombres en inglés
4. Refactorizar use cases para usar campos en inglés
5. Disfrutar programando completamente en inglés! 🎉
