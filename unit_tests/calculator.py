class Calculator(object):
    def sum(self, x, y):
        return x + y

    def sub(self, x, y):
        return x - y

    def mul(self, x, y):
        return x * y;

    def div(self, x, y):
        return x/y if y != 0 else 0
