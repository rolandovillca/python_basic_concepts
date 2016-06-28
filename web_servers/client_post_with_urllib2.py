'''
urllib2 - Library for opening URLs

A library for opening URLs that can be extended by defining custom protocol
handlers.

The urllib2 module defines functions and classes which help in opening URLs
(mostly HTTP) in a complex world - basic and digest authentication,
redirections, cookies and more.

The urllib2 module provides an updated API for using internet resources
identified by URLs. It is designed to be extended by individual applications to
support new protocols or add variations to existing protocols (such as handling
HTTP basic authentication).

https://pymotw.com/2/urllib2/
'''

import urllib
import urllib2

# EXAMPLE 1: HTTP POST:
# ==============================================================================
# To POST form-encoded data to the remote server, instead of using GET, pass the
# encoded query arguments as data to urlopen().

query_args = { 'q':'query string', 'foo':'bar' }
encoded_args = urllib.urlencode(query_args)
url = 'http://localhost:8080/'
print urllib2.urlopen(url, encoded_args).read()


# EXAMPLE 2: Working with Requests Directly:
# ==============================================================================
# urlopen() is a convenience function that hides some of the details of how the
# request is made and handled for you. For more precise control, you may want to
# instantiate and use a Request object directly.


# EXAMPLE 3: Adding Outgoing Headers:
# ==============================================================================
# As the examples above illustrate, the default User-agent header value is made
# up of the constant Python-urllib, followed by the Python interpreter version.
# If you are creating an application that will access other people’s web
# resources, it is courteous to include real user agent information in your
# requests, so they can identify the source of the hits more easily. Using a
# custom agent also allows them to control crawlers using a robots.txt file
# (see robotparser).

import urllib2

request = urllib2.Request('http://localhost:8080/')
request.add_header('User-agent', 'PyMOTW (http://www.doughellmann.com/PyMOTW/)')

response = urllib2.urlopen(request)
data = response.read()
print data


# EXAMPLE 4: Posting Form Data:
# ==============================================================================
# You can set the outgoing data on the Request to post it to the server.

import urllib
import urllib2

query_args = { 'q':'query string', 'foo':'bar' }

request = urllib2.Request('http://localhost:8080/')
print 'Request method before data:', request.get_method()

request.add_data(urllib.urlencode(query_args))
print 'Request method after data :', request.get_method()
request.add_header('User-agent', 'PyMOTW (http://www.doughellmann.com/PyMOTW/)')

print
print 'OUTGOING DATA:'
print request.get_data()

print
print 'SERVER RESPONSE:'
print urllib2.urlopen(request).read()


# EXAMPLE 5: Uploading Files:
# ==============================================================================
# Encoding files for upload requires a little more work than simple forms.
# A complete MIME message needs to be constructed in the body of the request,
# so that the server can distinguish incoming form fields from uploaded files.

import itertools
import mimetools
import mimetypes
from cStringIO import StringIO
import urllib
import urllib2

class MultiPartForm(object):
    '''Accumulate the data to be used when posting a form.'''

    def __init__(self):
        self.form_fields = []
        self.files = []
        self.boundary = mimetools.choose_boundary()
        return
    
    def get_content_type(self):
        return 'multipart/form-data; boundary=%s' % self.boundary

    def add_field(self, name, value):
        """Add a simple field to the form data."""
        self.form_fields.append((name, value))
        return

    def add_file(self, fieldname, filename, fileHandle, mimetype=None):
        """Add a file to be uploaded."""
        body = fileHandle.read()
        if mimetype is None:
            mimetype = mimetypes.guess_type(filename)[0] or 'application/octet-stream'
        self.files.append((fieldname, filename, mimetype, body))
        return
    
    def __str__(self):
        '''Return a string representing the form data, including attached files.'''
        # Build a list of lists, each containing "lines" of the
        # request.  Each part is separated by a boundary string.
        # Once the list is built, return a string where each
        # line is separated by '\r\n'.  
        parts = []
        part_boundary = '--' + self.boundary
        
        # Add the form fields
        parts.extend(
            [ part_boundary,
              'Content-Disposition: form-data; name="%s"' % name,
              '',
              value,
            ]
            for name, value in self.form_fields
            )
        
        # Add the files to upload
        parts.extend(
            [ part_boundary,
              'Content-Disposition: file; name="%s"; filename="%s"' % \
                 (field_name, filename),
              'Content-Type: %s' % content_type,
              '',
              body,
            ]
            for field_name, filename, content_type, body in self.files
            )
        
        # Flatten the list and add closing boundary marker,
        # then return CR+LF separated data
        flattened = list(itertools.chain(*parts))
        flattened.append('--' + self.boundary + '--')
        flattened.append('')
        return '\r\n'.join(flattened)

