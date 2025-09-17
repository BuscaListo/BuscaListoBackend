from datetime import datetime
from typing import Optional, List
from pydantic import BaseModel


class BaseProduct(BaseModel):
    """Clase base con campos comunes de productos"""
    id: int
    name: str
    brand_id: Optional[int]
    price_bs: float
    price_usd: Optional[float]
    subcategory_id: Optional[int]
    in_stock: Optional[int]
    branch_id: Optional[int]
    active: bool
    views: int
    created_at: datetime

    class Config:
        from_attributes = True


class ProductResponseDTO(BaseProduct):
    # Campos adicionales específicos para este DTO
    image_url: Optional[str] = None
    offer_description: Optional[str] = ""
    brand_name: Optional[str] = None
    subcategory_name: Optional[str] = None
    category_name: Optional[str] = None
    category_key: Optional[str] = None
    category_id: Optional[int] = None
    company_name: Optional[str] = None
    branch_name: Optional[str] = None


class RecentProductResponseDTO(BaseProduct):
    # Campos adicionales específicos para este DTO
    brand_name: str  # nombre de la marca
    subcategory_name: str
    offer_description: Optional[str] = ""
    image_url: Optional[str]


class BaseProductCreateUpdate(BaseModel):
    """Clase base para creación y actualización de productos"""
    name: Optional[str] = None
    description: Optional[str] = None
    price_bs: Optional[float] = None
    price_usd: Optional[float] = None
    images: List[str] = []
    code: Optional[str] = None
    in_stock: Optional[int] = 0
    features: Optional[List[str]] = [""]
    advanced_features: Optional[List[str]] = [""]


class ProductCreateDTO(BaseProductCreateUpdate):
    """DTO para crear productos - campos requeridos"""
    name:           str 
    description:    str
    price_usd:      float
    in_stock:       int
    code:           str
    images:         list[str]
    subcategory:    str
    branch:         str
    brand:          str
    created_by:     Optional[str] = None

class ProductUpdateDTO(BaseProductCreateUpdate):
    """DTO para actualizar productos - todos los campos opcionales"""
    subcategory_id: Optional[int] = None
    branch_id: Optional[int] = None
    brand_id: Optional[int] = None
    created_at: Optional[datetime] = None


class MockCommentDTO(BaseModel):
    id: int
    product_id: int
    user_name: str
    user_avatar: str
    rating: int
    comment: str
    created_at: str
    helpful_votes: int
    is_verified_purchase: bool


class ProductInfoDTO(BaseProduct):
    """Información básica del producto"""
    code: Optional[str] = None
    brand_name: Optional[str] = None
    subcategory_name: Optional[str] = None
    category: Optional[str] = None
    imagenes: List[str] = []
    characteristics: Optional[str] = None
    advancedCharacteristics: Optional[str] = None
    accessories: Optional[str] = None
    highlightedFeatures: Optional[str] = None
    pros: Optional[str] = None
    cons: Optional[str] = None


class PricingDTO(BaseModel):
    """Información de precios y ofertas"""
    price_bs: float
    price_usd: Optional[float]
    price_offer_usd: Optional[float]
    price_offer_bs: Optional[float]
    discount_percent: Optional[float]
    offer_description: Optional[str]


class CompanyDTO(BaseModel):
    """Información del proveedor/sucursal"""
    supplier_id: Optional[int]
    supplier_name: str
    supplier_branch: Optional[str]
    supplier_address: Optional[str]
    supplier_phone: Optional[str]
    supplier_email: Optional[str]
    supplier_website: Optional[str]
    supplier_hours: Optional[str]
    supplier_rating: Optional[float]
    supplier_reviews: Optional[int]


class MetaDTO(BaseModel):
    """Metadatos del producto"""
    views: int
    created_at: datetime
    url: str
    mockComments: List[MockCommentDTO]


class ProductDetailDTO(BaseModel):
    """DTO principal que agrupa toda la información del producto"""
    product: ProductInfoDTO
    pricing: PricingDTO
    company: CompanyDTO
    meta: MetaDTO

    class Config:
        from_attributes = True


class SearchResultDTO(BaseModel):
    """DTO para resultados de búsqueda"""
    id: int
    name: str
    brand_name: Optional[str] = None
    price_bs: float
    price_usd: Optional[float] = None
    image_url: Optional[str] = None
    subcategory_name: Optional[str] = None
    category_name: Optional[str] = None
    branch_name: Optional[str] = None
    company_name: Optional[str] = None
    views: int
    created_at: datetime
    in_stock: Optional[int] = None
    offer_description: Optional[str] = None

    class Config:
        from_attributes = True


class SearchResponseDTO(BaseModel):
    """DTO para respuesta completa de búsqueda"""
    products: List[SearchResultDTO]
    total: int
    page: int
    limit: int
    total_pages: int
    search_term: str
    category: Optional[str] = None
    sort_by: str
    sort_order: str

    class Config:
        from_attributes = True


class SearchSuggestionsDTO(BaseModel):
    """DTO para sugerencias de búsqueda"""
    suggestions: List[str]
    search_term: str

    class Config:
        from_attributes = True
