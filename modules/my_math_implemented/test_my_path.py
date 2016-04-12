# Import other modules:
from my_math.add import add
from my_math.divide import divide
from my_math.multiply import multiply
from my_math.substract import substract
from my_math.adv.fib import fibonacci
from my_math.adv.sqrt import squareroot

# Implement functions:
if __name__ == '__main__':
	print add(1, 2)
	print divide(1, 2)
	print multiply(1, 2)
	print substract(1, 2)
	print fibonacci(5)
	print squareroot(5)

	import sys
	print sys.argv

	# v = sys.argv[1].lower()
	# val_one = int(sys.argv[2])
	# val_two = int(sys.argv[3])

	# if v == 'a':
	# 	print add(val_one, val_two)
	# elif v == 'd':
	# 	print division(val_one, val_two)
	# elif v == 'm':
	# 	print multiply(val_one, val_two)
	# elif v == 's':
	# 	print substract(val_one, val_two)
	# else:
	# 	pass