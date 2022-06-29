def main():
	limit = 1e6
	decimals = ""
	number = 1
	while len(decimals) < limit:
		decimals += str(number)
		number += 1

	prod = 1
	for exp in range(7):
		idx = 10**exp
		prod *= int(decimals[idx-1])

	print(prod)

if __name__ == '__main__':
	main()