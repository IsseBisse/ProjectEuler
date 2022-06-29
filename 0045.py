from math_helpers import pq_formula

def triangular(n):
	return int(n*(n+1)/2)

def is_pentagonal(number):
	n = pq_formula(-1/3, -2/3*number)
	if n is None:
		return False

	if n[0] <= 1 or not n[0].is_integer():
		return False

	return True

def is_hexagonal(number):
	n = pq_formula(-1/2, -1/2*number)
	if n is None:
		return False

	if n[0] <= 1 or not n[0].is_integer():
		return False

	return True

def main():
	n = 285
	while True:
		n += 1
		number = triangular(n)

		if is_pentagonal(number) and is_hexagonal(number):
			break

	print(n, number)

if __name__ == '__main__':
	main()