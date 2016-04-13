def add(x, y):
	return x + y

def division(x, y):
	return x / y

def multiply(x, y):
	return x * y

def substract(x, y):
	return x - y

if __name__ == '__main__':
	import sys
	print sys.argv

	v = sys.argv[1].lower()
	val_one = int(sys.argv[2])
	val_two = int(sys.argv[3])

	if v == 'a':
		print add(val_one, val_two)
	elif v == 'd':
		print division(val_one, val_two)
	elif v == 'm':
		print multiply(val_one, val_two)
	elif v == 's':
		print substract(val_one, val_two)
	else:
		pass