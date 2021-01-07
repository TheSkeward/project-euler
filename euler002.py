"""Project Euler problem 2"""


def calculate(not_to_exceed):
    """Returns the sum of the even-valued terms in the Fibonacci sequence
    whose values do not exceed the specified number"""
    answer = 0
    term_one = 1
    term_two = 2
    while term_two < not_to_exceed:
        if not term_two % 2:
            answer += term_two
        next_term = term_one + term_two
        term_one = term_two
        term_two = next_term
    return answer


if __name__ == "__main__":
    print(calculate(4000000))
