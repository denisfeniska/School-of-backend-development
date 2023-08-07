def prime_generator():
    yield 2
    primes = [2]
    n = 3
    while True:
        is_prime = True
        for p in primes:
            if p * p > n:
                break
            if n % p == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(n)
            yield n
        n += 2


# Example usage:
gen = prime_generator()
for _ in range(10):
    print(next(gen))
