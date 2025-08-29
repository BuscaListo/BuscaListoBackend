from datetime import datetime
from sqlalchemy.orm import Session
from app.infrastructure.db.models.currency import CurrencyORM
from app.application.dto.db_models import CurrencyModel


def create_currency(db: Session, currency_data: CurrencyModel) -> CurrencyORM:
    new_currency = CurrencyORM(
        currency=currency_data.name,
        price_bs=currency_data.exchange_rate,
        created_at=datetime.utcnow(),
        created_by=currency_data.created_at,
        active=1
    )
    db.add(new_currency)
    db.commit()
    db.refresh(new_currency)
    return new_currency
