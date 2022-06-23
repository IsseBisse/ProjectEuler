def is_prime(number):
	# Naive
	for div in range(2, number):
		if number%div == 0:
			return False

	return True

def largest_prime_factor(number):
	factor = 2
	prime_factors = list()
	rest = number
	while not is_prime(rest):
		while rest % factor == 0:
			prime_factors.append(factor)
			rest //= factor

		factor += 1
		while not is_prime(factor):
			factor += 1

	if rest != 1:
		prime_factors.append(rest)

	return prime_factors[-1]

def main():
	assert largest_prime_factor(13195) == 29

	print(largest_prime_factor(600851475143))

if __name__ == '__main__':
	main()