"""Project Euler problem 17"""


def letter_count(num):
    """Returns the number of letters in the specified number"""
    assert 0 < num <= 1000
    num = str(num)
    acc = 0
    if len(num) > 3:
        acc += len("one thousand".replace(" ", ""))
        num = "0"
    if len(num) > 2:
        acc += (
            len("hundred and".replace(" ", "")) if int(num[-2:]) > 0 else len("hundred")
        )
        acc += (
            3
            if num[0] in ["1", "2", "6"]
            else 4
            if num[0] in ["4", "5", "9"]
            else 5
            if num[0] in ["3", "7", "8"]
            else 0
        )
        num = str(int(num[-2:]))
    if int(num) > 12:
        acc += len("ty") if int(num) > 19 else len("teen")
        num = num if int(num) > 19 or int(num) == 14 else num[-1:]
        acc += (
            3
            if num[0] in ["4", "5", "6"]
            else 4
            if num[0] in ["2", "3", "8", "9"]
            else 5
            if num[0] == "7"
            else 0
        )
        num = num[-1:] if int(num) > 19 or int(num) == 14 else "0"
    acc += (
        3
        if num in ["1", "2", "6", "10"]
        else 4
        if num in ["4", "5", "9"]
        else 5
        if num in ["3", "7", "8"]
        else 6
        if num in ["11", "12"]
        else 0
    )
    return acc


def calculate(up_to):
    """Returns the count of letters that would be used if all the numbers
    from one to the specified number inclusive were written out in words"""
    answer = sum(letter_count(n) for n in range(1, up_to + 1))
    return answer


if __name__ == "__main__":
    print(calculate(1000))
