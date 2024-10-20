from discounts import Discounts
from shopping_cart import ShoppingCart

class Checkout:

    def __init__(self, discounts: Discounts) -> None:
        self._shopping_cart = ShoppingCart(discounts)

    def add_product(self, product_code: str) -> None:
        self._shopping_cart.add_product(product_code)

    def empty(self) -> None:
        self._shopping_cart.empty()

    @property
    def total(self) -> str:
        return f"{self._shopping_cart.total_amount / 100:.2f} €"
    
    @property
    def contents(self) -> str:
        return "\n".join([
            f"{product_name} x {quantity}"
            for product_name, quantity in self._shopping_cart.contents.items()
        ])
