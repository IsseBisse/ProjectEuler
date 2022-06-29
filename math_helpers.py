from functools import reduce
import math

def num_to_digits(number):
    return [int(c) for c in str(number)]

def digits_to_num(digits):
    return int("".join(map(str, digits)))

def list_prod(list_):
	return reduce((lambda x, y: x*y), list_)

def divisors(number):
    """Naive"""
    divisors = list()
    for div in range(1, int(math.sqrt(number))+1):
    # for div in range(2, number):
        if number%div == 0:
            divisors.append(div)
            divisors.append(number//div)

    return divisors

def is_pandigital_num(number):
    digits = num_to_digits(number)
    return is_pandigital(digits, len(digits))

def is_pandigital(digits, n):
    if len(digits) != n:
        return False

    if sorted(digits) != list(range(1,n+1)):
        return False

    return True

def pq_formula(p, q):
    under_sqrt = (p/2)**2 - q
    if under_sqrt < 0:
        return None

    n = (-p/2+math.sqrt(under_sqrt), -p/2-math.sqrt(under_sqrt))
    return n