from http.client import HTTPConnection
from ftplib import FTP
import http.server
import socketserver
import threading

"""
 let's set up a simple HTTP server using Python's built-in http.server module
"""
class SimpleFactory():

    @staticmethod
    def get_connection(protocol):
        if protocol == 'http':
            return HTTPConnection(host='127.0.0.1', port=8000)
        elif protocol == 'ftp':
            return FTP('127.0.0.1')
        else:
            raise RuntimeError('Unknown protocol')
        
    @staticmethod
    def get_response(protocol):
        if protocol == 'http':
            conn = HTTPConnection(host='127.0.0.1', port=8000)
            conn.request('GET', '/')
            return conn.getresponse()
        elif protocol == 'ftp':
            conn = FTP('127.0.0.1')
            conn.login()
            response = []
            conn.retrlines('LIST', response.append)
            return '\n'.join(response)
        else:
            raise RuntimeError('Unknown protocol')

def start_http_server():
    handler = http.server.SimpleHTTPRequestHandler
    with socketserver.TCPServer(("", 8000), handler) as httpd:
        print("serving at port 8000")
        httpd.serve_forever()

if __name__ == '__main__':
    
    # Started the HTTP server in a separate thread to allow the main script to continue running.
    server_thread = threading.Thread(target=start_http_server)
    server_thread.daemon = True
    server_thread.start()

    protocol_type = input('Which protocol to use? (http or ftp): ')
    
    response = SimpleFactory.get_response(protocol_type)
    print(response)
    if protocol_type == 'http':
        print(response.status, response.reason)
        print(response.read().decode())
