

def vertical_check(board: list, position: int):
    counter = 0
    current = 0
    for row in board:
        if row[position] == 0:
            continue
        if row[position] != current:
            current = row[position]
            counter = 1
            continue
        counter += 1
        if counter >= 4:
            return True
    return False


def horizontal_check(board: list, height: int):
    row = board[height]
    counter = 0
    current = 0
    for i in row:
        if i == 0:
            counter = 0
            current = 0
            continue
        if i != current:
            current = i
            counter = 1
            continue
        counter += 1
        if counter >= 4:
            return True
    return False

# need to fix the point tracking in this function. it goes left to right top to bottom checking the diagonal.
# top statement is fixed, now need to add for when position > height. :( this is harder than i wanted it to be. my code looks so terrible

# loops through diagonal in matrix, lr determines top right -> bottom left (lr: -1), top left -> bottom right (lr: 1)


def diagonal_counter(board: list, start: int, end: int, start_index: int, lr: int):
    point_count = 0
    index = start_index
    current = 0
    for row in range(start, end):
        index += lr
        if board[row][index] == 0:
            current = 0
            point_count = 0
            continue
        if board[row][index] != current:
            current = board[row][index]
            point_count = 1
            continue
        point_count += 1
        if point_count >= 4:
            return True
    return False


# Function checks the diagonals l to r (top to bottom) for a win condition.
def lr_diagonal_check(board: list, position: int, height: int):
    reference = max((height, position)) - min((height, position))
    # Save some computing power if we're too close to the sides. At these positions, the game cannot be won on the diagonal.
    if reference > 3:
        return False
    point_count = 0
    current = 0
    if height >= position:
        return diagonal_counter(board, reference, 6, -1, 1)
        counter = -1
        # As the loop going through the diagonal is directly dependent on counter then it must always increase by 1 regardless of the conditions met. Basic requirement for the loop to work.
        for row_1 in range(reference, 6):
            counter += 1
            if board[row_1][counter] == 0:
                point_count = 0
                current = 0
                continue
            if board[row_1][counter] != current:
                current = board[row_1][counter]
                point_count = 1
                continue
            point_count += 1
            if point_count >= 4:
                return True
    else:
        return diagonal_counter(board, 0, 7 - reference, reference - 1, 1)
        counter = reference - 1
        # makes sure to not cause any index errors, so row counting stops depending on the position of the diagonal
        for row_2 in range(7-reference):
            counter += 1
            if board[row_2][counter] == 0:
                point_count = 0
                current = 0
                continue
            if board[row_2][counter] != current:
                current = board[row_2][counter]
                point_count = 1
                continue
            point_count += 1
            if point_count >= 4:
                return True
    return False


# Probably not the most efficient way to do this, but it works.
def rl_diagonal_check(board: list, position: int, height: int):
    x = position - 7
    reference = x + height
    if height >= -(1 + x):
        return diagonal_counter(board, reference + 1, 6, 0, -1)
        counter = 0
        for row_1 in range(reference + 1, 6):
            counter -= 1
            if board[row_1][counter] == 0:
                current = 0
                point_count = 0
                continue
            if board[row_1][counter] != current:
                current = board[row_1][counter]
                point_count = 1
                continue
            point_count += 1
            if point_count >= 4:
                return True
    else:
        return diagonal_counter(board, 0, reference + 8, reference + 1, -1)
        counter = reference + 1
        for row_2 in range(reference + 8):
            counter -= 1
            if board[row_2][counter] == 0:
                current = 0
                point_count = 0
                continue
            if board[row_2][counter] != current:
                current = board[row_2][counter]
                point_count = 1
                continue
            point_count += 1
            if point_count >= 4:
                return True
    return False


board = [
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 2, 1, 0, 0],
        [0, 2, 0, 1, 0, 0, 0],
        [0, 2, 1, 2, 1, 2, 0],
        [1, 1, 0, 1, 1, 0, 2],
        [1, 1, 2, 1, 2, 0, 0]
]


def print_board(board: list):
    for row in board:
        print(" |", end='')
        for i in row:
            if i == 0:
                print(" O", end='')
            if i == 1:
                print(" R", end='')
            if i == 2:
                print(" Y", end='')
        print(" |")
        print()


def win_check(board: list, position: int, height:  int):
    print(vertical_check(board, position))
    print(horizontal_check(board, height))
    print(lr_diagonal_check(board, position, height))
    print(rl_diagonal_check(board, position, height))

    return vertical_check(board, position) or horizontal_check(board, height) or lr_diagonal_check(board, position, height) or rl_diagonal_check(board, position, height)


print_board(board)

print(win_check(board, 6, 4))
