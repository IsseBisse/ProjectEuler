from math_helpers import num_to_digits
from prime_helpers import primes_below

PRIMES = [prime for prime in primes_below(10000) if prime >= 1000]

def has_special_adder(number):
    max_add = (9999 - number) // 2
    for add in range(1, max_add+1):
        if is_special(number, add):
            return add

    return None

def is_special(number, add):
    number_digits = sorted(num_to_digits(number))
    next_number = number
    for _ in range(2):
        next_number += add

        if sorted(num_to_digits(next_number)) != number_digits:
            return False

        if next_number not in PRIMES:
            return False

    return True

def main():
    print(is_special(1013, 18))

    for number in PRIMES:
        special_adder = has_special_adder(number)
        if special_adder is not None:
            print(number, number+special_adder, number+2*special_adder)



if __name__ == '__main__':
    main()