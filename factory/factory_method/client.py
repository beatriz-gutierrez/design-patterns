from connector import HTTPConnector, FTPConnector
from urllib.error import URLError
from urllib.parse import urljoin

if __name__=="__main__":
    domain = 'ftp.freebsd.org'
    path = '/pub/FreeBSD/'

    protocol = input(f'Connecting to {domain}. Which protocol to use? (0-http or 1-ftp): ')

    if protocol == '0':
        is_secure = bool(input('Use secure connection? (1-yes, 0-no): '))
        connector = HTTPConnector(is_secure=is_secure)
    elif protocol == '1':
        connector = FTPConnector(is_secure=False)
    else:
        print('Sorry, wrong answer')

    try:
        # url = urljoin(f"{connector.protocol_factory_method()}://{domain}:{connector.port_factory_method()}", path)
        # url = urljoin(f"{connector.protocol_factory_method()}://{domain}", path)
        url = urljoin(f"{connector.protocol}://{domain}", path)
        print(f"Connecting to {url}")

        content = connector.read(domain, path)
        print(connector.parse(content))

    except URLError as e:
        print(f"Can't access resource with this method: {e}")
