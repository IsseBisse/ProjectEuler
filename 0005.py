from functools import reduce

def is_prime(number):
	# Naive
	for div in range(2, number):
		if number%div == 0:
			return False

	return True

def prime_factors_dict(number):
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

	occurances = list_to_dict(prime_factors)

	return occurances

def list_to_dict(list_):
	return {number:list_.count(number) for number in list_}

def dict_to_list(dict_):
	list_ = list()
	for key, value in dict_.items():
		list_ += [key] * value

	return list_

def main():
	limit = 20 + 1
	non_primes = [number for number in range(1, limit) if not is_prime(number)]
	primes = [number for number in range(1, limit) if is_prime(number)]

	factors_dict = list_to_dict(primes)
	
	for number in non_primes:
		number_dict = prime_factors_dict(number)
		
		for key, value in number_dict.items():
			if value > factors_dict[key]:
				factors_dict[key] = value

	factors = dict_to_list(factors_dict)
	print(factors)

	product = reduce((lambda x, y: x*y), factors)
	print(product)

if __name__ == '__main__':
	main()