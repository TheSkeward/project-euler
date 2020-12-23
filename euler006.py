"""Project Euler problem 6"""
ANSWER = 0
SUM = 0
SUM_OF_SQUARES = 0
for number in range(1, 101):
    SUM += number
    SUM_OF_SQUARES += number ** 2
ANSWER = SUM ** 2 - SUM_OF_SQUARES
print(ANSWER)
