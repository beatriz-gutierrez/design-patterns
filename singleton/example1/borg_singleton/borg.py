class Borg():
    # class attribute
    _shared_stage = {}

    def __new__(cls, *args, **kwargs):
        obj = super().__new__(cls, *args, **kwargs)
        obj.__dict__ = cls._shared_stage
        return obj
    
class ChildB(Borg):
    pass

class ChildB_NoSharedState(Borg):
    _shared_stage = {}

if __name__ == "__main__":
    borg1 = Borg()
    borg2 = Borg()
    print(borg1._shared_stage)
    print(borg2._shared_stage)
    print(borg1 is borg2)

    child_b = ChildB()
    borg1.only_one_var = "hello"
    print(borg1._shared_stage)
    print(child_b._shared_stage)
    print(child_b is borg1)

    child_c = ChildB_NoSharedState()
    print(child_c._shared_stage)
    print(borg1._shared_stage)

