def get_input():
	with open("0013.txt") as file:
		text = file.read()

	numbers = [int(row) for row in text.split("\n")]
	return numbers



if __name__ == '__main__':
	numbers = get_input()
	print(numbers)
	print(str(sum(numbers))[:10])