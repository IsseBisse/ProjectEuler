def is_palindrome(string):
	return string == string[::-1]

def is_double_palindrome(number):
	number_string = str(number)
	if not is_palindrome(number_string):
		return False
	
	binary_string = f"{number:b}"
	return is_palindrome(binary_string)

def main():
	double_palindromes = list()

	for number in range(int(1e6)):
		if is_double_palindrome(number):
			double_palindromes.append(number)
		
	print(double_palindromes)
	print(sum(double_palindromes))

if __name__ == '__main__':
	main()