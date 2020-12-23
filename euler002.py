"""Project Euler problem 2"""
TERM_1 = 1
TERM_2 = 2
SUM = 0
while TERM_2 < 4000000:
    if not TERM_2 % 2:
        SUM += TERM_2
    NEXT_TERM = TERM_1 + TERM_2
    TERM_1 = TERM_2
    TERM_2 = NEXT_TERM
print(SUM)
