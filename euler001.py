"""Project Euler problem 1"""


def calculate(below):
    answer = 0
    for number in range(below):
        if not (number % 3 and number % 5):
            answer += number
    return answer


print(calculate(1000))
