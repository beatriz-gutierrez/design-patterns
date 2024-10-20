import settings
from discounts import Discounts
from checkout import Checkout


if __name__ == "__main__":

    discounts = Discounts(settings.DISCOUNTS, settings.AVAILABLE_PRODUCTS_MAP)

    checkout = Checkout(discounts)

    my_shopping = [
        settings.PRODUCT_CODE_A,
        settings.PRODUCT_CODE_A,
        settings.PRODUCT_CODE_B,
        settings.PRODUCT_CODE_C,
        settings.PRODUCT_CODE_C,
        settings.PRODUCT_CODE_C,
    ]

    for product in my_shopping:
        checkout.add_product(product)

    print("\nCheckout - Cart content:")
    print(checkout.contents)
    print(f"\n Shopping total: {checkout.total}")
