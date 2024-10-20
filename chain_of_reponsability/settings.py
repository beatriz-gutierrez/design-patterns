from product import Product
from discounts import BulkPurchasePriceDiscount, BuyNGetOneFreeDiscount

# All prices are in euro cents

# Product codes definitions
PRODUCT_CODE_A = "PRODUCT CODE #1"
PRODUCT_CODE_B = "PRODUCT CODE #2"
PRODUCT_CODE_C = "PRODUCT CODE #3"

# Products avaible to be purchased
AVAILABLE_PRODUCTS = [
    Product(
        code=PRODUCT_CODE_A, friendly_name="Product A user-friendly name", price=500
    ),
    Product(
        code=PRODUCT_CODE_B, friendly_name="Product B user-friendly name", price=1000
    ),
    Product(
        code=PRODUCT_CODE_C, friendly_name="Product C user-friendly name", price=750
    ),
]

# Active discounts, applied in order
DISCOUNTS = [
    BuyNGetOneFreeDiscount(product_code=PRODUCT_CODE_A, amount=2), # 2 by 1
    BulkPurchasePriceDiscount(product_code=PRODUCT_CODE_B, amount=3, reduced_price=900)
]


AVAILABLE_PRODUCTS_MAP = {
    product.code: product for product in AVAILABLE_PRODUCTS
}
