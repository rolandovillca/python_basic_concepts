'''
Proxy pattern has three essential elements:
    Real Subject - that performs the business objectives, represented by Proxy.
    Proxy Class - that acts as an interface to user requests and shields the real subject.
    Client - that makes the requests for getting the job done.
'''

import time

class Manager(object):
    ''' The Real Subject class '''
    def work(self):
        print 'Sales Manager Working.'

    def talk(self):
        print 'Hello, we can talk now.'

class Receptionist(object):
    ''' The Proxy class '''

    def __init__(self):
        self.manager_busy = False # indicate whether Manager is available
        self._manager = None

    def work(self):
        print 'Receptionist checking for Manager availability...'
        time.sleep(1)
        if not self.manager_busy:
            print 'Manager ready to talk'
            self._manager = Manager()
            time.sleep(1)
            self._manager.talk()
        else:
            print 'Soryy, Manager is busy, no time to talk.'

if __name__ == '__main__':
    proxy = Receptionist()
    proxy.work()
    proxy.manager_busy = True
    proxy.work()