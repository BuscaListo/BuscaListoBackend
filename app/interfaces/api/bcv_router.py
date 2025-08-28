from fastapi import APIRouter, status, HTTPException
from sqlmodel import select
from typing import Dict, Optional, List
from sqlalchemy.orm import Session
from app.application.bcv_process.scraper import get_bcv_currency_rates
from app.infrastructure.db.models.type_change import TypeChange
from app.application.bcv_process.scraper import get_bcv_currency_rates

router = APIRouter(prefix="/currencies", tags=["currencies"])

@router.get(
        "/load_currencies_in_db", 
        response_model=TypeChange, 
        status_code=status.HTTP_201_CREATED
)
def load_currencies_in_db(db: Session) -> Dict[str, Optional[str]]:
    """
    Extraer los precios desde el BCV para almacenarlos en la DB

    data_bcv = {
        "euro": "156,12340000",
        "yuan": "20,45760000",
        "lira": "7,89760000",
        "rublo": "1,23450000",
        "dolar": "145,74530000"
    }
    """

    data_bcv = get_bcv_currency_rates()
    data_bcv = TypeChange.model_validate(data_bcv)
    db.add(data_bcv)
    db.commit()
    db.refresh(data_bcv)
    return data_bcv


@router.get("/list_currencies", response_model=List[TypeChange])
def get_list_currencies(db: Session) -> Dict[str, Optional[str]]:
    """
    Endpoint to fetch BCV currency rates.
    """
    return db.exec(select(TypeChange)).all()


# @router.get("/currencies", response_model=Dict[str, Optional[str]])
# def get_only_currency() -> Dict[str, Optional[str]]:
#     """
#     Endpoint to fetch BCV currency rates.
#     """
#     return get_bcv_currency_rates()
