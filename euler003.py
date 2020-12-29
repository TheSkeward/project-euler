"""Project Euler problem 3"""


def sqrt(number):
    """Returns the square root of the specified number as an int, rounded down"""
    count = 0
    while count ** 2 < number:
        count += 1
    return count - 1


def calculate(answer):
    """Returns the largest prime factor of the specified number"""
    count = 2
    while count < sqrt(answer):
        if answer % count == 0:
            answer //= count
        else:
            count += 1
    return answer


print(calculate(600851475143))
