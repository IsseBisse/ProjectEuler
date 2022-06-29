from math_helpers import num_to_digits, digits_to_num
from prime_helpers import primes_below, is_prime

def is_truncatable(prime):
	digits = num_to_digits(prime)
	if len(digits) == 1:
		return False

	# From left to right
	for start_ind, _ in enumerate(digits):
		number = digits_to_num(digits[start_ind:])
		if not is_prime(number):
			return False
		
	# From right to left
	for offset, _ in enumerate(digits):
		end_ind = len(digits) - offset
		number = digits_to_num(digits[:end_ind])
		if not is_prime(number):
			return False

	return True

def main():
	truncatable_primes = list()
	
	limit = 10
	while len(truncatable_primes) < 11:
		for prime in primes_below(limit):
			if is_truncatable(prime) and not prime in truncatable_primes:
				truncatable_primes.append(prime)

		limit *= 10

	print(truncatable_primes)
	print(sum(truncatable_primes))

if __name__ == '__main__':
	main()