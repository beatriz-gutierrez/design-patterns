# https://www.perplexity.ai/search/explain-the-model-view-control-T61lbUXIQ7OdBDNHinHcrQ?login-source=floatingSignup


class Singleton:
    _instande = None

    def __new__(cls, *args, **kwargs) -> Singleton:
        if cls._instance is None:
            cls.instance = super().__new__(cls, *args, **kwargs)
        return cls._instance

    def __init__(self) -> None:
        pass
