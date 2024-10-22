from payments_processor import PaymentProcessor
from payment_gateways.stripe import Stripe

class StripeAdapter(PaymentProcessor):

    def __init__(self, stripe: Stripe) -> None:
        self._stripe = stripe

    def process_payment(self, currency: str, amount: int) -> None:
        self._stripe.make_payment(currency, amount)

