def prime_factors(n):
    i = 2
    factors = []
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    return factors

def main():
    num_factors = 4
    num_consequtive = 0
    
    number = 1
    while num_consequtive < 4:
        factors = prime_factors(number)
        if len(set(factors)) == num_factors:
            num_consequtive += 1
        else:
            num_consequtive = 0

        number += 1

    for _ in range(4):
        number -= 1        
        print(number, prime_factors(number))
    
if __name__ == '__main__':
    main()