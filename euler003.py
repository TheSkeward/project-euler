"""Project Euler problem 3"""


def calculate(number):
    """Returns the largest prime factor of the given number"""
    count = 2
    while count ** 2 < number:
        if number % count == 0:
            number //= count
        else:
            count += 1
    return number


print(calculate(600851475143))
