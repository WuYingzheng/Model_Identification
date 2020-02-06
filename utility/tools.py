def prime_factors(n):
    """
    Returns all the prime factors of a positive integer
    求正因数，正约数
    12 =>> 2, 2, 3
    """
    factors = []
    d = 2
    while n > 1:
        while n % d == 0:
            factors.append(d)
            n /= d
        d += 1
        if d*d > n:
            if n > 1:
                factors.append(n)
            break
    return factors

if __name__ == '__main__':
    f = prime_factors(12)
    print(f)