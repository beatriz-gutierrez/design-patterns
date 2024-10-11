from abc import ABC, abstractmethod

class Port(ABC):
    """
    Abstract class for creating ports.
    One of its subclasses will be created in the factory methods.
    """

    @abstractmethod
    def __str__(self):
        """
        A string representation of the port.
        """
        pass

class HHTPort(Port):
    """
    A concrete class for creating HTTP ports.
    """

    def __str__(self):
        return '80'
    
class HTTPSecurePort(Port):
    """
    A concrete class for creating HTTPS ports.
    """

    def __str__(self):
        return '443'
    
class FTPPort(Port):
    """
    A concrete class for creating FTP ports.
    """

    def __str__(self):
        return '21'
    
