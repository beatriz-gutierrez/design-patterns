class Singleton():
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, 'instance'):
            cls.instance = super().__new__(cls)
        return cls.instance

    def __init__(
        self, to_visit: set = set(), downloaded: set = set()
    ):
        self.to_visit = to_visit
        self.downloaded = downloaded

    # def __init__(self, queue_to_parse: list = [], to_visit: set = set(), downloaded: set = set()):
    #     self.queue_to_parse = queue_to_parse
    #     self.to_visit = to_visit
    #     self.downloaded = downloaded
