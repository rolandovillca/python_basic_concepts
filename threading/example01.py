'''
Method of operation of the threading.Thread class: The class threading.Thread
has a method start(), which can start a Thread.

It triggers off the method run(), which has to be overloaded. The join()
method makes sure that the main program waits until all threads have terminated.
'''

import time
from threading import Thread

# Target function:
def sleeper(i):
    print 'thread {} sleeps for 5 seconds'.format(i)
    time.sleep(5)
    print 'thread {} wope up'.format(i)

# Run the threads:
for i in range(10):
    t = Thread(target=sleeper, args=(i,))
    t.start()