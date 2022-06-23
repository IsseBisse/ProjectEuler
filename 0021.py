from itertools import chain

from math_helpers import divisors

def main():
	divisor_sums = dict()

	amicable_numbers = list()
	for number in range(1, 10000):
		div_sum = sum(divisors(number)) - number
		divisor_sums[number] = div_sum

		if div_sum != number and \
			div_sum in divisor_sums and \
			divisor_sums[div_sum] == number:
			amicable_numbers.append((number, div_sum))

	print(amicable_numbers)
	print(sum(list(chain(*amicable_numbers))))

if __name__ == '__main__':
	main()