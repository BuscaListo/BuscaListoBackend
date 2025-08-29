import requests
from enum import Enum
from bs4 import BeautifulSoup
from typing import Dict, List, Optional


class Config(Enum):
    BASE_URL = "https://www.bcv.org.ve/bcv/contactos"
    DEFAULT_CURRENCIES = ("euro", "yuan", "lira", "rublo", "dolar")


class CurrencyScraper:
    """Scraper to extract currency values from BCV website."""

    BASE_URL: str = Config.BASE_URL.value

    def __init__(self, currencies: Optional[List[str]] = None) -> None:
        default_currencies = Config.DEFAULT_CURRENCIES.value
        self.currencies = currencies or default_currencies

    def fetch_page(self) -> str:
        response = requests.get(self.BASE_URL, timeout=10, verify=False)
        response.raise_for_status()
        return response.text

    def parse_currency_value(self, html: str, currency_id: str) -> Optional[float]:
        soup = BeautifulSoup(html, "html.parser")
        element = soup.find("div", id=currency_id)
        if not element:
            return None
        value_tag = element.find("strong")
        if not value_tag:
            return None
        
        text_value = value_tag.get_text(strip=True)
        try:
            # Replace comma with dot for decimal conversion
            normalized_value = text_value.replace(",", ".")
            return round(float(normalized_value), 8)
        except (ValueError, TypeError):
            return None

    def get_currency_values(self) -> Dict[str, Optional[float]]:
        html = self.fetch_page()
        return {
            currency: self.parse_currency_value(html, currency)
            for currency in self.currencies
        }


def get_bcv_currency_rates() -> Dict[str, Optional[float]]:
    scraper = CurrencyScraper()
    return scraper.get_currency_values()
