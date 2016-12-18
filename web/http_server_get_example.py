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

# EXAMPLE 1: HTTP GET:
# ==============================================================================
# This example request handler illustrates how to return a response to the client
# and some of the local attributes which can be useful in building the response.

class GetHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        parsed_path = urlparse.urlparse(self.path)
        message_parts = [
            'CLIENT_VALUES:',
            'client_address=%s (%s)' % (self.client_address,
                                        self.address_string()),
            'command=%s' % self.command,
            'path=%s' % self.path,
            'real path=%s' % parsed_path.path,
            'query=%s' % parsed_path.query,
            'request_version=%s' % self.request_version,
            '',
            'SERVER VALUES:',
            'server_version=%s' % self.server_version,
            'sys_version=%s' % self.sys_version,
            'protocol_version=%s' % self.protocol_version,
            '',
            'HEADERS RECEIVED:',
        ]

        for name, value in sorted(self.headers.items()):
            message_parts.append('%s=%s' % (name, value.rstrip()))
        message_parts.append('')
        message = '\r\n'.join(message_parts)
        self.send_response(200)
        self.end_headers()
        self.wfile.write(message)
        return

if __name__ == '__main__':
    from BaseHTTPServer import HTTPServer
    server = HTTPServer(('localhost', 8080), GetHandler)
    print 'Starting server, use <Ctrl-C> to stop.'
    server.serve_forever()