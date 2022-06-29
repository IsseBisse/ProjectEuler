from math import factorial

def sum_of_factorials(number):
	return sum([factorial(int(char)) for char in str(number)])

def main():
	limit = 9
	while limit < sum_of_factorials(limit):
		limit = int(str(limit) + "9")
	
	equals_sum_of_factorials = list()
	for number in range(limit):
		if number == sum_of_factorials(number):
			equals_sum_of_factorials.append(number)

	equals_sum_of_factorials.remove(1)
	equals_sum_of_factorials.remove(2)
	print(equals_sum_of_factorials)
	print(sum(equals_sum_of_factorials))

if __name__ == '__main__':
	main()