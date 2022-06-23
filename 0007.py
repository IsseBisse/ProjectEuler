import math

def is_prime(number):
	# Naive
	for div in range(2, int(math.sqrt(number))+1):
	# for div in range(2, number):
		if number%div == 0:
			return False

	return True

def nth_prime(n):	
	if n == 1:
		return 2

	elif n == 2:
		return 3

	base = 6
	primes_found = 2

	while True:
		for offset in [-1, 1]:
			number = base + offset
			if is_prime(number):
				primes_found += 1

				if primes_found == n:
					return number

		base += 6

def main():
	print(nth_prime(6))
	print(nth_prime(10001))

if __name__ == '__main__':
	main()