from abc import ABC, abstractmethod
from bs4 import BeautifulSoup

class Parser(ABC):
    """
    An abstract product which represents parser to parse web content.
    Its subclasses will be created in factory methods
    """

    @abstractmethod
    def __call__(self, content):
        pass

class HTTPParser(Parser):
    """
    A concrete product which represents HTTP parser.
    """
    def __call__(self, content):
        filenames = []
        soup = BeautifulSoup(content, 'html.parser')
        links = soup.table.find_all('a')
        for link in links:
            filenames.append(link.text)
        return '\n'.join(filenames)
    

class FTPParser(Parser):
    """
    A concrete product which represents FTP parser.
    """
    def __call__(self, content):
        lines = content.decode('utf-8').split('\n')
        
        filenames = []
        for line in lines:
            splitted_line =line.split(None, 8)
            if len(splitted_line) == 9:
                filenames.append(splitted_line[-1])
        
        return '\n'.join(filenames)
