"""Project Euler problem 9"""


def calculate(perimeter):
    """Returns the product a*b*c of a Pythagorean triplet for which a + b + c == perimeter"""
    for a in range(1, perimeter):
        if a > perimeter:
            break
        for b in range(1, perimeter):
            if a + b > perimeter:
                break
            for c in range(1, perimeter):
                if a + b + c > perimeter:
                    break
                if a + b + c == perimeter and a ** 2 + b ** 2 == c ** 2:
                    answer = a * b * c
                    return answer


if __name__ == "__main__":
    print(calculate(1000))
