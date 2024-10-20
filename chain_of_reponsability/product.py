class Product:
    def __init__(self, code: str, friendly_name: str, price: int) -> None:
        self._code = code
        self._friendly_name = friendly_name
        self._price = price

    @property
    def code(self) -> str:
        return self._code
    
    @property
    def friendly_name(self) -> str:
        return self._friendly_name
    
    @property 
    def price(self) -> int:
        return self._price