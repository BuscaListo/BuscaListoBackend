from sqlalchemy import func
from datetime import datetime
from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from app.infrastructure.db.models import ProductORM,SubCategoryORM,BranchORM,BrandORM,CurrencyORM
from app.application.dto.product_dto import ProductCreateDTO


def verify_in_db(field_in: str, tb_name: str, db: Session ,model_ORM) -> int:
    """Obtiene valor id para un <field_in> en la tabla <tb_name>"""
    print(5*'=')
    print(f"OBTENIENDO ID VALOR {tb_name}")
    id_output = 0
    try:
        id_field  = 0
        str_field = ''
        try:
            id_field  = int(float(field_in))
            print(f"Id {tb_name} detectado")
        except:
            str_field = str(field_in).lower()
            print(f"Cadena {tb_name} detectada")
        if id_field != 0:
            print(f"ID {tb_name}, valor:",id_field)
            sub_category_orm = db.query(model_ORM).filter(model_ORM.id == id_field).first()
            if not sub_category_orm:
                raise HTTPException(
                    status_code=status.HTTP_404_NOT_FOUND,
                    detail=f"Id {tb_name} "+str(id_field)+" No existe"
                )
            id_output = id_field
            print(f"{tb_name} nombre encontrada:",sub_category_orm.name)
        else:
            print(f"Traducir {tb_name} encontrada",str_field)
            search_by_name = db.query(model_ORM).filter(
                func.lower(model_ORM.name) == func.lower(str_field),
                model_ORM.active == True
            ).first()
            if not search_by_name:
                #Busqueda de similares
                sugerencias = db.query(model_ORM.name,model_ORM.id).filter(
                    model_ORM.name.ilike(f"%{field_in}%"),
                    model_ORM.active == True
                ).all()
                sugerencias = {s[1]:s[0] for s in sugerencias}
                items = list(sugerencias.items())
                print('Sugerencias Detectadas',sugerencias)
                if len(sugerencias) == 1:
                    id_output = items[0][0]
                    print(f"{tb_name} Detectada por sugerencia",id_output,'-',items[0][1])
                elif len(sugerencias) == 0:
                    raise HTTPException(
                        status_code=status.HTTP_404_NOT_FOUND,
                        detail=f"No se encontro {tb_name} para "+ str_field
                    )
                else:
                    raise HTTPException(
                        status_code=status.HTTP_404_NOT_FOUND,
                        detail=f"{tb_name} sugeridas "+'|'.join([e[1] for e in items])+". Se encontro mas de un resultado para "+ str_field
                    )
            else:
                id_output = int(search_by_name.id)
                print(f"{tb_name} encontrada por name correctamente")
    except Exception as err:
        print("Error:",err)
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail= str(err)
        )
    print(f"Id {tb_name} encontrado:",id_output)
    print(5*'=')
    return id_output

def create_product_use_case(db: Session, product_data: ProductCreateDTO) -> ProductORM:
    # Validation product data
    print("Product Data IN:",product_data)
    print("Verificando Datos de producto")
    #####################
    # Verify Sub-Category
    #####################
    sub_category_out = verify_in_db(
        field_in=str(product_data.subcategory).strip(),
        tb_name= 'SubCategoria',
        db= db,
        model_ORM=SubCategoryORM
    )
    ##########################
    # Verify Branch (Sucursal)
    ##########################
    branch_out = verify_in_db(
        field_in=str(product_data.branch).strip(),
        tb_name= 'Sucursales',
        db= db,
        model_ORM=BranchORM
    )
    ##########################
    # Verify Brand (Marca)
    ##########################
    brand_out = verify_in_db(
        field_in=str(product_data.brand).strip(),
        tb_name= 'Marcas',
        db= db,
        model_ORM=BrandORM
    )
    ##########################
    # Convert USD->BS
    ##########################
    print(5*"=")
    print("OBTENIENDO PRECIO PRODUCTO BS")
    price_product_usd = 0
    try:
        price_product_usd = float(product_data.price_usd)
    except Exception as err:
        print(err)
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail= 'Precio usd en formato incorrecto: '+str(err)
        )
    # Get currency USD
    print("Precio producto enviado:",price_product_usd)
    price_bs_by_usd  = db.query(CurrencyORM.price_bs).filter(CurrencyORM.currency == 'USD').first()
    all_currencies = db.query(CurrencyORM).all()
    import pdb
    from sqlalchemy import text
    result = db.execute(text("SELECT * FROM moneda"))
    rows = result.fetchall()
    print("Registros SQL directo:", len(rows))

    pdb.set_trace()
    for currency in all_currencies:
        print(f"ID: {currency.id}, Currency: '{currency.currency}', Price: {currency.price_bs}")

    print("Tasa USD -> BS obtenida:",price_bs_by_usd)
    try:
        price_product_bs = price_bs_by_usd * price_product_usd
    except Exception as err:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail= 'Precio bs no calculado. Verificar tabla moneda: '+str(err)
        )

    print("Obtenido precio bs:",price_product_bs)
    print(5*"=")

    print("Data: OK")
    nuevo_producto = ProductORM(
        name              = product_data.name,
        description       = product_data.description,
        price_bs          = price_product_bs,
        price_usd         = price_product_usd,
        images            = product_data.images,
        code              = product_data.code,
        in_stock          = product_data.in_stock if product_data.in_stock is not None else 1,
        subcategory_id    = sub_category_out,
        branch_id         = branch_out,
        brand_id          = brand_out,
        created_at        = datetime.utcnow(),
        created_by        = product_data.created_by,
        features          = product_data.features,
        advanced_features = product_data.advanced_features,
        active            = 1
    )

    #db.add(nuevo_producto)
    #db.commit()
    #db.refresh(nuevo_producto)

    ##########################
    # INSERT IMAGES-PRODUCTS
    ##########################
    print(5*"=")
    print("INSERTANDO IMAGENES DEL PRODUCTO")
    print(5*"=")

    return nuevo_producto

