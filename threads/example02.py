import threading
import time

class ThreadingExample(object):
    '''
    Threading example class.
    The run() method will be started and
    it will run in the background until the application exits.
    '''
    def __init__(self, interval=1):
        '''
        Constructor
        :type interval: int
        :param interval: Check interval, in seconds.
        '''
        self.interval = interval
        thread = threading.Thread(target=self.run, args=())
        thread.daemon = True # Daemonize thread
        thread.start()       # Start the execution

    def run(self):
        '''
        Method tha runs forver.
        Once a thread object is created, its activity must be started by calling
        the thread's start() method. This invokes the run() method in a separate
        thread of control.
        '''
        while True:
            # Do something
            print 'Doing something imporant in the background'
            time.sleep(20)

example = ThreadingExample()
time.sleep(30)
print 'Checkpoint'
time.sleep(30)
print 'Bye'