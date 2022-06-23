
def hundreds_to_word(digit):
	return SINGLES_TO_WORD[digit] + " hundred"

def tens_to_word(ten, single):
	if ten < 2:
		return SINGLES_TO_WORD[int(str(ten)+str(single))]

	else:
		return f"{TENS_TO_WORD[ten]}-{SINGLES_TO_WORD[single]}"

TENS_TO_WORD = {2: "twenty",
	3: "thirty",
	4: "forty",
	5: "fifty",
	6: "sixty",
	7: "seventy",
	8: "eighty",
	9: "ninety",}


SINGLES_TO_WORD = {0: "",
	1: "one",
	2: "two",
	3: "three",
	4: "four",
	5: "five",
	6: "six",
	7: "seven",
	8: "eight",
	9: "nine",
	10: "ten",
	11: "eleven",
	12: "twelve",
	13: "thirteen",
	14: "fourteen",
	15: "fifteen",
	16: "sixteen",
	17: "seventeen",
	18: "eighteen",
	19: "nineteen",}

def number_to_word(number):
	"""number in [0, 1000]"""
	if number == 1000:
		return "one thousand"

	digits = [int(c) for c in str(number)]

	word = ""
	if len(digits) > 2:
		word += f"{hundreds_to_word(digits[-3])} "

		if not (digits[-2] == 0 and digits[-1] == 0):
			word += "and " 
	
	if len(digits) == 1:
		word += f"{tens_to_word(0, digits[-1])} "
	
	else:
		word += f"{tens_to_word(digits[-2], digits[-1])} "

	print(number, word)
	return word


def main():
	string = ""
	for digit in range(1, 1001):
		string += number_to_word(digit)

	string = string.replace(" ", "")
	string = string.replace("-", "")

	assert len(number_to_word(115).replace(" ", "").replace("-", "")) == 20
	assert len(number_to_word(342).replace(" ", "").replace("-", "")) == 23

	print(len(string))

if __name__ == '__main__':
	main()