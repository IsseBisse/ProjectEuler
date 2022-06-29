from math import ceil

from math_helpers import num_to_digits, is_pandigital

def concat_products(number, n):
	products = list()
	for mult in range(1, n+1):
		products.append(number*mult)

	return int("".join([str(prod) for prod in products]))

def main():
	pandigital_numbers = list()
	for n in range(2, 10):
		max_num_digits = ceil(9 / n)
		for number in range(1, 10**max_num_digits):
			number_string = concat_products(number, n)
			digits = num_to_digits(number_string)
			if is_pandigital(digits, 9):
				pandigital_numbers.append(int(number_string))

	pandigital_numbers.sort()
	print(pandigital_numbers[-1])


if __name__ == '__main__':
	main()