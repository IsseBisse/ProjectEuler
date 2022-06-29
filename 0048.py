from math_helpers import num_to_digits

def array_add(array1, array2):
	new_array = list()

	len1 = len(array1)
	len2 = len(array2)
	carry = 0
	for i in range(max(len1, len2)):
		num1 = array1[-(i+1)] if i < len1 else 0
		num2 = array2[-(i+1)] if i < len2 else 0


		result = num_to_digits(num1 + num2 + carry)
		new_array.append(result[-1])

		if len(result) > 1:
			carry = result[0]
		else:
			carry = 0

	if carry == 1 and len(new_array) < 10:
		new_array.append(carry)

	return new_array[::-1]

def array_mult(array, multiplier):
	new_array = array.copy()
	for _ in range(multiplier-1):
		new_array = array_add(new_array, array)
		# print(new_array)

	return new_array
	# carry = 0
	# new_array = list()
	# for i, num in enumerate(reversed(array)):
	# 	result = num_to_digits(num * multiplier + carry)
	# 	new_array.append(result[-1])

	# 	if len(result) > 1:
	# 		carry = result[0]
	# 	else:
	# 		carry = 0
		
	# if carry != 0 and len(new_array) < 10:
	# 	new_array.append(carry)

	# return new_array[::-1]

# This is slooow (>2 minutes)
# def main():
# 	sum_array = [0] * 10
# 	for number in range(1, 200):
# 		array_number = num_to_digits(number)
# 		for _ in range(number-1):
# 			array_number = array_mult(array_number, number)
		
# 		# print(number, str(number**number)[-10:], "".join([str(num) for num in array_number]))

# 		sum_array = array_add(sum_array, array_number)[-10:]

# 	print("".join([str(num) for num in sum_array]))

def snipper(length):
	def snip(number):
		if len(str(number)) > length:
			number = int(str(number)[-length:]) 

		return number

	return snip

def main():
	ten_snipper = snipper(10)
	total = 0
	for number in range(1, 1001):
		powered_number = number
		for _ in range(number-1):
			powered_number *= number

			powered_number = ten_snipper(powered_number)

		total += powered_number
		total = ten_snipper(total)



	print(total)


if __name__ == '__main__':
	main()