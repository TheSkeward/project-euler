"""Project Euler problem 10"""


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


def calculate(below):
    """Returns the sum of the primes below the specified number"""
    primes = []
    for potential in range(below):
        if is_prime(potential):
            primes.append(potential)
    answer = sum(primes)
    return answer


print(calculate(2000000))
