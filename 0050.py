from prime_helpers import primes_below

def main():
	limit = 1000000
	primes = primes_below(limit)

	max_length = 1
	while sum(primes[:max_length]) < limit:
		max_length += 1 

	print(max_length)

	for length in reversed(range(max_length+1)):
		start = 0
		prime_sum = sum(primes[start:start+length])
		while prime_sum < limit and prime_sum not in primes:
			start += 1
			prime_sum = sum(primes[start:start+length])

		if prime_sum in primes:
			break

	print(prime_sum)


if __name__ == '__main__':
	main()