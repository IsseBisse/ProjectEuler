def get_words():
	with open("0042.txt") as file:
		text = file.read()

	words = text.replace("\"","").lower().split(",")
	return words

def get_triangle_numbers(n_max):
	triangle_numbers = list()
	for n in range(n_max):
		number = int(0.5*n*(n+1))
		triangle_numbers.append(number)

	return triangle_numbers

def word_sum(word):
	char_values = [ord(char)-ord("a")+1 for char in word]
	return sum(char_values)

def main():
	words = get_words()
	max_word_length = max([len(word) for word in words])
	max_word_sum = (ord("z") - ord("a") + 1) * max_word_length

	# Since maximum triangle number is roughly n**2 this gives a WIDE margin
	triangle_numbers = get_triangle_numbers(max_word_sum)

	num_triangle_words = 0
	for word in words:
		if word_sum(word) in triangle_numbers:
			num_triangle_words += 1

	print(num_triangle_words)

if __name__ == '__main__':
	main()