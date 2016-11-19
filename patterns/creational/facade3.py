from abc import ABCMeta, abstractmethod

class Base(metaclass=ABCMeta):
    @abstractmethod
    def foo(self):
        pass

    @abstractmethod
    def bar(self):
        pass


class Concrete(Base):
    def __init__(self):
        super(Concrete, self).__init__()

    def print_class_name(self):
        print 'class namei is: {}'.format(__name__)


if __name__ == '__main__':
    concrete = Concrete()
    concrete.print_class_name()