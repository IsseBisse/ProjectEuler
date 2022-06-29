from itertools import permutations

from math_helpers import num_to_digits, digits_to_num

def get_all_pandigital():
    pandigital = list()
    digits = list(range(10))
    for perm in permutations(digits):
        pandigital.append(digits_to_num(perm))

    return pandigital

def is_substring_divisible(pandigital_number):
	digits = num_to_digits(pandigital_number)

	divisors = [2, 3, 5, 7, 11, 13, 17]
	for i, div in enumerate(divisors):
		sub_number = digits_to_num(digits[i+1:i+4])
		if sub_number % div != 0:
			return False

	return True

def main():
	substring_numbers = list()
	for number in get_all_pandigital():
		if is_substring_divisible(number):
			substring_numbers.append(number)
	
	print(sum(substring_numbers))

if __name__ == '__main__':
	main()