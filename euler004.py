"""Project Euler problem 4"""


def calculate(digits):
    """Finds the largest palindrome made from the
    product of two numbers that have the number of digits specified"""
    answer = max(
        number * number_2
        for number in range(10 ** digits - 1, 10 ** digits // 10 - 1, -1)
        for number_2 in range(10 ** digits - 1, 10 ** digits // 10 - 1, -1)
        if str(number * number_2) == str((number * number_2))[::-1]
    )
    return answer


if __name__ == "__main__":
    print(calculate(3))
