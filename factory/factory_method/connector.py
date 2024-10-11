from abc import ABC, abstractmethod
from urllib.request import urlopen
from port import FTPPort, HHTPort, HTTPSecurePort, Port
from bs4 import BeautifulSoup


class Connector(ABC):
    """
    Abstract class to connect to remote reource. 
    This class provides two factory methods for creating protocol and port that must be implemented by concrete connectors.
    """
    def __init__(self, is_secure):
        self.is_secure = is_secure
        self.port = self.port_factory_method()
        self.protocol = self.protocol_factory_method()

    @abstractmethod
    def parse(self):
        """
        Parses web content. Abstract method to be implemented by concrete connectors.
        """
        pass

    def read(self, host, path):
        """
        A generic method for reading web content.
        """
        # url = self.protocol + '://' + host + str(self.port) + path
        url = f"{self.protocol}://{host}{path}"
        print(f"Connecting to {url}")
        return urlopen(url, timeout=2).read()

    @abstractmethod
    def protocol_factory_method(self) -> str:
        """
        A factory method that must be implemented by concrete connectors.
        """
        pass

    @abstractmethod
    def port_factory_method(self) -> Port:
        """
        A factory method that must be implemented by concrete connectors.
        """
        pass


class HTTPConnector(Connector):
    """
    A concrete connector that creates a HTTP connector and sets in runtime all its attributes
    """

    def protocol_factory_method(self) -> str:
        if self.is_secure:
            return "https"
        return "http"

    def port_factory_method(self) -> Port:
        if self.is_secure:
            return HTTPSecurePort()
        return HHTPort()

    def parse(self, content):
        """
        Parses web content
        """
        soup = BeautifulSoup(content, 'lxml')
        links = soup.table.findAll("a")

        #return soup.prettify()
        return "\n".join([link["href"] for link in links])


class FTPConnector(Connector):
    """
    A concrete connector that creates a FTP connector and sets in runtime all its attributes
    """

    def protocol_factory_method(self) -> str:
        return "ftp"

    def port_factory_method(self) -> Port:
        return FTPPort()

    def parse(self, content):
        """
        Parses ftp content
        """
        # decode bytes to string
        lines = content.decode('utf-8').split("\n")
        filenames = []

        for line in lines:
            # ftp format has 8 columns
            splitted_line = line.split(None, 8)
            if len(splitted_line) == 9:
                filenames.append(splitted_line[-1])

        return "\n".join(filenames)
