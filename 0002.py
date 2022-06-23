def generate_fib(limit):
	sequence = [1, 2]
	
	number = sequence[-1] + sequence[-2]
	while number <= limit:
		sequence.append(number)

		number = sequence[-1] + sequence[-2]

	even_sequence = [number for number in sequence if number%2==0]

	print(even_sequence)
	print(sum(even_sequence))

def main():
	generate_fib(4e6)

if __name__ == '__main__':
	main()