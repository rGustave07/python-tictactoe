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

def print_board(row, column, player):
    board[row][column] = player

    print(board[0])
    print(board[1])
    print(board[2])


def player_decision():
    print("X goes first (Choose 1-9): ")


menu(True)