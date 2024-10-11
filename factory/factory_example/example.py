from http.client import HTTPConnection
from ftplib import FTP
class SimpleFactory():

    @staticmethod
    def build_connection(protocol):
        if protocol == 'http':
            return HTTPConnection(host='127.1.0.0')
        elif protocol == 'ftp':
            return FTP('127.0.0.1')
        else:
            raise RuntimeError('Unknown protocol')


if __name__ == '__main__':
    protocol_type = input('Which protocol to use? (http or ftp): ')
    protocol = SimpleFactory.build_connection(protocol_type)

    protocol.connect()
    response = protocol.get_response()
    print(response)
