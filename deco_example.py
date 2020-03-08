def b_function(func):
	"""
	Функция которая принимает другую функцию.
	"""

	def c_func():
		val = "Результат от %s это %s" % (func(), eval(func()))

		return val

	return c_func


def a_function():
	"""Обычная функция"""
	return "1+1"


if __name__ == "__main__":
	value = a_function()
	print(value)
	decorator = b_function(a_function)
	print(decorator())