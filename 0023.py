from itertools import permutations
from math import ceil, sqrt

from math_helpers import divisors

def is_abundant(number):
	div = divisors(number)
	div.remove(number)
	return sum(set(div)) > number

def sum_pair_exists(number, sorted_abundant_numbers):
	for ab_num in sorted_abundant_numbers:
		if ab_num >= number:
			return False

		if is_abundant(number - ab_num):
			return True

	return False

def main():
	limit = 28123
	# limit = 8000
	abundant_numbers = list()
	for number in range(1, (limit + 1)//2):
		if is_abundant(number):
			abundant_numbers.append(number)
		
	abundant_numbers.sort()
	# print(len(abundant_numbers))

	no_pairs = list()
	for number in range(1, limit + 1):
		if not sum_pair_exists(number, abundant_numbers):
			no_pairs.append(number)

	print(sum(no_pairs))

if __name__ == '__main__':
	main()