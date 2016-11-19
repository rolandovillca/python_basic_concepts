import abc

class Shape(object):
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def draw(self):
        pass


class Rectangle(Shape):
    def __init__(self):
        super(Rectangle, self).__init__()

    def draw(self):
        print 'Drawing Rectangle...'


class Square(Shape):
    def __init__(self):
        super(Square, self).__init__()

    def draw(self):
        print 'Drawing Square...'


class DemoFacade():
    def __init__(self):
        self.rectangle = Rectangle()
        self.square = Square()

    def draw_rectangle(self):
        self.rectangle.draw()

    def draw_square(self):
        self.square.draw()


# main class.

if __name__ == '__main__':
    shape_facade = DemoFacade()
    shape_facade.draw_rectangle()
    shape_facade.draw_square()