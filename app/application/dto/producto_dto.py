from datetime import datetime
from typing import Optional
from pydantic import BaseModel


class ProductResponseDTO(BaseModel):
    id: int
    name: str
    brand: int
    price: float
    category: str
    precio_dls: Optional[float]
    stock: Optional[int]
    offerDescription: Optional[str]
    supplier: Optional[int]
    availableOnline: bool
    views: int
    image: Optional[str]
    creado: datetime

    class Config:
        from_attributes = True


class ProductCreateDTO(BaseModel):
    nombre: str
    descripcion: Optional[str] = None
    precio_bs: float
    precio_dls: Optional[float] = None
    imagenes: Optional[str] = None
    codigo: Optional[str] = None
    in_stock: Optional[int] = None
    id_sub_categoria: int
    id_sucursal: int
    id_marca: int
    creado_por: Optional[str] = None
    caracteristicas: Optional[str] = None
    caracteristicas_avanzada: Optional[str] = None


class ProductUpdateDTO(BaseModel):
    nombre: Optional[str] = None
    descripcion: Optional[str] = None
    precio_bs: Optional[float] = None
    precio_dls: Optional[float] = None
    imagenes: Optional[str] = None
    codigo: Optional[str] = None
    in_stock: Optional[bool] = None
    id_sub_categoria: Optional[int] = None
    id_sucursal: Optional[int] = None
    id_marca: Optional[int] = None
    creado: Optional[datetime] = None
    caracteristicas: Optional[str] = None
    caracteristicas_avanzada: Optional[str] = None
