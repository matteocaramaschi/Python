from random import randrange   # Necessary to use randrange() method

# Prints the board
def display_board(board):
    print("+-------+-------+-------+")

    # We know that each row is composed by three squares, so we directly print them.
    for row in board:
        print("|       |       |       |")
        print("|   ", row[0], "   |   ", row[1], "   |   ", row[2], "   |", sep="")
        print("|       |       |       |")
        print("+-------+-------+-------+")
    print()

# Asks user to enter a move, checkes the input and updates the board
def enter_move(board):
    move_is_valid = False
    while(not move_is_valid):
        try:
            move = int(input("Enter your move: "))
            if move in range(1,10):
                if move >= 1 and move < 4 and board[0][move - 1] not in ["X", "O"]:     # Move in the first row
                    move_is_valid = True
                    board[0][move - 1] = "O"
                elif move >= 4 and move < 7 and board[1][move % 4] not in ["X", "O"]:   # Move in the second row: using module with
                    move_is_valid = True                                                # first column to retrieve the correct square
                    board[1][move % 4] = "O"
                elif move >= 7 and move <= 9 and board[2][move % 7] not in ["X", "O"]:  # Move in the third row: using module with
                    move_is_valid = True                                                # first column to retrieve the correct square
                    board[2][move % 7] = "O"
                else:
                    print("The square is already filled. Please enter another number.\n")
            else:
                print("Invalid input. Please enter a number between 1 and 9.\n")
        except ValueError:
            print("Input entered is not an integer number. Retry.\n")
            
    display_board(board)

# Shows current available squares to help the user
def make_list_of_free_fields(board):
    free_squares = []
    print("The current free squares are the following:")
    for row in board:
        for value in row:
            if value != "X" and value != "O":
                free_squares.append(value)
    
    print(free_squares, end="\n\n")

# Checks if someone won
def victory_for(board, sign):
    victory = False

    # Row wins
    if board[0][0] == sign and board[0][1] == sign and board[0][2] == sign:
        victory = True
    elif board[1][0] == sign and board[1][1] == sign and board[1][2] == sign:
        victory = True
    elif board[2][0] == sign and board[2][1] == sign and board[2][2] == sign:
        victory = True

    # Column wins
    elif board[0][0] == sign and board[1][0] == sign and board[2][0] == sign:
        victory = True
    elif board[0][1] == sign and board[1][1] == sign and board[2][1] == sign:
        victory = True
    elif board[0][2] == sign and board[1][2] == sign and board[2][2] == sign:
        victory = True

    # Diagonal wins
    elif board[0][0] == sign and board[1][1] == sign and board[2][2] == sign:
        victory = True
    elif board[0][2] == sign and board[1][1] == sign and board[2][0] == sign:
        victory = True

    if victory:
        if sign == "X":
            print("Computer wins!")
        else:
            print("You won!")
    
    return victory

# Calculates computer's move
def draw_move(board):
    move_is_valid = False
    while(not move_is_valid):
        move = randrange(1,10)
        if move >= 1 and move < 4 and board[0][move - 1] not in ["X", "O"]:
            move_is_valid = True
            board[0][move - 1] = "X"
        elif move >= 4 and move < 7 and board[1][move % 4] not in ["X", "O"]:
            move_is_valid = True
            board[1][move % 4] = "X"
        elif move >= 7 and move <= 9 and board[2][move % 7] not in ["X", "O"]:
            move_is_valid = True
            board[2][move % 7] = "X"

    print("Computer's move:")
    display_board(board)

# Main
print("Welcome to Tic Tac Toe!", "Computer plays as X, you play as O.", sep="\n")

board = [[1,2,3], [4,'X',6], [7,8,9]]

print("Computer starts from the center square.\n")
display_board(board)

player_turn = True

# Iterate until 8, which are the maximum moves allowed for a draw
for i in range(1,9):
    if player_turn:
        make_list_of_free_fields(board)
        enter_move(board)
        if victory_for(board, "O"):
            break
        player_turn = False
    else:
        draw_move(board)
        if victory_for(board, "X"):
            break
        player_turn = True
else:
    print("It's a draw!")