if __name__ == '__main__':
    # Create the form with simple fields
    form = MultiPartForm()
    form.add_field('firstname', 'Doug')
    form.add_field('lastname', 'Hellmann')
    
    # Add a fake file
    form.add_file('biography', 'bio.txt', 
                  fileHandle=StringIO('Python developer and blogger.'))

    # Build the request
    request = urllib2.Request('http://localhost:8080/')
    request.add_header('User-agent', 'PyMOTW (http://www.doughellmann.com/PyMOTW/)')
    body = str(form)
    request.add_header('Content-type', form.get_content_type())
    request.add_header('Content-length', len(body))
    request.add_data(body)

    print
    print 'OUTGOING DATA:'
    print request.get_data()

    print
    print 'SERVER RESPONSE:'
    print urllib2.urlopen(request).read()


# EXAMPLE 6: Custom Protocol Handlers:
# ==============================================================================
# urllib2 has built-in support for HTTP(S), FTP, and local file access.
# If you need to add support for other URL types, you can register your own
# protocol handler to be invoked as needed. For example, if you want to support
# URLs pointing to arbitrary files on remote NFS servers, without requiring your
# users to mount the path manually, would create a class derived from
# BaseHandler and with a method nfs_open().

# The protocol open() method takes a single argument, the Request instance, and
# it should return an object with a read() method that can be used to read the
# data, an info() method to return the response headers, and geturl() to return
# the actual URL of the file being read. A simple way to achieve that is to
# create an instance of urllib.addurlinfo, passing the headers, URL, and open
# file handle in to the constructor.

import mimetypes
import os
import tempfile
import urllib
import urllib2

class NFSFile(file):
    def __init__(self, tempdir, filename):
        self.tempdir = tempdir
        file.__init__(self, filename, 'rb')
    def close(self):
        print
        print 'NFSFile:'
        print '  unmounting %s' % self.tempdir
        print '  when %s is closed' % os.path.basename(self.name)
        return file.close(self)

class FauxNFSHandler(urllib2.BaseHandler):
    
    def __init__(self, tempdir):
        self.tempdir = tempdir
    
    def nfs_open(self, req):
        url = req.get_selector()
        directory_name, file_name = os.path.split(url)
        server_name = req.get_host()
        print
        print 'FauxNFSHandler simulating mount:'
        print '  Remote path: %s' % directory_name
        print '  Server     : %s' % server_name
        print '  Local path : %s' % tempdir
        print '  File name  : %s' % file_name
        local_file = os.path.join(tempdir, file_name)
        fp = NFSFile(tempdir, local_file)
        content_type = mimetypes.guess_type(file_name)[0] or 'application/octet-stream'
        stats = os.stat(local_file)
        size = stats.st_size
        headers = { 'Content-type': content_type,
                    'Content-length': size,
                  }
        return urllib.addinfourl(fp, headers, req.get_full_url())

if __name__ == '__main__':
    tempdir = tempfile.mkdtemp()
    try:
        # Populate the temporary file for the simulation
        with open(os.path.join(tempdir, 'file.txt'), 'wt') as f:
            f.write('Contents of file.txt')
        
        # Construct an opener with our NFS handler
        # and register it as the default opener.
        opener = urllib2.build_opener(FauxNFSHandler(tempdir))
        urllib2.install_opener(opener)

        # Open the file through a URL.
        response = urllib2.urlopen('nfs://remote_server/path/to/the/file.txt')
        print
        print 'READ CONTENTS:', response.read()
        print 'URL          :', response.geturl()
        print 'HEADERS:'
        for name, value in sorted(response.info().items()):
            print '  %-15s = %s' % (name, value)
        response.close()
    finally:
        os.remove(os.path.join(tempdir, 'file.txt'))
        os.removedirs(tempdir)