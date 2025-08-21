from datetime import date, datetime
from decimal import Decimal
from typing import Optional

from pydantic import BaseModel


class BaseFromORM(BaseModel):
    class Config:
        from_attributes = True


class ProductoModel(BaseFromORM):
    id: int
    nombre: str
    descripcion: Optional[str] = None
    precio_bs: float
    precio_dls: Optional[float] = None
    imagenes: Optional[str] = None
    codigo: Optional[str] = None
    in_stock: bool
    id_sub_categoria: int
    id_sucursal: int
    id_marca: int
    creado: Optional[datetime] = None
    creado_por: Optional[str] = None
    activo: bool
    caracteristicas: Optional[str] = None
    caracteristicas_avanzada: Optional[str] = None


class CategoriaModel(BaseFromORM):
    id: int
    nombre: str
    imagenes: Optional[str] = None
    creado: Optional[datetime] = None
    creado_por: Optional[str] = None
    activo: bool


class SubCategoriaModel(BaseFromORM):
    id: int
    nombre: str
    imagenes: Optional[str] = None
    id_categoria: int
    creado: Optional[datetime] = None
    creado_por: Optional[str] = None
    activo: bool


class StockModel(BaseFromORM):
    id: int
    id_producto: int
    cantidad_total: Optional[int] = None
    cantidad_vendida: Optional[int] = None
    cantidad_ofertada: Optional[int] = None
    creado: Optional[datetime] = None
    creado_por: Optional[str] = None
    activo: bool


class MarcaModel(BaseFromORM):
    id: int
    nombre: str
    descripcion: Optional[str] = None
    imagenes: Optional[str] = None
    logo: Optional[str] = None
    creado: Optional[datetime] = None
    creado_por: Optional[str] = None
    activo: bool


class OfertaModel(BaseFromORM):
    id: int
    descripcion: str
    porcentaje: Optional[Decimal] = None
    id_producto: Optional[int] = None
    id_categoria: Optional[int] = None
    id_sub_categoria: Optional[int] = None
    creado: Optional[datetime] = None
    creado_por: Optional[str] = None
    activo: bool


class SucursalModel(BaseFromORM):
    id: int
    nombre: str
    imagenes: Optional[str] = None
    id_empresa: int
    id_ubicacion: int
    id_usuario: int
    creado: Optional[datetime] = None
    creado_por: Optional[str] = None
    activo: bool


class EmpresaModel(BaseFromORM):
    id: int
    nombre: str
    telefono: Optional[str] = None
    id_ubicacion: int
    logo: Optional[str] = None
    creado: Optional[datetime] = None
    creado_por: Optional[str] = None
    activo: bool


class UbicacionModel(BaseFromORM):
    id: int
    nombre: str
    latitud: Decimal
    longitud: Decimal
    creado: Optional[datetime] = None
    creado_por: Optional[str] = None
    activo: bool


class WebServiceLogModel(BaseFromORM):
    id: int
    id_web_service: int
    input: Optional[str] = None
    error: Optional[str] = None
    creado: Optional[datetime] = None
    creado_por: Optional[str] = None


class WebServiceModel(BaseFromORM):
    id: int
    nombre: Optional[str] = None
    descripcion: Optional[str] = None
    url: Optional[str] = None
    creado: Optional[datetime] = None
    creado_por: Optional[str] = None
    activo: Optional[bool] = True


class BitacoraPrecioProductoModel(BaseFromORM):
    id: int
    id_producto: int
    precio_actualizado: Optional[Decimal] = None
    precio_nuevo: Optional[Decimal] = None
    porcentaje: Optional[Decimal] = None
    creado: Optional[datetime] = None
    creado_por: Optional[str] = None


class CatalogoPermisosModel(BaseFromORM):
    id: int
    nombre: Optional[str] = None
    creado: Optional[datetime] = None
    creado_por: Optional[str] = None
    activo: Optional[bool] = True


class PermisosUsuariosModel(BaseFromORM):
    id: int
    id_usuario: Optional[int] = None
    id_catalogo_permiso: Optional[int] = None
    read: Optional[bool] = False
    write: Optional[bool] = False
    delete: Optional[bool] = False
    edit: Optional[bool] = False
    creado: Optional[datetime] = None
    creado_por: Optional[str] = None
    activo: Optional[bool] = True


class SubscripcionModel(BaseFromORM):
    id: int
    nombre: Optional[str] = None
    precio: Optional[Decimal] = None
    anuncios: Optional[str] = None
    prioridad_listado: Optional[str] = None
    ubicaciones: Optional[str] = None
    estadisticas: Optional[str] = None
    soporte: Optional[str] = None
    extras: Optional[str] = None
    creado: Optional[datetime] = None
    creado_por: Optional[str] = None
    activo: Optional[bool] = True


class SubscripcionUsuarioModel(BaseFromORM):
    id: int
    id_subscripcion: int
    id_usuario: int
    activo: Optional[bool] = True
    creado: Optional[datetime] = None
    creado_por: Optional[str] = None


class UsuarioModel(BaseFromORM):
    id: int
    nombre: Optional[str] = None
    email: Optional[str] = None
    password: Optional[str] = None
    creado: Optional[datetime] = None
    creado_por: Optional[str] = None
    activo: Optional[bool] = True


class PublicidadModel(BaseFromORM):
    id: int
    id_sucursal: int
    imagenes_publicidad: Optional[str] = None
    link_destino: Optional[str] = None
    prioridad: Optional[int] = None
    fecha_inicio: Optional[date] = None
    fecha_fin: Optional[date] = None
    activo: Optional[bool] = True
    creado: Optional[datetime] = None


class EstadisticasPublicidadModel(BaseFromORM):
    id: int
    id_publicidad: Optional[int] = None
    impresiones: Optional[int] = None
    clics: Optional[int] = None
    fecha: Optional[date] = None
    creado: Optional[datetime] = None
    creado_por: Optional[str] = None
    activo: Optional[bool] = True

