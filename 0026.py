import re

def is_reccuring(denominator):
	while denominator % 2 == 0:
		denominator //= 2

	while denominator % 5 == 0:
		denominator //= 5
		
	if denominator == 1:
		return False

	else:
		return True

def find_reccuring_cycle(denominator):
	print(re.findall(r"\S*(\S+)\1\S*", f"{int(1e12)/denominator:.15f}"))
	return int(int(1e40)/denominator)

def main():
	for denominator in range(1, 20):
		if is_reccuring(denominator):
			print(denominator, find_reccuring_cycle(denominator))

if __name__ == '__main__':
	main()