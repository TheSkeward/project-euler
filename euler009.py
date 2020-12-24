"""Project Euler problem 9"""


def calculate(abc_sum):
    """Finds a Pythagorean triplet for which a + b + c == abc_sum and returns the product a*b*c"""
    for a in range(1, abc_sum):
        if a > abc_sum:
            break
        for b in range(1, abc_sum):
            if a + b > abc_sum:
                break
            for c in range(1, abc_sum):
                if a + b + c > abc_sum:
                    break
                if a + b + c == abc_sum and a ** 2 + b ** 2 == c ** 2:
                    return a * b * c


print(calculate(1000))
