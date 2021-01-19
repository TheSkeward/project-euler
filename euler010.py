"""Project Euler problem 10"""


def is_prime(num):
    """Returns True if num is prime"""
    if num <= 1:
        return False
    if num <= 3:
        return True
    count = 2
    while count ** 2 <= num:
        if num % count == 0:
            return False
        count += 1
    return True


def calculate(below):
    """Returns the sum of the primes below the specified number"""
    primes = []
    for potential in range(below):
        if is_prime(potential):
            primes.append(potential)
    answer = sum(primes)
    return answer


if __name__ == "__main__":
    print(calculate(2000000))
