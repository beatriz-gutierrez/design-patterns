from abstract_factory import AbstractFactory
from urllib.request import urlopen
from abc import abstractmethod

class Connector():
    """ 
    A client
    """

    def __init__(self, factory: AbstractFactory):
        self.protocol = factory.create_protocol()
        self.port = factory.create_port()
        self.parser = factory.create_parser()

    def read(self, host, path):
        url = self.protocol + "://" + host + ":" + str(self.port) + path
        print(f"Connecting to {url}")
        return urlopen(url, timeout=2).read()
    
    # @abstractmethod
    # def parse(self, content):
    #     pass