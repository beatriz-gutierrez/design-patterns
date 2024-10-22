from enum import Enum
from adapters.paypal_adapter import PayPalAdapter
from adapters.square_adapter import SquareAdapter
from adapters.stripe_adapter import StripeAdapter
from payment_gateways.paypal import PayPal
from payment_gateways.square import Square
from payment_gateways.stripe import Stripe
from payments_processor import PaymentProcessor

class PaymentProcessorType(Enum):
    paypal = "paypal"
    square = "square"
    stripe = "stripe"

class Application:

    @staticmethod
    def _get_payment_processor_instance(payment_processor: Enum) -> PaymentProcessor:

        if payment_processor == PaymentProcessorType.paypal:
            return PayPalAdapter(PayPal())
        elif payment_processor == PaymentProcessorType.square:
            return SquareAdapter(Square())
        elif payment_processor == PaymentProcessorType.stripe:
            return StripeAdapter(Stripe())
        else:
            raise ValueError("Invalid payment processor")

    @staticmethod
    def checkout(currency: str, amount: int, payment_processor: Enum) -> None:

        print(f"Processing checkout (selected '{payment_processor}')")
        Application._get_payment_processor_instance(payment_processor).process_payment(currency, amount)
        print(f"Checkout complete (selected '{payment_processor}')\n")
