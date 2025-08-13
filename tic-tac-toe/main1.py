# ---------------- Global Variables ---------------- #
# Game board
board = ["-","-","-",
         "-","-","-",
         "-","-","-"]

# If game is still going
game_still_going = True

# who won? or tie?
winner = None

# Current player
current_player = "X"

def display_board():
    print(board[0] + " | " + board[1] + " | " + board[2])
    print(board[3] + " | " + board[4] + " | " + board[5])
    print(board[6] + " | " + board[7] + " | " + board[8])
# play the game tic tac toe
def play_game():
 
    # Display initail board 
    display_board()
    # while the game is still going
    while game_still_going:
        # Handle a single turn of an arbitrary player
        handle_turn(current_player)

        # Check if the game has ended
        check_if_game_over()

        # Flip to the other player
        flip_player(current_player)

    # The game has ended
    if winner == "X" or winner == "O":
        print(winner + " won!")
    elif winner is None:
        print("It's a draw!")

    
def handle_turn(player):

    global current_player

    position = int(input("Choose a position from 1-9: "))
    position = position - 1  # Convert to 0-indexed

    if player == "X":
        board[position] = player
        display_board()
    elif player == "O":
        board[position] = player
        display_board()
    

def check_if_game_over():
    check_for_winner()
    check_for_draw()

def check_for_winner():
    # set up global variables
    global winner
    # check rows
    row_winner = check_rows()
    # check columns
    col_winner = check_columns()
    # check diagonals
    diag_winner = check_diagonals()

    if row_winner:
        winner = row_winner
    elif col_winner:
        winner = col_winner
    elif diag_winner:
        winner = diag_winner
    else:
        winner = None
    return

# check rows
def check_rows():
    # Set up global variables
    global game_still_going
    # Check if any of the rows have all the same value (and is not empty)
    row_1 = board[0] == board[1] == board[2] != "-"
    row_2 = board[3] == board[4] == board[5] != "-"
    row_3 = board[6] == board[7] == board[8] != "-"
    # If any row does have a match, flag that there is a win
    if row_1 or row_2 or row_3:
        game_still_going = False
    if row_1:
        return board[0]
    elif row_2:
        return board[3]
    elif row_3:
        return board[6]
    return
# check columns
def check_columns():
    # Set up global variables
    global game_still_going
    col_1 = board[0] == board[3] == board[6] != "-"
    col_2 = board[1] == board[4] == board[7] != "-"
    col_3 = board[2] == board[5] == board[8] != "-"
    # If any col does have a match, flag that there is a win
    if col_1 or col_2 or col_3:
        game_still_going = False
    if col_1:
        return board[0]
    elif col_2:
        return board[1]
    elif col_3:
        return board[2]
    return

# check diagonals
def check_diagonals():
    # Set up global variables
    global game_still_going
    diag_1 = board[0] == board[4] == board[8] != "-"
    diag_2 = board[2] == board[4] == board[6] != "-"
    # If any diag does have a mathc, flag that there is a win
    if diag_1 or diag_2:
        game_still_going = False
    if diag_1:
        return board[0]
    elif diag_2:
        return board[6]
    return
def check_for_draw():
    return


# Change the turn of the player
def flip_player(player):

    global current_player

    if player == "X":
        current_player = "O"
    else:
        current_player = "X"
    return current_player

play_game()