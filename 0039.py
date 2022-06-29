from math import sqrt

# def is_right_angle(sides):
# 	sides.sort()
# 	return sides[0] ** 2 + sides[1] ** 2 == sides[2] ** 2

# too slow
# def num_right_angled_sides(p):
# 	right_angled_sides = list()
# 	for a in range(1, p-1):
# 		for b in range(1, p-a):
# 			c = p-(a+b)
# 			sides = [a,b,c]
# 			if is_right_angle(sides) and sides not in right_angled_sides:
# 				right_angled_sides.append(sides)

# 	return len(right_angled_sides)

def find_b_sides(a, p_limit):
	integer_right_angled = list()
	for b in range(1, a):
		c = sqrt(a**2 + b**2)
		if sum([a,b,c]) > p_limit:
			return integer_right_angled

		if c.is_integer():
			integer_right_angled.append((b,a,int(c)))

	return integer_right_angled

def integer_right_angled_triangles(p_limit):
	integer_right_angled = list()
	for a in range(1, p_limit):
		integer_right_angled += find_b_sides(a, p_limit)

	return integer_right_angled

def main():
	limit = 1001
	possible_integer_triangles = integer_right_angled_triangles(limit)

	p_dict = {p:0 for p in range(1, limit+1)}
	for triangle in possible_integer_triangles:
		p_dict[sum(triangle)] += 1
		print(triangle, sum(triangle))
	
	p_dict = [key for key, value in sorted(p_dict.items(), key=lambda item: item[1])]
	print(p_dict[-1])

if __name__ == '__main__':
	main()