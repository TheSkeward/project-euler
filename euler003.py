"""Project Euler problem 3"""


def sqrt(number):
    """Returns the square root of the specified number as an int, rounded down"""
    assert number >= 0
    offset = 1
    while offset ** 2 <= number:
        offset *= 2
    count = 0
    while offset > 0:
        if (count + offset) ** 2 <= number:
            count += offset
        offset //= 2
    return count


def smallest_prime_factor(number):
    """Returns the smallest prime factor of the specified number"""
    assert number >= 2
    for potential in range(2, sqrt(number) + 1):
        if number % potential == 0:
            return potential
    return number


def calculate(number):
    """Returns the largest prime factor of the specified number"""
    while True:
        smallest = smallest_prime_factor(number)
        if number > smallest:
            number //= smallest
        else:
            answer = number
            return answer


if __name__ == "__main__":
    print(calculate(600851475143))
