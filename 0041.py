from math_helpers import is_pandigital, num_to_digits
from prime_helpers import primes_below

def main():
	largest_pandigital = 0
	num_digits = 8
	for prime in primes_below(10 ** (num_digits)):
		digits = num_to_digits(prime)
		if is_pandigital(digits, len(digits)):
			largest_pandigital = prime
	
	print(largest_pandigital)

if __name__ == '__main__':
	main()