"""Project Euler problem 16"""


def calculate(power):
    """Returns the sum of the digits of the number 2 to the power of the specified number"""
    answer = sum(list(map(int, str((2 ** power)))))
    return answer


print(calculate(1000))
