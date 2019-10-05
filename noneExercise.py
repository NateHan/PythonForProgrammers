

def square(number):
	if isinstance(number, (int, float)):
		return number * number
	else:
		return None

print(square(3))
print(square("three"))