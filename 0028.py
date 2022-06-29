def spiral_numbers(size):
	numbers = [1]
	current = 1

	for step in range(1, size, 2):
		for _ in range(4):
			current += step + 1
			numbers.append(current)
	
	return numbers

if __name__ == '__main__':
	numbers = spiral_numbers(1001)
	print(sum(numbers))