from math_helpers import num_to_digits

def remove_digit(digits, remove_digit):
	new_digits = digits.copy()
	new_digits.remove(remove_digit)
	return new_digits[0]

def get_nontrivial_simplification(fraction):
	numerator, denominator = fraction
	num_digits = num_to_digits(numerator)
	den_digits = num_to_digits(denominator)

	# Remove trivial n/n and a/b > 1
	if numerator == denominator or numerator > denominator:
		return None

	# Remove trivial a*10/b*10
	common_digits = set([digit for idx, digit in enumerate(num_digits) if (digit in den_digits and digit != 0)])

	if not common_digits:
		return None

	for common in common_digits:
		new_numerator = remove_digit(num_digits, common)
		new_denominator = remove_digit(den_digits, common)

		# Skip division
		if new_denominator == 0:
			continue

		if new_numerator / new_denominator == numerator / denominator:
			return (new_numerator, new_denominator)

	return None

def main():
	nontrivial_simplications = list()
	for numerator in range(10,100):
		for denominator in range(10,100):
			fraction = (numerator, denominator)
			new_fraction = get_nontrivial_simplification(fraction)

			if new_fraction is not None:
				nontrivial_simplications.append((fraction, new_fraction))

	print(nontrivial_simplications)
	
	big_numerator = 1
	big_denominator = 1
	for fraction, _ in nontrivial_simplications:
		numerator, denominator = fraction
		big_numerator *= numerator
		big_denominator *= denominator

	print(big_numerator, big_denominator)

if __name__ == '__main__':
	main()