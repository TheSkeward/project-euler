"""Project Euler problem 22"""


def calculate(name_list):
    """Returns the sum of the alphabetical value for each name
    in the list multiplied by its position in the list"""
    return sum(
        (i + 1) * (ord(c) - ord("A") + 1)
        for i, name in enumerate(sorted(name_list))
        for c in name.strip('"')
    )


with open("p022_names.txt") as f:
    NAMES = f.read().split(",")

if __name__ == "__main__":
    print(calculate(NAMES))
