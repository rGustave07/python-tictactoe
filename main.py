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
        print("\n")

        print_board(row, column, player)
        if check_win():
            print("Game Over")
            retry = input("Would you like to try again? (True/False)")
            if retry == 'False':
                tryagain = False


def print_board(row, column, player):
    board[row][column] = player

    print(board[0])
    print(board[1])
    print(board[2])


def check_win():
    if board[0][0] == 'X' or board[0][0] == 'O' and board[0][1] == 'X' or board[0][1] == 'O' and board[0][2] == 'X' or board[0][2] == 'O':
        return True
    elif board[1][0] == 'X' or board[1][0] == 'O' and board[1][1] == 'X' or board[1][1] == 'O' and board[1][2] == 'X' or board[1][2] == 'O':
        return True
    elif board[2][0] == 'X' or board[2][0] == 'O' and board[2][1] == 'X' or board[2][1] == 'O' and board[2][2] == 'X' or board[2][2] == 'O':
        return True
    elif board[0][0] == 'X' or board[0][0] == 'O' and board[1][0] == 'X' or board[1][0] == 'O' and board[2][0] == 'X' or board[2][0] == 'O':
        return True
    elif board[0][1] == 'X' or board[0][1] == 'O' and board[1][1] == 'X' or board[1][1] == 'O' and board[2][1] == 'X' or board[2][1] == 'O':
        return True
    elif board[0][2] == 'X' or board[0][2] == 'O' and board[1][2] == 'X' or board[1][2] == 'O' and board[2][2] == 'X' or board[2][2] == 'O':
        return True
    elif board[0][0] == 'X' or board[0][0] == 'O' and board[1][1] == 'X' or board[1][1] == 'O' and board[2][2] == 'X' or board[2][2] == 'O':
        return True
    elif board[0][2] == 'X' or board[0][2] == 'O' and board[1][1] == 'X' or board[1][1] == 'O' and board[2][0] == 'X' or board[2][0] == 'O':
        return True
    else:
        return False


def player_decision():
    print("X goes first (Choose 1-9): ")


menu(True)