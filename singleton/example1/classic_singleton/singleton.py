class Singleton:

    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, "instance"):
            cls.instance = super().__new__(cls)

        return cls.instance

    def __init__(self, value: str = None) -> None:
        self.value = value


class Child(Singleton):
    def __new__(cls, *args, **kwargs):
        return super().__new__(cls)
    
    