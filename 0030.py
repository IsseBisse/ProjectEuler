def sum_of_powered_digits(number, power):
	return sum([int(digit)**power for digit in str(number)])

def main():
	power = 5
	
	limit = 9
	while limit < sum_of_powered_digits(limit, 5):
		limit = int(str(limit) + "9")

	equals_sum_of_digits = list()
	for num in range(2, limit):
		if num == sum_of_powered_digits(num, power):
			equals_sum_of_digits.append(num)

	print(equals_sum_of_digits)
	print(sum(equals_sum_of_digits))

if __name__ == '__main__':
	main()