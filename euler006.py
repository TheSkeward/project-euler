"""Project Euler problem 6"""


def calculate(nth_number):
    """Returns the difference between the sum of the squares and the
    square of the sum of the specified number of the first natural numbers"""
    sums = sum(number for number in range(1, nth_number + 1))
    sum_of_squares = 0
    for number in range(1, nth_number + 1):
        sum_of_squares += number ** 2
    answer = sums ** 2 - sum_of_squares
    return answer


print(calculate(100))
