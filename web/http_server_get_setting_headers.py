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

https://pymotw.com/2/BaseHTTPServer/index.html#module-BaseHTTPServer
'''

from BaseHTTPServer import BaseHTTPRequestHandler
import urlparse
import time

# EXAMPLE 1: HTTP GET - Setting Headers:
# ==============================================================================
# The send_header method adds header data to the HTTP response. It takes two
# arguments, the name of the header and the value.

class GetHandler(BaseHTTPRequestHandler):
    
    def do_GET(self):
        self.send_response(200)
        self.send_header('Last-Modified', self.date_time_string(time.time()))
        self.end_headers()
        self.wfile.write('Response body\n')
        return

if __name__ == '__main__':
    from BaseHTTPServer import HTTPServer
    server = HTTPServer(('localhost', 8080), GetHandler)
    print 'Starting server, use <Ctrl-C> to stop'
    server.serve_forever()