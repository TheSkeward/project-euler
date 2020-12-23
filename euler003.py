"""Project Euler problem 3"""
NUMBER = 600851475143
COUNT = 2
while COUNT ** 2 < NUMBER:
    if NUMBER % COUNT == 0:
        NUMBER //= COUNT
    else:
        COUNT += 1
print(NUMBER)
