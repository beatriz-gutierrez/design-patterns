from collections import defaultdict
from typing import Optional, Dict

from discounts import Discounts
import settings

class ShoppingCart():

    def __init__(self, discounts: Discounts) -> None:
        self._discounts: Discounts = discounts
        self._cart: defaultdict = defaultdict(int)

    def add_product(self, product_code: str, quantity:Optional[int] = 1) -> None:
        
        if product_code not in settings.AVAILABLE_PRODUCTS_MAP:
            raise ValueError(f"Product code {product_code} not available")
        
        self._cart[product_code] += quantity

    def empty(self) -> None:
        self._cart = defaultdict(int)

    @property
    def contents(self) -> Dict[str, int]:
        return {
           settings.AVAILABLE_PRODUCTS_MAP[product_code]._friendly_name: quantity 
           for product_code, quantity in self._cart.items()
        }
    
    @property
    def total_amount_without_discounts(self) -> int:
        return sum([
            settings.AVAILABLE_PRODUCTS_MAP[product_code]._price * quantity
            for product_code, quantity in self.cart.items()
        ])
    
    @property
    def total_amount(self) -> int:
        return (
            self.total_amount_without_discounts - 
            self._discounts.calculate_total_discount(self._cart)
        )

    @property
    def cart(self) -> defaultdict:
        return self._cart
