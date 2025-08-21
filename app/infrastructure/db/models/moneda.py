from pydantic import BaseModel
from typing import Optional
from datetime import datetime
from decimal import Decimal


class Moneda(BaseModel):
    id: Optional[int]  
    divisa: Optional[str]
    precio_bs: Optional[Decimal]
    creado: Optional[datetime]
    creado_por: Optional[str]
    activo: Optional[bool] = True
