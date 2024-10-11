from abc import ABC, abstractmethod
from port import FTPPort, HTTPPort, HTTPSecurePort
from parser import FTPParser, HTTPParser

"""
The abstract factory defines the interface of the factories.
"""
class AbstractFactory(ABC):

    def __init__(self, is_secure):
        self.is_secure = is_secure

    @abstractmethod
    def create_protocol(self):
        pass

    @abstractmethod
    def create_port(self):
        pass

    @abstractmethod
    def create_parser(self):
        pass


class HTTPFactory(AbstractFactory):
    """
    Concrete factory for building HTTP connection
    """

    def create_protocol(self):
        if self.is_secure:
            return "https"
        return "http"

    def create_port(self):
        if self.is_secure:
            return HTTPSecurePort()
        return HTTPPort()

    def create_parser(self):
        return HTTPParser()


class FTPFactory(AbstractFactory):
    """
    Concrete factory for building FTP connection
    """

    def create_protocol(self):
        return "ftp"

    def create_port(self):
        return FTPPort()

    def create_parser(self):
        return FTPParser()
