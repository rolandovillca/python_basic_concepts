# EXAMPLE 1:
# ==============================================================================
def dollar(in_fnc):
	def out_fnc(in_fnc):
		return '$' + str(in_fnc)
	return out_fnc

@dollar
def price(amount):
	return amount

print price(1000)
print

# EXAMPLE 2:
# ==============================================================================
def pound1(in_fnc):
	def out_fnc(in_fnc):
		return (u"\u00A3").encode('utf-8') + str(in_fnc)
	return out_fnc

@pound1
def price1(amount):
	return amount

print price1(100)

# EXAMPLE 3: WOW!!!
# ==============================================================================
def count(f):
	def inner(*args, **kargs):
		inner.counter += 1
		return f(*args, **kargs)
	inner.counter = 0
	return inner

@count
def my_fnc():
	pass

my_fnc()
my_fnc()
my_fnc()
	
print 'my_fnc.counter', my_fnc.counter

#EXAMPLE 4:
# ==============================================================================
import time
def timer(fn):
	def inner(*args, **kargs):
		t = time.time()
		ret = fn(*args, **kargs)
		print 'timer = %s' % (time.time() - t)
	return inner

@timer
def my_fnc2():
	pass

my_fnc2()

# EXAMPLE 5:
# ==============================================================================
def bold(f):
    def wrapped():
        return '<b>' + f() + '</b>'
    return wrapped

def italic(f):
    def wrapped():
        return '<i>' + f() + '</i>'
    return wrapped

@bold
@italic
def hello():
    return 'hello'

print hello()