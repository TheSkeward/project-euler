"""Project Euler problem 25"""


def calculate(digits):
    """Returns the index of the first term in the Fibonacci
    sequence to contain the specified number of digits."""
    answer = 0
    prev = 1
    cur = 1
    while len(str(prev)) < digits:
        answer += 1
        next_term = prev + cur
        prev = cur
        cur = next_term
    answer += 1
    return answer


if __name__ == "__main__":
    print(calculate(1000))
