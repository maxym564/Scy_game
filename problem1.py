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


def check_not_finished_board(board: list):
    """
    Check if skyscraper board is not finished, i.e., '?' present on the game board.

    Return True if finished, False otherwise.

    >>> check_not_finished_board(['***21**', '4?????*', '4?????*', '*?????5', '*?????*', '*?????*', '*2*1***'])
    False
    >>> check_not_finished_board(['***21**', '412453*', '423145*', '*543215', '*35214*', '*41532*', '*2*1***'])
    True
    >>> check_not_finished_board(['***21**', '412453*', '423145*', '*5?3215', '*35214*', '*41532*', '*2*1***'])
    False
    """
    for line in board:
        for el in line:
            if el == '?':
                return False
    return True


def check_uniqueness_in_rows(board: list):
    """
    Check buildings of unique height in each row.

    Return True if buildings in a row have unique length, False otherwise.

    >>> check_uniqueness_in_rows(['***21**', '412453*', '423145*', '*543215', '*35214*', '*41532*', '*2*1***'])
    True
    >>> check_uniqueness_in_rows(['***21**', '452453*', '423145*', '*543215', '*35214*', '*41532*', '*2*1***'])
    False
    >>> check_uniqueness_in_rows(['***21**', '412453*', '423145*', '*553215', '*35214*', '*41532*', '*2*1***'])
    False
    """
    board = board[1:-1]
    for line in board:
        line = line[1:-1]
        el_in_row_set = set()
        for num in line:
            if num in el_in_row_set:
                return False
            el_in_row_set.add(num)
    return True

def check_horizontal_visibility(board: list):
    """
    Check row-wise visibility (left-right and vice versa)

    Return True if all horizontal hints are satisfiable,
     i.e., for line 412453* , hint is 4, and 1245 are the four buildings
      that could be observed from the hint looking to the right.

    >>> check_horizontal_visibility(['***21**', '412453*', '423145*', '*543215', '*35214*', '*41532*', '*2*1***'])
    True
    >>> check_horizontal_visibility(['***21**', '452453*', '423145*', '*543215', '*35214*', '*41532*', '*2*1***'])
    False
    >>> check_horizontal_visibility(['***21**', '452413*', '423145*', '*543215', '*35214*', '*41532*', '*2*1***'])
    False
    """
    board = board[1:len(board)-1]
    for line in board:
        if line[0].isdigit():
            if not left_to_right_check(line,int(line[0])):
                return False
        if line[len(line)-1].isdigit():
            if not left_to_right_check(line[::-1],int(line[len(line)-1])):
                return False
    return True




def check_columns(board: list):
    """
    Check column-wise compliance of the board for uniqueness (buildings of unique height) and visibility (top-bottom and vice versa).

    Same as for horizontal cases, but aggregated in one function for vertical case, i.e. columns.

    >>> check_columns(['***21**', '412453*', '423145*', '*543215', '*35214*', '*41532*', '*2*1***'])
    True
    >>> check_columns(['***21**', '412453*', '423145*', '*543215', '*35214*', '*41232*', '*2*1***'])
    False
    >>> check_columns(['***21**', '412553*', '423145*', '*543215', '*35214*', '*41532*', '*2*1***'])
    False
    """
    new_board = []
    new_line = ''
    for index in range(len(board)):
        for line in board:
            new_line += line[index]
        new_board.append(new_line)
        new_line = ''
    if not check_uniqueness_in_rows(new_board):
        return False
    if not check_horizontal_visibility(new_board):
        return False
    return True




def check_skyscrapers(input_path: str):
    """
    Main function to check the status of skyscraper game board.
    Return True if the board status is compliant with the rules,
    False otherwise.

    >>> check_skyscrapers("check.txt")
    True
    """
    board = read_input(input_path)
    total = []
    total.append(check_not_finished_board(board))
    total.append(check_uniqueness_in_rows(board))
    total.append(check_horizontal_visibility(board))
    total.append(check_columns(board))
    if all(total):
        return True
    return False



if __name__ == "__main__":
    print(check_columns([
    '***21**', 
    '412453*', 
    '423145*', 
    '*542315', 
    '*35214*', 
    '*41532*', 
    '*2*1***']))