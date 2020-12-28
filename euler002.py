"""Project Euler problem 2"""


def calculate(not_to_exceed):
    """Returns the sum of the even-valued terms in the Fibonacci sequence
    whose values do not exceed the given number"""
    term_one = 1
    term_two = 2
    total = 0
    while term_two < not_to_exceed:
        if not term_two % 2:
            total += term_two
        next_term = term_one + term_two
        term_one = term_two
        term_two = next_term
    return total


print(calculate(4000000))
