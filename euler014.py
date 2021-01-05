"""Project Euler problem 14"""


def calculate(under):
    """Returns the starting number under the specified
    number that produces the longest Collatz sequence"""
    answer = 0
    current_best = 0
    for starting in range(1, under + 1):
        term = starting
        count = 1
        while term != 1:
            count += 1
            if term % 2 == 0:
                term //= 2
            else:
                term = term * 3 + 1
        if count > current_best:
            current_best = count
            answer = starting
    return answer


print(calculate(1000000))
