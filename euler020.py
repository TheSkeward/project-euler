"""Project Euler problem 20"""


def calculate(number):
    """Returns the sum of the digits in the factorial of the specified number"""
    factorial = 1
    for permutation in range(1, number + 1):
        factorial *= permutation
    answer = sum(list(map(int, str(factorial))))
    return answer


if __name__ == "__main__":
    print(calculate(100))
