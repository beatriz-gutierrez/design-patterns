class _SingletonWrapper:
    """
    A singleton wrapper class.
    Its instances would be created for decorated class.
    """
    
    def __init__(self, cls):
        self.__wrapped__ = cls
        self._instance = None

    def __call__(self, *args, **kwargs):
        """Returns a single instance of decorated class"""
        if self._instance is None:
            self._instance = self.__wrapped__(*args, *kwargs)
        return self._instance