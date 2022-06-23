def main():
	factors = [3, 5]
	limit = 1000

	multiples = list()
	for number in range(1, limit):
		if any([number % factor == 0 for factor in factors]):
			multiples.append(number)

	print(multiples)
	print(sum(multiples))

if __name__ == '__main__':
	main()