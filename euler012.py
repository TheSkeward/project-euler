"""Project Euler problem 12"""
from euler003 import sqrt


def num_divisors(number):
    """Returns the number of divisors of the specified number"""
    end = sqrt(number)
    result = sum(2 for i in range(1, end + 1) if number % i == 0)
    return result


def calculate(over):
    """Returns the value of the first triangle number to have
    over the specified number of divisors"""
    triangle = 0
    count = sum(range(triangle))
    while True:
        if num_divisors(count) > over:
            answer = count
            return answer
        triangle += 1
        count = sum(range(triangle))


if __name__ == "__main__":
    print(calculate(500))
