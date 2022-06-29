from prime_helpers import primes_below

# def is_reccuring(denominator):
# 	while denominator % 2 == 0:
# 		denominator //= 2

# 	while denominator % 5 == 0:
# 		denominator //= 5
		
# 	if denominator == 1:
# 		return False

# 	else:
# 		return True

# def high_precision_division(denominator, num_decimals):
# 	decimal_number_string = ""
# 	rem = 1
# 	for _ in range(num_decimals):
# 		decimal_number_string += str(rem // denominator)
# 		rem = 10 * (rem % denominator)

# 	return decimal_number_string

# def find_reccuring_cycle(decimal_number_string):
# 	longest_matching_substring = ""
# 	if len(decimal_number_string) % 2 != 0:
# 		decimal_number_string = decimal_number_string[1:] 

# 	for sub_start in range(0, len(decimal_number_string), 2):
# 		substring = decimal_number_string[sub_start:]
		
# 		halfway = len(substring) // 2
# 		# print(substring, find_reccuring_cycle(substring[:halfway]))

# 		if substring[:halfway] == substring[halfway:] and find_reccuring_cycle(substring[:halfway]) is None:
# 			return substring[:halfway]

# def main():
# 	base_num_decimals = 100
	
# 	max_cycle_length = 0
# 	for denominator in range(1, 1001):
# 		if is_reccuring(denominator):
# 			# print(f"Denominator: {denominator}")
# 			cycle = None
# 			num_decimals = base_num_decimals
# 			while cycle is None:
# 				decimal_number_string = high_precision_division(denominator, num_decimals)
# 				cycle = find_reccuring_cycle(decimal_number_string)
# 				num_decimals *= 2

# 			cycle_length = len(cycle)

# 			# print(denominator, len(cycle))

# 			if cycle_length > max_cycle_length:
# 				max_cycle_length = cycle_length
# 				max_denominator = denominator

# 	print(max_cycle_length, max_denominator)

def cycle_length(denominator):
	"""Works for primes >= 7"""
	numerator = 1

	numerator = numerator * 10 % denominator
	cycles = 1
	while numerator != 1:
		numerator = numerator * 10 % denominator
		cycles += 1

	return cycles

def main():
	primes = primes_below(1000)[3:]
	
	max_length = 0
	max_denominator = None
	for denominator in primes:
		length = cycle_length(denominator)

		print(denominator, length)

		if length > max_length:
			max_length = length
			max_denominator = denominator
		
	print(denominator, max_length)

if __name__ == '__main__':
	main()

