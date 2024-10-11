from abc import ABC, abstractmethod

class Port(ABC):
    """
    An abrstract product that represents port to connect.
     Its subclasses will be created in factory methods.
    """

    @abstractmethod
    def __str__(self):
        """
        A string representation of the port
        """
        pass

class HTTPPort(Port):
    """
    A concrete product which represents HTTP port.
    """
    def __str__(self):
        return '80'
    
class HTTPSecurePort(Port):
    """
    A concrete product which represents HTTPS port.
    """
    def __str__(self):
        return '443'
    
class FTPPort(Port):
    """
    A concrete product which represents FTP port.
    """
    def __str__(self):
        return '21'
    

    
