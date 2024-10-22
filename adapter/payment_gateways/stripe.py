class Stripe:

    def make_payment(self, currency: str, amount: int) -> None:

        print(f"Processing payment of {currency} {amount} through Stripe.")