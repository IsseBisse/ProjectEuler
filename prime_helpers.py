import math

def is_prime(number):
    # Naive
    if number == 1:
        return False

    for div in range(2, int(math.sqrt(number))+1):
    # for div in range(2, number):
        if number%div == 0:
            return False

    return True

def primes_below(n):
    """ Returns  a list of primes < n

    From: https://stackoverflow.com/questions/2068372/fastest-way-to-list-all-primes-below-n/3035188#3035188
    """
    sieve = [True] * (n//2)
    for i in range(3,int(n**0.5)+1,2):
        if sieve[i//2]:
            sieve[i*i//2::i] = [False] * ((n-i*i-1)//(2*i)+1)
    return [2] + [2*i+1 for i in range(1,n//2) if sieve[i]]