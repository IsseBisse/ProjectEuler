def sum_of_squares(numbers):
	numbers_squared = [num**2 for num in numbers]
	return sum(numbers_squared)

def square_of_sum(numbers):
	return sum(numbers) ** 2

def diff(numbers):
	return abs(square_of_sum(numbers) - sum_of_squares(numbers))

def main():
	numbers = range(1, 101)
	print(diff(numbers))

if __name__ == '__main__':
	main()