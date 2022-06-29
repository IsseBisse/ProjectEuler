def distinct_powers(a_range, b_range):
	powers = list()
	for a in a_range:
		for b in b_range:
			powers.append(a**b)

	return set(powers)

if __name__ == '__main__':
	a_range = b_range = range(2, 101)
	print(len(distinct_powers(a_range, b_range)))