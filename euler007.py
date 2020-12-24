"""Project Euler problem 7"""


def calculate(last_prime):
    """finds the last_primeth number"""
    primes = []
    count = 2
    while len(primes) < last_prime:
        match = False
        for prime in primes:
            if count % prime == 0:
                match = True
                break
        if not match:
            primes.append(count)
        count += 1
    return primes[-1]


print(calculate(10001))
