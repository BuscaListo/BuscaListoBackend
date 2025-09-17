from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.infrastructure.session import get_db
from typing import Dict, Optional, List
from pydantic import BaseModel
from datetime import datetime
from app.application.bcv_process.scraper import get_bcv_currency_rates
from app.application.bcv_process.create_currency import create_currency
from app.application.dto.db_models import CurrencyModel, CurrencyEnum, CurrencyResponse


router = APIRouter()

@router.post("/load_currencies_in_db", response_model=dict[str, float], status_code=status.HTTP_201_CREATED)
async def load_currencies_in_db(db: Session = Depends(get_db)):
    """
    Extraer los precios desde el BCV para almacenarlos en la DB
    ```
    example={
        "euro": 156,12340000,
        "yuan": 20,45760000,
        "lira": 7,89760000,
        "rublo": 1,23450000,
        "dolar": 145,74530000
    }
    ```
    """
    data_bcv = get_bcv_currency_rates()
    
    currency_symbols = {
        'euro': '€',
        'yuan': '¥', 
        'lira': '₺',
        'rublo': '₽',
        'dolar': '$'
    }
    
    for currency, rate in data_bcv.items():
        data_currency = CurrencyModel(
            id=0,  # Will be auto-generated
            code=currency.upper()[:3],
            name=currency,
            symbol=currency_symbols.get(currency, currency[0].upper()),
            exchange_rate=rate,
            active=True
        )
        create_currency(db, data_currency)
    return data_bcv


@router.get("/currencies", response_model=List[CurrencyResponse])
async def get_currencies(db: Session = Depends(get_db)):
    """
    Endpoint to fetch all currencies from database.
    """
    from app.infrastructure.db.models.currency import CurrencyORM
    currencies = db.query(CurrencyORM).filter(CurrencyORM.active == True).all()
    print("currencies",currencies)
    return currencies


@router.get("/only_currency", response_model=CurrencyResponse)
async def get_only_currency(currency: CurrencyEnum, db: Session = Depends(get_db)):
    """
    Endpoint to fetch specific currency from database.
    """
    from app.infrastructure.db.models.currency import CurrencyORM
    
    result = db.query(CurrencyORM).filter(
        CurrencyORM.currency == currency.value,
        CurrencyORM.active == True
    ).first()
    
    if not result:
        raise HTTPException(status_code=404, detail=f"Currency '{currency}' not found")
    
    return result
