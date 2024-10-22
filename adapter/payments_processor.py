from abc import ABC, abstractmethod

class PaymentProcessor(ABC):
    
    @abstractmethod
    def process_payment(self, currency: str, amount: int) -> None:
        raise NotImplementedError("Method not implemented")
    
