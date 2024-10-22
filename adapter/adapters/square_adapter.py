from payments_processor import PaymentProcessor
from payment_gateways.square import Square

class SquareAdapter(PaymentProcessor):

    def __init__(self, square: Square) -> None:
        self._square = square

    def process_payment(self, currency: str, amount: int) -> None:
        self._square.charge(currency, amount)