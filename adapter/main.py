from app import Application, PaymentProcessorType

if __name__ == "__main__":

    app = Application()

    app.checkout("SEK", 50000, PaymentProcessorType.paypal)

    app.checkout("DKK", 432, PaymentProcessorType.stripe)

    app.checkout("EUR", 250, PaymentProcessorType.square)
