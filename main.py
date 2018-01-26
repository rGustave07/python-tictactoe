# tic tac toe game
import random

global current_player
current_player = 'X'
board = ['hold', '1', '2', '3', '4', '5', '7', '7', '8', '9']


def print_board(board):
    print("Enter the corresponding number on the keyboard to make your selection!\n")
    print("            |            |            ")
    print("     " + str(board[1]) + "      |      " + str(board[2]) + "     |      " + str(board[3]) + "     ")
    print("____________|____________|____________")
    print("            |            |            ")
    print("     " + str(board[4]) + "      |      " + str(board[5]) + "     |      " + str(board[6]) + "     ")
    print("____________|____________|____________")
    print("            |            |            ")
    print("     " + str(board[7]) + "      |      " + str(board[8]) + "     |      " + str(board[9]) + "     ")
    print("            |            |            ")


def menu(current_player):
    new_game = input("Welcome to Tic-Tac-Toe! Would you like to start a new game?(Y/N) \n")
    if new_game.lower() == 'y':
        start = True
    else:
        start = False

    while start:
        print_board(board)
        select_first_player()
        result_check(current_player)

        start = retry()


def select_first_player():
    first_time = True
    if random.randint(0,2) == 1 and first_time:
        first_time = False
        current_player = 'X'
        print(current_player + " goes first")
        player_turn(current_player)
    elif first_time:
        first_time = False
        current_player = 'O'
        print(current_player + " goes first")
        player_turn(current_player)

    player_turn(current_player)


def result_check(current_player):
    for element in board[1:]:
        if element != 'X' and element != 'O' and not element.isalnum():
            print("The Game is Tied!")
        else:
            player_turn(current_player)

    if   board[1] == board[4] == board[7]:
        print(board[1] + " wins!")
    elif board[1] == board[5] == board[9]:
        print(board[1] + " wins!")
    elif board[1] == board[2] == board[3]:
        print(board[1] + " wins!")
    elif board[2] == board[5] == board[8]:
        print(board[2] + " wins!")
    elif board[3] == board[5] == board[7]:
        print(board[3] + " wins! ")
    elif board[3] == board[6] == board[9]:
        print(board[3] + " wins! ")
    elif board[4] == board[5] == board[6]:
        print(board[4] + " wins! ")
    elif board[7] == board[8] == board[9]:
        print(board[7] + " wins! ")
    else:
        pass


def player_turn(current_player):
    mark = input( current_player + " player select your box: ")
    board[int(mark)] = current_player
    print_board(board)
    if current_player == 'X':
        current_player = 'O'
    elif current_player == 'O':
        current_player = 'X'


def retry():
    new_game = input("Would you like to start a new game?(Y/N)")

    if new_game.lower() == 'y':
        return True
    elif new_game.lower() == 'n':
        return False
    else:
        return False


menu(current_player)