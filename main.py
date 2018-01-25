# tic tac toe game

board = [
    ['_', '_', '_'],
    ['_', '_', '_'],
    ['_', '_', '_']
]


def menu(tryagain):
    while tryagain:
        # Define function that starts game
        row = int(input("Enter row selection: "))
        column = int(input("Enter column selection: "))
        player = input("Enter Mark: ")

        print_board(row, column, player)
        if check_win():
            print("Game Over")


def print_board(row, column, player):
    board[row][column] = player

    print(board[0])
    print(board[1])
    print(board[2])


def check_win():
    if board[0][0] == 'X' and board[0][1] == 'X' and board[0][2] == 'X':
        return True
    elif board[1][0] == 'X' and board[1][1] == 'X' and board[1][2] == 'X':
        return True
    elif board[2][0] == 'X' and board[2][1] == 'X' and board[2][2] == 'X':
        return True
    elif board[0][0] == 'X' and board[1][0] == 'X' and board[2][0] == 'X':
        return True
    elif board[0][1] == 'X' and board[1][1] == 'X' and board[2][1] == 'X':
        return True
    elif board[0][2] == 'X' and board[1][2] == 'X' and board[2][2] == 'X':
        return True
    elif board[0][0] == 'X' and board[1][1] == 'X' and board[2][2] == 'X':
        return True
    elif board[0][2] == 'X' and board[1][1] == 'X' and board[2][0] == 'X':
        return True
    else:
        return False


def player_decision():
    print("X goes first (Choose 1-9): ")


menu(True)