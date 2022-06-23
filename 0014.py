def next_number(number):
	if number % 2 == 0:
		return number // 2

	else:
		return 3 * number + 1

class Collatz:
	def __init__(self):
		self.cache = dict()

	def cached_get_chain_length(self, start_number):
		number = start_number
		length = 1

		while number != 1:
			if number in self.cache:
				return length + self.cache[number]

			number = next_number(number)
			length += 1


		self.cache[start_number] = length

		return length 

	def cached_recursive_get_chain_length(self, number):
		if number == 1:
			return 1

		elif number in self.cache:
			return self.cache[number] 

		else:
			length = self.cached_recursive_get_chain_length(next_number(number)) + 1
			self.cache[number] = length
			return length

def get_chain_length(start_number):
	number = start_number
	length = 1

	while number != 1:
		number = next_number(number)
		length += 1

	return length 

def main():
	max_length = 0
	max_length_number = 0

	collatzer = Collatz()
	for start_number in range(1,1000001):
		# length = get_chain_length(start_number)
		length = collatzer.cached_recursive_get_chain_length(start_number)

		# assert length == old_length
		
		if length > max_length:
			max_length = length
			max_length_number = start_number

	print(max_length_number, max_length)

if __name__ == '__main__':
	main()