from primes_helpers import primes_below

def sum_of_primes_below(limit):
	primes = primes_below(limit)
	return sum(primes)

def main():
	print(sum_of_primes_below(10))
	print(sum_of_primes_below(int(2e6)))

if __name__ == '__main__':
	main()