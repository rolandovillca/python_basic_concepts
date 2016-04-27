import abc

class Observer(object):
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def update():
        raise

class ConcreteObserver(object):
    pass

if __nama__ == '__main__':
    print 'thing'
    conc = ConcreteObserver()