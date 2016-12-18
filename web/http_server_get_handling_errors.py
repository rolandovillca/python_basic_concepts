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


# EXAMPLE 1: HTTP GET - Handling Errors:
# ==============================================================================
# Error handling is made easy with send_error(). Simply pass the appropriate
# error code and an optional error message, and the entire response (with
# headers, status code, and body) is generated automatically.

class ErrorHandler(BaseHTTPRequestHandler):
    
    def do_GET(self):
        self.send_error(404)
        return

if __name__ == '__main__':
    from BaseHTTPServer import HTTPServer
    server = HTTPServer(('localhost', 8080), ErrorHandler)
    print 'Starting server, use <Ctrl-C> to stop'
    server.serve_forever()