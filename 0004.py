def is_palindrome(number):
	return str(number) == str(number)[::-1]

def find_largest_palindrome(num_digits):
	largest_palindrome = 0
	for num1 in range(10**num_digits):
		for num2 in range(10**num_digits):
			product = num1*num2
			if product > largest_palindrome and is_palindrome(product):
				largest_palindrome = product

	return largest_palindrome


def main():
	print(find_largest_palindrome(3))

if __name__ == '__main__':
	main()