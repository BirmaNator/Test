# --------------- Variables ---------------

# Hold's game board data - use to display
board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-"]

# Hold's the current player's marker - X is allways 1st
current_player = 'X'

# Hold's the winner 
winner = None

# Place holder for game
game_is_running = True


# --------------- Functions ---------------

# Display the game board to the screen
def dislay_board():
    """
    :return: prints game board
    """
    print("\n")
    print(board[0] + " | " + board[1] + " | " + board[2] + "     1 | 2 | 3")
    print(board[3] + " | " + board[4] + " | " + board[5] + "     4 | 5 | 6")
    print(board[6] + " | " + board[7] + " | " + board[8] + "     7 | 8 | 9")
    print("\n")


# Checks if game board is full
def check_board(board):
    """
    :param board:
    :return: Changes game_is_running  value
    """
    if "-" not in board:
        game_is_running = False
    else:
        game_is_running = True


# Checks winner
def check_winner(board):
    """
    :param board:
    :return: X or Y if there is a winner else returns None
    """
    if game_is_running == False:
        if check_rows(board) != None:
            winnner = check_rows(board)
        elif check_columns(board) != None:
            winnner = check_columns(board)
        elif check_diagonals(board) != None:
            winnner = check_diagonals(board)
        else:
            winnner = None


def turn_handler(current_player):
    """
    :param current_player:
    :return: inserts players pick if valid to the game board
    """
    print(current_player + 's Turn:')
    display_board(board)
    position = input('Enter a number between 1-9')
    valid = False
    while not valid:
        while position not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            position = input('Enter a number between 1-9')

        position = int(position) - 1
        if board[position] == '-':
            valid = True
        else:
            print("This place is already taken, pick another one")
    board[position] = current_player


def flip_player():
    """
    :return: changes current_player value
    """
    if current_player == "X":
        current_player = "O"
    elif current_player == "O":
        current_player = "X"


def check_rows(board):
    """
    :param board:
    :return: checks if rows value is the same
    """
    row1 = board[0] == board[1] == board[2] != "-"
    row2 = board[3] == board[4] == board[5] != "-"
    row3 = board[6] == board[7] == board[8] != "-"
    if row1 or row2 or row3:
        game_is_running = False
    if row1:
        return board[0]
    if row2:
        return board[3]
    if row3:
        return board[6]
    else:
        return None


def check_columns(board):
    """
    :param board:
    :return: checks if columns value is the same
    """
    column1 = board[0] == board[3] == board[6] != "-"
    column2 = board[1] == board[4] == board[7] != "-"
    column3 = board[2] == board[6] == board[8] != "-"
    if column1 or column2 or column3:
        game_is_running = False
    if column1:
        return board[0]
    if column2:
        return board[1]
    if column3:
        return board[2]
    else:
        return None


def check_diagonals(board):
    """
    :param board:
    :return: checks if diagonal value is the same
    """
    diagonal1 = board[0] == board[5] == board[8] != "-"
    diagonal2 = board[7] == board[5] == board[2] != "-"
    if diagonal1 or diagonal2:
        game_is_running = False
    if diagonal1:
        return board[0]
    if diagonal2:
        return board[7]
    else:
        return None


def play():
    """
    :return: run's the flow of the game and prints an output
    """
    display_board()
    while game_is_running:
        turn_handler(current_player)
        check_board(board)
        check_winner(board)
        flip_player()
    if winner == 'X' or winner == 'O':
        print(winner + "Won")
    else:
        print("It's a TIE")


# --------------- Let's play ---------------
play()
