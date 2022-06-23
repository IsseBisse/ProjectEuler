from itertools import permutations

numbers = range(10)
perms = permutations(numbers, len(numbers))
print("".join([str(digit) for digit in list(perms)[1000000-1]]))