from decorator import singleton

@singleton
class Logger:
    def __init__(self):
        self.log = []

    def write_log(self, message):
        self.log.append(message)

    def read_log(self):
        return self.log

