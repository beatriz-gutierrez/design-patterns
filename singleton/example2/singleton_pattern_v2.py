class OneOnly:

    _singleton = None

    def __new__(cls, *args, **kwargs):

        if not cls._singleton:
            cls._singleton = super().__new__(cls, *args, **kwargs)

        return cls._singleton
    
if __name__ == "__main__":
    o1 = OneOnly()
    o2 = OneOnly()

    assert o1 == o2

    print(o1)
    print(o2)

    print(o1._singleton)
    print(o2._singleton)
