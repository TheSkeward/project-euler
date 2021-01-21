"""Project Euler problem 19"""


def calculate():
    """Returns the number of Sundays that fell on the
    first of the month during the twentieth century"""
    reg_months = (31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)
    leap_months = (31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)
    years = range(1900, 2001)
    acc = 0
    day_counter = 0
    for year in years:
        months = (
            leap_months
            if year % 4 == 0 and year % 100 != 0 or year % 400 == 0
            else reg_months
        )
        for month in months:
            for day in range(month):
                if day == 0 and year != 1900 and day_counter % 7 == 6:
                    acc += 1
                day_counter += 1
    return acc


if __name__ == "__main__":
    print(calculate())

str.join()