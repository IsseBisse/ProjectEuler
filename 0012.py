import math

def triangle_number(n):
    return sum(range(n+1))
# def triangle_number(n):
#     if n < 0:
#         return 0
#     elif n == 1:
#         return 1

#     else:
#         return n + triangle_number(n-1)

def divisors(number):
    """Naive"""
    divisors = list()
    for div in range(1, int(math.sqrt(number))+1):
    # for div in range(2, number):
        if number%div == 0:
            divisors.append(div)
            divisors.append(number//div)

    return divisors

def main():
    n = 1
    while len(divisors(triangle_number(n))) <= 500:
        n += 1

    print(triangle_number(n))

if __name__ == '__main__':
    main()