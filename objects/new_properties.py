class C(object):
    def foo(self):
        print "Hi!"

def bar(self):
    print "Bork bork bork!"

c = C()
C.bar = bar
c.bar()

c.foo()
