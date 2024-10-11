from abstract_factory import HTTPFactory, FTPFactory
from connector import Connector
from urllib.error import URLError

if __name__ == "__main__":
    domain = 'ftp.freebsd.org'
    path = '/pub/FreeBSD/'

    protocol = input(f'Connecting to {domain}. Which protocol to use? (0-http or 1-ftp): ')

    if protocol == '0':
        is_secure = bool(input('Use secure connection? (1-yes, 0-no): '))
        factory = HTTPFactory(is_secure=is_secure)
    elif protocol == '1':
        is_secure = False
        factory = FTPFactory(is_secure=is_secure)
    else:
        print('Sorry, wrong answer')

    connector = Connector(factory)
    try:
        content = connector.read(domain, path)
        print(factory.create_parser()(content))
    except URLError as e:
        print(f"Can't access resource with this method: {e}")
