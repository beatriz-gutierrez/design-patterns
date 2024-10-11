from wrapper import _SingletonWrapper

def singleton(cls):
    """
    A singleton decorator. Returns a wrapper object.
    A call on that object returns a single instance object
    of decorated class. 
    Use the __wrapped__  attribute to access to the decorated 
    class directly in unit tests.
    """
    return _SingletonWrapper(cls)