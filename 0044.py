from math import sqrt

def pentagonal(n):
	return int(n*(3*n-1)/2)

def pq_formula(p, q):
	under_sqrt = (p/2)**2 - q
	if under_sqrt < 0:
		return None

	n = (-p/2+sqrt(under_sqrt), -p/2-sqrt(under_sqrt))
	return n

def is_pentagonal(number):
	return number in pentagonal_numbers
	n = pq_formula(-1/3, -2/3*number)

	print(n)
	if n is None:
		return False

	if n[0] < 1 or not n[0].is_integer():
		return False

	return True

def sum_difference_pentagonal(p1, p2, pentagonal_inverse):
	diff = abs(p1 - p2)
	if diff not in pentagonal_inverse:
		return False

	if sum([p1, p2]) not in pentagonal_inverse:
		return False

	return True

def main():
	pentagonal_numbers = list()
	pentagonal_inverse = dict()

	done = False

	n = 0
	while not done:
		n += 1
		p1 = pentagonal(n)

		pentagonal_numbers.append(p1)
		pentagonal_inverse[p1] = n

		for p2 in pentagonal_numbers:
			if sum_difference_pentagonal(p1, p2, pentagonal_inverse):
				print(p1, p2)
				break

if __name__ == '__main__':
	main()

	# print(7042750 - 1560090)