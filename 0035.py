from math_helpers import num_to_digits
from prime_helpers import primes_below, is_prime

def is_circular(prime):
	digits = num_to_digits(prime)
	
	num_digits = len(digits)
	for start_ind in range(num_digits):
		rotation = list()
		for offset in range(num_digits):
			i = (start_ind + offset) % num_digits
			rotation.append(digits[i])
		
		rotation = int("".join(map(str, rotation)))
		
		if not is_prime(rotation):
			return False
		
	return True
	# print(digits) 

def main():
	circular_primes = list()
	for prime in primes_below(int(1e6)):
		if is_circular(prime):
			circular_primes.append(prime)

	print(circular_primes)
	print(len(circular_primes))

if __name__ == '__main__':
	main()