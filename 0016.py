def sum_digits(number):
	return sum([int(c) for c in str(number)])

def main():
	for i in range(32):
		number = 2**i
		print(number, sum_digits(number))

if __name__ == '__main__':
	main()

	print(sum_digits(2**1000))