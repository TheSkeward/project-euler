"""Project Euler problem 5"""
from collections import Counter
import fractions


def calculate(end_number):
    """Returns the smallest positive number that is evenly divisible
    by all of the numbers from 1 to the specified number"""
    factors_by_number = []
    for divisor in range(2, end_number + 1):
        count = 2
        factors = []
        while count ** 2 <= divisor:
            if divisor % count == 0:
                factors.append(count)
                divisor = fractions.Fraction(divisor, count)
            else:
                count += 1
        factors.append(divisor)
        factors_by_number.append(Counter(factors))
    all_factors = {}
    for counter in factors_by_number:
        for key in counter:
            if key not in all_factors or all_factors[key] < counter[key]:
                all_factors[key] = counter[key]
    answer = 1
    for key, value in all_factors.items():
        answer *= key ** value
    return answer


print(calculate(20))
