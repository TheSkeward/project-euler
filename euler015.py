"""Project Euler problem 15"""
import math


def calculate(dimension):
    """Returns the number of routes from the top-left to the bottom-right of a n-dimension 2d grid"""
    return int((math.factorial(2 * dimension)) / ((math.factorial(dimension)) ** 2))


if __name__ == "__main__":
    print(calculate(20))
