# Modelos de base de datos con alias en inglés
from .product import ProductORM
from .category import CategoryORM
from .subcategory import SubCategoryORM
from .brand import BrandORM
from .branch import BranchORM
from .company import CompanyORM
from .location import LocationORM
from .user import UserORM
from .stock import StockORM
from .offer import OfferORM
from .advertisement import AdvertisementORM
from .subscription import SubscriptionORM
from .user_subscription import UserSubscriptionORM
from .user_permission import UserPermissionORM
from .permission_catalog import PermissionCatalogORM
from .web_service import WebServiceORM
from .web_service_log import WebServiceLogORM
from .price_history import PriceHistoryORM
from .ad_statistics import AdStatisticsORM
from .image import ImageORM
from .image_categories import ImageCategoryORM
from .currency import CurrencyORM

# Modelos de base de datos con nombres en inglés

# Alias para mantener la consistencia en el código
# Ahora tanto las clases como los campos están en inglés
Product = ProductORM
Category = CategoryORM
SubCategory = SubCategoryORM
Brand = BrandORM
Branch = BranchORM
Company = CompanyORM
Location = LocationORM
User = UserORM
Stock = StockORM
Offer = OfferORM
Advertisement = AdvertisementORM
Subscription = SubscriptionORM
UserSubscription = UserSubscriptionORM
UserPermission = UserPermissionORM
PermissionCatalog = PermissionCatalogORM
WebService = WebServiceORM
WebServiceLog = WebServiceLogORM
PriceHistory = PriceHistoryORM
AdStatistics = AdStatisticsORM
Image = ImageORM
ImageCategory = ImageCategoryORM
Currency = CurrencyORM

# Exportar todos los modelos
__all__ = [
    # Modelos en inglés
    'ProductORM', 'CategoryORM', 'SubCategoryORM', 'BrandORM', 'BranchORM',
    'CompanyORM', 'LocationORM', 'UserORM', 'StockORM', 'OfferORM',
    'AdvertisementORM', 'SubscriptionORM', 'UserSubscriptionORM', 'UserPermissionORM',
    'PermissionCatalogORM', 'WebServiceORM', 'WebServiceLogORM', 'PriceHistoryORM',
    'AdStatisticsORM', 'ImageORM', 'CurrencyORM', 'ImageCategoryORM',
    
    # Alias para compatibilidad
    'Product', 'Category', 'SubCategory', 'Brand', 'Branch', 'Company', 'Location',
    'User', 'Stock', 'Offer', 'Advertisement', 'Subscription', 'UserSubscription',
    'UserPermission', 'PermissionCatalog', 'WebService', 'WebServiceLog', 'PriceHistory',
    'AdStatistics', 'Image', 'Currency', 'ImageCategory'
]
