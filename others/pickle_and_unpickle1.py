'''
The pickle module implements binary protocols for serializing and de-serializing
a Python object structure. “Pickling” is the process whereby a Python object
hierarchy is converted into a byte stream,
and “unpickling” is the inverse operation, whereby a byte stream (from a binary
file or bytes-like object) is converted back into an object hierarchy. Pickling
(and unpickling) is alternatively known as “serialization”, “marshalling,” or
“flattening”; however, to avoid confusion, the terms used here are “pickling”
and “unpickling”.

url: https://pymotw.com/2/pickle/
'''


# EXAMPLE 1: Encoding and Decoding Data in Strings:
# ==============================================================================
# Once the data is serialized, you can write it to a file, socket, pipe, etc.
# Then later you can read the file and unpickle the data to construct a new
# object with the same values.

# By default, the pickle will contain only ASCII characters.
# A more efficient binary format is also available, but all of the examples
# here use the ASCII output because it is easier to understand in print.

try:
    import cPickle as pickle
except:
    import pickle
import pprint

data1 = [ { 'a':'A', 'b':2, 'c':3.0 } ]
print 'BEFORE:',
pprint.pprint(data1)

data1_string = pickle.dumps(data1)

data2 = pickle.loads(data1_string)
print 'AFTER:',
pprint.pprint(data2)

print 'SAME?:', (data1 is data2)
print 'EQUAL?:', (data1 == data2)

# As you see, the newly constructed object is the equal to but not the same
# object as the original. No surprise there.


# EXAMPLE 2: Working with Streams:
# ==============================================================================
# In addition to dumps() and loads(), pickle provides a couple of convenience
# functions for working with file-like streams. It is possible to write multiple
# objects to a stream, and then read them from the stream without knowing in
# advance how many objects are written or how big they are.

try:
    import cPickle as pickle
except:
    import pickle
import pprint
from StringIO import StringIO

class SimpleObject(object):

    def __init__(self, name):
        self.name = name
        l = list(name)
        l.reverse()
        self.name_backwards = ''.join(l)
        return

data = []
data.append(SimpleObject('pickle'))
data.append(SimpleObject('cPickle'))
data.append(SimpleObject('last'))

# Simulate a file with StringIO
out_s = StringIO()

# Write to the stream
for o in data:
    print 'WRITING: %s (%s)' % (o.name, o.name_backwards)
    pickle.dump(o, out_s)
    out_s.flush()

# Set up a read-able stream
in_s = StringIO(out_s.getvalue())

# Read the data
while True:
    try:
        o = pickle.load(in_s)
    except EOFError:
        break
    else:
        print 'READ: %s (%s)' % (o.name, o.name_backwards)

# The example simulates streams using StringIO buffers, so we have to play a
# little trickery to establish the readable stream. A simple database format
# could use pickles to store objects, too, though shelve would be easier to work with.


# EXAMPLE 3: Problems Reconstructing Objects:
# ==============================================================================
