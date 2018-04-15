"""
Just a timer example.
"""

from contextlib import ContextDecorator
from contextlib import contextmanager
from time import sleep, time

class Timed:
    def __enter__(self):
        self.start = time()
        print 'Starting at {}'.format(self.start)

    def  exit(self, xtype, xvalue, xtraceback):
        if xtraceback:
            print 'Type: {}'.format(xtype)
            print 'Value: {}'.format(sxvalue)
            print 'Traceback:'.format(xtraceback)
        self.end = time()
        total = self.end - self.start
        print 'Ending at: {}, Total: {}'.format(self.end, total)
