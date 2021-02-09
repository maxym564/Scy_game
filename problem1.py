def read_input(path: str):
    """
    Read game board file from path.
    Return list of str.

    >>> read_input("check.txt")
    ['***21**', '452453*', '423145*', '*543215', '*35214*', '*41532*', '*2*1***']
    """
    total = []
    with open(path) as table:
        for line in table:
            line = line.strip()
            total.append(line)
    return total


def left_to_right_check(input_line: str, pivot: int):
    """
    Check row-wise visibility from left to right.
    Return True if number of building from the left-most hint is visible looking to the right,
    False otherwise.

    input_line - representing board row.
    pivot - number on the left-most hint of the input_line.

    >>> left_to_right_check("412453*", 4)
    True
    >>> left_to_right_check("452453*", 5)
    False
    """
    input_line = input_line[1:]
    max_num = input_line[0]
    correct_nums = 1
    index = 1
    while index != len(input_line) - 1:
        if input_line[index] > max_num:
            max_num = input_line[index]
            correct_nums += 1
        index += 1
    if correct_nums == pivot:
        return True
    return False


