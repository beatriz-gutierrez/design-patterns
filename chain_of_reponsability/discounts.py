from abc import ABC, abstractmethod
from typing import Dict, List, Optional 

from product import Product

class Discounts():

    def __init__(self, 
                 discounts: List['BaseDiscount'], 
                 available_products: Dict[str, Product]) -> None:
        self._discounts: Optional[List['BaseDiscount']] = discounts
        self._available_products: Optional[Dict[str, Product]] = available_products

        # TODO: why we do this for here?
        discounts_count = len(self._discounts)
        for index, discount in enumerate(self._discounts):
            if index < (discounts_count - 1):
                discount.set_next(self._discounts[index + 1])

    def calculate_total_discount(self, products: Dict[str, int]) -> int:
        if not self._discounts:
            raise ValueError("Need to have setup at least one discount.")

        # TODO: why index 0?
        return self._discounts[0].execute(products, self._available_products)


class BaseDiscount(ABC):

    def __init__(self) -> None:
        # typing: forward reference
        self._next_discount: Optional['BaseDiscount'] = None

    def set_next(self, discount: 'BaseDiscount') -> None:
        self._next_discount = discount

    @abstractmethod
    def calculate_discount(self, 
                           products: Dict[str, int],
                           available_products: Dict[str, Product]) -> int:
        pass

    def execute(self, 
                products: Dict[str, int], 
                available_products: Dict[str, Product]) -> int:
        discount = self.calculate_discount(products, available_products)
        if not self._next_discount:
            return discount
        
        return discount + self._next_discount.execute(products, available_products)


# --- Available discount imlementations: ---

class NoDiscount(BaseDiscount):

    def calculate_discount(self,
                           products: Dict[str, int],
                           available_products: Dict[str, Product]) -> int:
        return 0


class BuyNGetOneFreeDiscount(BaseDiscount):

    def __init__(self, product_code: str, amount: int) -> None:
        super().__init__()
        self._product_code: str = product_code
        self._amount: int = amount
 
    def calculate_discount(self,
                           products: Dict[str, int],
                           available_products: Dict[str, Product]) -> int:
        discount = 0

        if self._product_code not in products:
            return discount
        
        quantity = products[self._product_code]
        while quantity > 0 and quantity >= self._amount:
            quantity -= self._amount
            discount += available_products[self._product_code].price

        return discount

class BulkPurchasePriceDiscount(BaseDiscount):
    # Buy N units to have a reduced per unit price

    def __init__(self, product_code: str, amount: int, reduced_price: int) -> None:
        super().__init__()
        self._product_code: str = product_code
        self._amount: int = amount
        self._reduced_price: int = reduced_price

    def calculate_discount(self,
                           products: Dict[str, int],
                           available_products: Dict[str, Product]) -> int:
        discount = 0

        if self._product_code not in products:
            return discount

        quantity = products[self._product_code]
        if quantity >= self._amount:
            original_aggregated_price = available_products[self._product_code].price * quantity
            discount = original_aggregated_price - self._reduced_price * quantity

        return discount
