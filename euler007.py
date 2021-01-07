"""Project Euler problem 7"""


def is_prime(number):
    """Returns True if the specified number is prime"""
    if number <= 1:
        return False
    count = 2
    while count ** 2 <= number:
        if number % count == 0:
            return False
        count += 1
    return True


def calculate(last_prime):
    """Returns the last_prime-th prime"""
    primes = []
    count = 0
    while len(primes) < last_prime:
        match = False
        if is_prime(count):
            for prime in primes:
                if count % prime == 0:
                    match = True
                    break
            if not match:
                primes.append(count)
        count += 1
    answer = primes[-1]
    return answer


if __name__ == "__main__":
    print(calculate(10001))
