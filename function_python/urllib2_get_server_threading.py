'''
-----------------------------------------------------------
BaseHTTPServer - base classes for implementing web servers:
-----------------------------------------------------------

Purpose: BaseHTTPServer includes classes that can form the basis of a web server.
Available In: 1.4 and later

BaseHTTPServer uses classes from SocketServer to create base classes for making
HTTP servers. HTTPServer can be used directly, but the BaseHTTPRequestHandler is
intended to be extended to handle each protocol method (GET, POST, etc.).

To add support for an HTTP method in your request handler class, implement the
method do_METHOD(), replacing METHOD with the name of the HTTP method.
For example, do_GET(), do_POST(), etc. For consistency, the method takes no
arguments. All of the parameters for the request are parsed by
BaseHTTPRequestHandler and stored as instance attributes of the request instance.
'''

from BaseHTTPServer import HTTPServer, BaseHTTPRequestHandler
from SocketServer import ThreadingMixIn
import threading

# EXAMPLE 1: HTTP GET - Threading and Forking:
# ==============================================================================
# HTTPServer is a simple subclass of SocketServer.TCPServer, and does not use
# multiple threads or processes to handle requests. To add threading or forking,
# create a new class using the appropriate mix-in from SocketServer.

class Handler(BaseHTTPRequestHandler):
    
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        message =  threading.currentThread().getName()
        self.wfile.write(message)
        self.wfile.write('\n')
        return

class ThreadedHTTPServer(ThreadingMixIn, HTTPServer):
    '''Handle requests in a separate thread.'''

if __name__ == '__main__':
    server = ThreadedHTTPServer(('localhost', 8080), Handler)
    print 'Starting server, use <Ctrl-C> to stop'
    server.serve_forever()