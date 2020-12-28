"""Project Euler problem 1"""


def calculate(below):
    """Returns the sum of all the multiples of 3 or 5 below the given number"""
    answer = 0
    for number in range(below):
        if not (number % 3 and number % 5):
            answer += number
    return answer


print(calculate(1000))
