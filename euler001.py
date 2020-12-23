"""Project Euler problem 1"""
ANSWER = 0
for number in range(1000):
    if not (number % 3 and number % 5):
        ANSWER += number
print(ANSWER)
