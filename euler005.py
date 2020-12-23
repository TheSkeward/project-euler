"""Project Euler problem 5"""
from collections import Counter


def get_prime_factors(number):
    count = 2
    factors = []
    while count ** 2 <= number:
        if number % count == 0:
            factors.append(count)
            number //= count
        else:
            count += 1
    factors.append(number)
    return [1] + factors


NUMBER = 20
FACTORS_BY_NUMBER = []
for divisor in range(2, NUMBER + 1):
    FACTORS_BY_NUMBER.append(Counter(get_prime_factors(divisor)))
ALL_FACTORS = {}
for counter in FACTORS_BY_NUMBER:
    for key in counter:
        if key not in ALL_FACTORS or ALL_FACTORS[key] < counter[key]:
            ALL_FACTORS[key] = counter[key]
SMALLEST_MULTIPLE = 1
for key, value in ALL_FACTORS.items():
    SMALLEST_MULTIPLE *= key ** value
print(SMALLEST_MULTIPLE)