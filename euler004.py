"""Project Euler problem 4"""


def calculate():
    """Finds the largest palindrome made from the product of two 3-digit numbers"""
    answer = 0
    for number in range(999, 99, -1):
        for number_2 in range(999, 99, -1):
            if (
                number * number_2 > answer
                and str(number * number_2) == str((number * number_2))[::-1]
            ):
                answer = number * number_2
    return answer


print(calculate())
