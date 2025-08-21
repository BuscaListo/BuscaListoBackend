from dataclasses import dataclass
from datetime import datetime
from typing import Optional


@dataclass
class Image:
    id: int
    url: Optional[str]
    id_producto: Optional[int]
    activo: bool
    creado: datetime
    creado_por: Optional[str]
