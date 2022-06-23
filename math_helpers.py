from functools import reduce
import math

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