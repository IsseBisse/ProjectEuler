def is_pandigital(digits, n):
	if len(digits) != n:
		return False

	if sorted(digits) != list(range(1,n+1)):
		return False

	return True

def num_to_digits(number):
	return [int(c) for c in str(number)]

def main():
	# 111 * 111 = 12321 is more than 9 digits so this limit should be enough
	limit = 12321
	products = list()
	for numerator in range(1, limit):
		for denominator in range(1, numerator):
			if numerator % denominator == 0:
				fraction = numerator // denominator

				digits = num_to_digits(numerator) + \
					num_to_digits(denominator) + \
					num_to_digits(fraction)

				if is_pandigital(digits, 9):
					products.append(numerator)

	products = set(products)

	print(products)
	print(sum(products))

if __name__ == '__main__':
	main()