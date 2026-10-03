from rich import print
import time

game_board = [
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0]
]

# Banner is formatted wrong i i add spaces on teh first line
banner = '''
 [yellow]______    _______    __   __    __   __    ______    ______    __________[/yellow]     [red]__    __[/red]
[yellow]|  ____|  |  ___  |  |  \\ |  |  |  \\ |  |  |  ____|  |  ____|  |___    ___|[/yellow]   [red]|  |  |  |[/red]
[yellow]| |       | |   | |  |   \\|  |  |   \\|  |  | |__     | |           |  |[/yellow]       [red]|  |__|  |[/red]
[yellow]| |       | |   | |  |  \\ |  |  |  \\ |  |  |  __|    | |           |  |[/yellow]       [red]|______  |[/red]
[yellow]| |____   | |___| |  |  |\\   |  |  |\\   |  | |____   | |____       |  |[/yellow]             [red]|  |[/red]
[yellow]|______|  |_______|  |__| \\__|  |__| \\__|  |______|  |______|      |__|[/yellow]             [red]|__|[/red]

'''

player_chips = {
    0: " O",
    1: " [bold red]O[/bold red]",
    2: " [bold yellow]O[/bold yellow]"
}


def print_board(board: list):
    for row in board:
        print(" |", end='')
        for i in row:
            print(player_chips[i], end="")
        print(" |")
        print()


def determine_slot(board: list, position: int):
    height_count = -1
    for row in board:
        if row[position] != 0:
            break
        height_count += 1
    return height_count


# def add_chip(board: list, position: int, player: int):
#    height = determine_slot(board, position)
#   if height not in {0, 1, 2, 3, 4, 5, 6}:
#       return
#  board[height][position] = player
#  return board


def add_chip(board: list, position: int, player: int):
    height = determine_slot(board, position)
    if height not in {0, 1, 2, 3, 4, 5}:
        return
    for i in range(height + 1):
        print("\n" * 10)
        board[i][position] = player
        print_board(board)
        board[i][position] = 0
        time.sleep(0.15)
    board[height][position] = player
    return board


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


# loops through diagonal in matrix. lr determines: top right -> bottom left (lr = -1), top left -> bottom right (lr = 1)
def diagonal_loop(board: list, start: int, end: int, start_index: int, lr: int):
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


# Arguments for start, end and start_index were determined on pen and paper, not sure if i will be able to decipher this later.
def lr_diagonal_check(board: list, position: int, height: int):
    reference = max((height, position)) - min((height, position))
    if reference > 3:
        return False
    if height >= position:
        return diagonal_loop(board, reference, 6, -1, 1)
    else:
        return diagonal_loop(board, 0, 7 - reference, reference - 1, 1)


def rl_diagonal_check(board: list, position: int, height: int):
    x = position - 7
    reference = x + height
    if height >= -(1 + x):
        return diagonal_loop(board, reference + 1, 6, 0, -1)
    else:
        return diagonal_loop(board, 0, reference + 8, reference + 1, -1)


def win_check(board: list, position: int, height:  int):
    return vertical_check(board, position) or horizontal_check(board, height) or lr_diagonal_check(board, position, height) or rl_diagonal_check(board, position, height)


def main(board: list):
    x = 0
    print(banner)
    input("Press any key to continue")
    print_board(board)
    game_counter = 0
    while game_counter < 42:
        try:
            p_input = int(
                input(f"Player {x+1} please choose where you want to insert your chip (0-6): "))
        except ValueError:
            print("Please type in a valid number (0-6)")
            continue
        if p_input not in {0, 1, 2, 3, 4, 5, 6}:
            print("Please type in a valid number (0-6)")
            continue
        height = determine_slot(board, p_input)
        if add_chip(board, p_input, x + 1) == None:
            print("You can't put chips there anymore!")
            continue
        if win_check(board, p_input, height):
            print("\n" * 10)
            print_board(board)
            print(f"Player {1+x} wins!!")
            return
        x = 1 - x
        game_counter += 1
    print("This game is a draw!!")


main(game_board)
