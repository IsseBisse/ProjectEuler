from math import sqrt, ceil

def main():
	max_value = 1000
	for a in range(1, max_value):
		for b in range(1, max_value):
			c = sqrt(a**2 + b**2)
			# print(c)

			if c.is_integer() and a + b + c == 1000:
				c = int(c)
				print(a, b, c)
				print(a*b*c)
				return

if __name__ == '__main__':
	main()