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

import urllib2


# EXAMPLE 1: HTTP GET:
# ==============================================================================
# As with urllib, an HTTP GET operation is the simplest use of urllib2.
# Pass the URL to urlopen() to get a "file-like" handle to the remote data.

url = 'http://www.google.com'
resp = urllib2.urlopen(url)
print 'Response: ', resp
print 'Url: ', resp.geturl()
print 'Code: ', resp.code
print 'Html: ', resp.read()
print

headers = resp.info()
print 'Date: ', headers['date']
print 'Server: ', headers['server']
print 'Headers:'
print headers
print

data = resp.read()
print 'Length: ', len(data)
print 'Data:'
print data
print


# EXAMPLE 2: The file-like object returned by urlopen() is iterable:
# ==============================================================================
for line in resp:
    print line.rstrip()


# EXAMPLE 3: Encoding Arguments:
# ==============================================================================
# Arguments can be passed to the server by encoding them with urllib.urlencode()
# and appending them to the URL.

import urllib

url = 'http://www.google.com?'

query_args = { 'q':'query string', 'foo':'bar' }
encoded_args = urllib.urlencode(query_args)
print 'Encoded: ', encoded_args

url = url + encoded_args
print urllib2.urlopen(url).read()