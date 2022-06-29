from prime_helpers import is_prime

def num_consequtive_primes(a, b):
	num = 0
	n = 0
	num_primes = -1
	while num >= 0 and is_prime(num):
		num = n**2 + a*n + b
		n += 1
		num_primes += 1

	return num_primes

def find_highest_num_consequtive_primes(a_range, b_range):
	a_best = None
	b_best = None
	num_best = -1
	for a in a_range:
		for b in b_range:
			num_consequtive = num_consequtive_primes(a, b)

			if num_consequtive > num_best:
				num_best = num_consequtive
				a_best = a
				b_best = b

	print(a_best, b_best)
	return a_best, b_best

if __name__ == '__main__':
	a_range = range(-999, 1000)
	b_range = range(-1000, 1001)
	a_best, b_best = find_highest_num_consequtive_primes(a_range, b_range)

	print(a_best, b_best, a_best*b_best)