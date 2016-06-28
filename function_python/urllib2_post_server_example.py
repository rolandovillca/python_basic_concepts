from BaseHTTPServer import BaseHTTPRequestHandler
import cgi

# EXAMPLE 1: HTTP POST:
# ==============================================================================
# Supporting POST requests is a little more work, because the base class does
# not parse the form data for us. The cgi module provides the FieldStorage class
# which knows how to parse the form, if it is given the correct inputs.

class PostHandler(BaseHTTPRequestHandler):
    def do_POST(self):
        # Parse the form data posted:
        form = cgi.FieldStorage(
            fp=self.rfile,
            headers=self.headers,
            environ={'REQUEST_METHOD':'POST',
                     'CONTENT_TYPE':self.headers['Content-Type'],
                     })

        # Begin the response:
        self.send_response(200)
        self.end_headers()
        self.wfile.write('Client: %s\n' % str(self.client_address))
        self.wfile.write('User-agent: %s\n' % str(self.headers['user-agent']))
        self.wfile.write('Path: %s\n' % self.path)
        self.wfile.write('Form data:\n')

        # Echo back information about what was posted in the form:
        for field in form.keys():
            field_item = form[field]
            if field_item.filename:
                # The field contains an uploaded file:
                file_data = field_item.file.read()
                file_len = len(file_data)
                del file_data
                self.wfile.write('\tUploaded %s as "%s" (%d bytes)\n' % \
                        (field, field_item.filename, file_len))
            else:
                # Regular form value:
                self.wfile.write('\t%s=%s\n' % (field, form[field].value))

if __name__ == '__main__':
    from BaseHTTPServer import HTTPServer
    server = HTTPServer(('localhost', 8080), PostHandler)
    print 'Starting server, use <Strl-C> to stop.'
    server.serve_forever()