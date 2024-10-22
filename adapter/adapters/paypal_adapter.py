from payments_processor import PaymentProcessor
from payment_gateways.paypal import PayPal

class PayPalAdapter(PaymentProcessor):

    def __init__(self, paypal: PayPal) -> None:
        self._paypal = paypal

    def process_payment(self, currency: str, amount: int) -> None:
        self._paypal.send_payment(currency, amount)