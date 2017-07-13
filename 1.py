import sys

class CustomError(Exception):
	pass


def divide(x, y):
	try:
		a = int(x)**int(y)
	except ValueError:
		print("Error: please enter integer number")
		a = 0
	except ZeroDivisionError:
		print("Can't divide by zero")
		a = 0
	except:
		print("Unknown Error")
		a = 0
	finally:
		if a == 1:
			raise CustomError("This is a custom error")
		return a

def func2():
	pass

def func3():
	pass




if len(sys.argv) == 3:
	print("Division = " + str(divide(sys.argv[1], sys.argv[2])))
else:
	print("Please enter two numbers exactly")
