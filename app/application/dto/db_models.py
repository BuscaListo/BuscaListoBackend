from datetime import date, datetime
from decimal import Decimal
from typing import Optional
from enum import Enum

from pydantic import BaseModel


class BaseFromORM(BaseModel):
    class Config:
        from_attributes = True


class ProductModel(BaseFromORM):
    id: int
    name: str
    description: Optional[str] = None
    price_bs: float
    price_usd: Optional[float] = None
    images: Optional[str] = None
    code: Optional[str] = None
    in_stock: int
    subcategory_id: int
    branch_id: int
    brand_id: int
    created_at: Optional[datetime] = None
    created_by: Optional[str] = None
    active: int
    features: Optional[str] = None
    advanced_features: Optional[str] = None


class CategoryModel(BaseFromORM):
    id: int
    name: str
    images: Optional[str] = None
    created_at: Optional[datetime] = None
    created_by: Optional[str] = None
    active: bool


class SubCategoryModel(BaseFromORM):
    id: int
    name: str
    images: Optional[str] = None
    category_id: int
    created_at: Optional[datetime] = None
    created_by: Optional[str] = None
    active: bool


class StockModel(BaseFromORM):
    id: int
    product_id: int
    total_quantity: Optional[int] = None
    sold_quantity: Optional[int] = None
    offered_quantity: Optional[int] = None
    created_at: Optional[datetime] = None
    created_by: Optional[str] = None
    active: bool


class BrandModel(BaseFromORM):
    id: int
    name: str
    description: Optional[str] = None
    images: Optional[str] = None
    logo: Optional[str] = None
    created_at: Optional[datetime] = None
    created_by: Optional[str] = None
    active: bool


class OfferModel(BaseFromORM):
    id: int
    description: str
    percentage: Optional[Decimal] = None
    product_id: Optional[int] = None
    category_id: Optional[int] = None
    subcategory_id: Optional[int] = None
    created_at: Optional[datetime] = None
    created_by: Optional[str] = None
    active: bool


class BranchModel(BaseFromORM):
    id: int
    name: str
    images: Optional[str] = None
    company_id: int
    location_id: int
    user_id: int
    created_at: Optional[datetime] = None
    created_by: Optional[str] = None
    active: bool


class CompanyModel(BaseFromORM):
    id: int
    name: str
    phone: Optional[str] = None
    email: Optional[str] = None
    website: Optional[str] = None
    logo: Optional[str] = None
    created_at: Optional[datetime] = None
    created_by: Optional[str] = None
    active: bool


class LocationModel(BaseFromORM):
    id: int
    address: str
    city: str
    state: str
    country: str
    postal_code: Optional[str] = None
    latitude: Optional[float] = None
    longitude: Optional[float] = None
    created_at: Optional[datetime] = None
    created_by: Optional[str] = None
    active: bool


class UserModel(BaseFromORM):
    id: int
    username: str
    email: str
    full_name: str
    phone: Optional[str] = None
    role: str
    created_at: Optional[datetime] = None
    created_by: Optional[str] = None
    active: bool


class AdvertisementModel(BaseFromORM):
    id: int
    title: str
    description: str
    image_url: str
    start_date: date
    end_date: date
    active: bool
    created_at: Optional[datetime] = None
    created_by: Optional[str] = None


class SubscriptionModel(BaseFromORM):
    id: int
    name: str
    description: str
    price: float
    duration_days: int
    features: Optional[str] = None
    active: bool
    created_at: Optional[datetime] = None
    created_by: Optional[str] = None


class UserSubscriptionModel(BaseFromORM):
    id: int
    user_id: int
    subscription_id: int
    start_date: date
    end_date: date
    status: str
    created_at: Optional[datetime] = None
    created_by: Optional[str] = None


class UserPermissionModel(BaseFromORM):
    id: int
    user_id: int
    permission_id: int
    granted: bool
    created_at: Optional[datetime] = None
    created_by: Optional[str] = None
    active: bool


class PermissionCatalogModel(BaseFromORM):
    id: int
    name: str
    description: str
    module: str
    action: str
    created_at: Optional[datetime] = None
    created_by: Optional[str] = None
    active: bool


class WebServiceModel(BaseFromORM):
    id: int
    name: str
    url: str
    api_key: str
    description: Optional[str] = None
    active: bool
    created_at: Optional[datetime] = None
    created_by: Optional[str] = None


class WebServiceLogModel(BaseFromORM):
    id: int
    web_service_id: int
    request_data: str
    response_data: str
    status_code: int
    execution_time: float
    created_at: Optional[datetime] = None
    created_by: Optional[str] = None


class PriceHistoryModel(BaseFromORM):
    id: int
    product_id: int
    old_price: float
    new_price: float
    change_date: datetime
    reason: Optional[str] = None
    created_at: Optional[datetime] = None
    created_by: Optional[str] = None


class AdStatisticsModel(BaseFromORM):
    id: int
    advertisement_id: int
    views: int
    clicks: int
    conversions: int
    date: date
    created_at: Optional[datetime] = None
    created_by: Optional[str] = None
    active: bool


class ImageModel(BaseFromORM):
    id: int
    url: str
    alt_text: Optional[str] = None
    product_id: Optional[int] = None
    category_id: Optional[int] = None
    subcategory_id: Optional[int] = None
    brand_id: Optional[int] = None
    branch_id: Optional[int] = None
    company_id: Optional[int] = None
    created_at: Optional[datetime] = None
    created_by: Optional[str] = None
    active: bool


class CurrencyModel(BaseFromORM):
    id: int
    code: str
    name: str
    symbol: str
    exchange_rate: float
    active: bool
    created_at: Optional[datetime] = None
    created_by: Optional[str] = None


class CurrencyResponse(BaseFromORM):
    id: int
    currency: str
    price_bs: float
    created_at: Optional[datetime] = None
    created_by: Optional[str] = None
    active: bool

class CurrencyEnum(str, Enum):
    euro = "euro"
    yuan = "yuan"
    lira = "lira"
    rublo = "rublo"
    dolar = "dolar"
    