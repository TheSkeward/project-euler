"""Project Euler problem 23"""


def calculate(limit):
    """Returns the sum of all positive integers which cannot
    be written as the sum of two abundant numbers up to limit"""
    sum_of_divisors = [0] * limit
    for i in range(1, limit):
        for j in range(i * 2, limit, i):
            sum_of_divisors[j] += i
    abundant = [i for (i, x) in enumerate(sum_of_divisors) if x > i]
    sum_of_abundant = set()
    for num in abundant:
        for num_2 in abundant:
            sum_of_abundant.add(num + num_2)
    return sum(set(range(1, limit)) - sum_of_abundant)


if __name__ == "__main__":
    print(calculate(28124))
