from math import sqrt

from prime_helpers import is_prime, primes_below

LIMIT = int(1e4)
PRIMES = primes_below(LIMIT)

def is_goldbach(number):
	for prime in PRIMES:
		if prime > number:
			return False

		rem = number - prime
		if rem % 2 != 0:
			continue

		rem //= 2
		if sqrt(rem).is_integer():
			return True

def main():	
	for number in range(3, LIMIT, 2):
		if number in PRIMES:
			continue

		if not is_goldbach(number):
			break

	print(number)	


if __name__ == '__main__':
	main()