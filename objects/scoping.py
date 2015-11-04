def hello():
    print "global hello"

class bla:
    def hello(self):
        self.thing()
        hello()

    def thing(self):
        print "hello"

b = bla()
b.hello()
