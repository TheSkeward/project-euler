"""Project Euler problem 1"""


def calculate(below):
    """Returns the sum of all the multiples of 3 or 5 below the specified number"""
    answer = sum(x for x in range(below) if (x % 3 == 0 or x % 5 == 0))
    answer = str(answer)
    return answer


if __name__ == "__main__":
    print(calculate(1000))
