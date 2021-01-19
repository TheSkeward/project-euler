"""Project Euler problem 21"""


def div(num):
    """Returns the sum of proper divisors of num"""
    acc = 0
    for i in range(1, num):
        if num % i == 0:
            acc += i
    return acc


def calculate(num):
    """Returns the sum of all numbers a and b under num
    such that div(a) == b and div(b) == a and a != b."""
    divisor_sum = [0] * num
    for i, val in enumerate(divisor_sum):
        divisor_sum[i] = div(i)
    acc = 0
    counted = []
    for i, val in enumerate(divisor_sum):
        try:
            if all(
                [
                    i not in counted,  # not already counted
                    i != val,  # a != b
                    i == divisor_sum[val],  # div(a) == b
                    val == divisor_sum[i],  # div(b) == a
                ]
            ):
                counted.append(val)
                acc += i + val
        except IndexError:
            pass
    return acc


if __name__ == "__main__":
    print(calculate(10000))
