number_of_rows = 3

possible_moves = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]

number_of_squares = (number_of_rows)**2

def make_board(number_of_squares):
#This sets up the 3 by 3 tic-tac-toe board as a dictionary.
    board = {}
    counter = 1
    for x in range(number_of_squares):
        board[counter] = counter
        counter += 1

    return board

def display_board(board):
#This prints out the three rows of the board for the user to see.
    print("")
    print(board[1], board[2], board[3])
    print(board[4], board[5], board[6])
    print(board[7], board[8], board[9])
    print("")

def check_move_validity(user_move, board, player_symbol):
#This checks the user's move to make sure it is one of the options.
#If it is in the possible_moves list, we take the int of the string they've entered.
#If not, the user is prompted to enter a valid move.
    if user_move not in possible_moves:
        # print("")
        print("\nMove invalid. Input one of the remaining integers between 1 and 9.\n")
        # print("")
        # make_move(board, player_symbol)
        return False
    else:
        return int(user_move)

def check_if_move_available(int_user_move, board):
#This checks to make sure the user move hasn't already been played.
#If it has already been played, the user is prompted to enter a valid move.
    if type(board[int_user_move]) != int:
        print("\nMove invalid. Input one of the remaining integers between 1 and 9.\n")

        return False

def make_move(board, player_symbol):
# This prompts the user to enter their move.
# If the move is both valid and available, the move is entered in the board.
# If not -- if it is False -- the turn restarts, asking the user to enter a
# valid move.
    user_move = (input(f"Player {player_symbol}, type in the integer where you want to go: "))


    int_user_move = check_move_validity(user_move, board, player_symbol)

    if user_move == False:
        # This repeats the turn if the user inputs an invalid move.
        return make_move(board, player_symbol)

    move_is_available = check_if_move_available(int_user_move, board)

    if move_is_available == False:
        return make_move(board, player_symbol)

    else:
        board[int_user_move] = player_symbol
        display_board(board)
    return board

def check_for_winner(board, player_symbol):
# This function lists the possible win sequences.
# It then checks those lists for three in a row of either X or O.

    row_1 = [board[1], board[2], board[3]]
    row_2 = [board[4], board[5], board[6]]
    row_3 = [board[7], board[8], board[9]]

    column_1 = [board[1], board[4], board[7]]
    column_2 = [board[2], board[5], board[8]]
    column_3 = [board[3], board[6], board[9]]

    diagonal_1 = [board[1], board[5], board[9]]
    diagonal_2 = [board[3], board[5], board[7]]

    possible_win_lists = [
                        row_1,
                        row_2,
                        row_3,
                        column_1,
                        column_2,
                        column_3,
                        diagonal_1,
                        diagonal_2
                        ]
    for win in possible_win_lists:
        if win.count(win[0]) == len(win):
            return True

def switch_player_symbol(player_symbol):
# This function alternates the player, starting with X as the default 1st to move.

    if player_symbol == "X":
        player_symbol = "O"
        # return player_symbol
    else:
        player_symbol = "X"

    return player_symbol

def loop_turns_until_win_or_draw(board, player_symbol):
# This function loops the alternating turns.
# It checks for a winner after the player makes a move.
# It also stops the game after X's final turn and declares a draw if no one won.

    while sum(1 for value in board.values() if value == "X") < 5:

        board = make_move(board, player_symbol)
        win_check = check_for_winner(board, player_symbol)

        if win_check == True:
            print(f"\nCongratulations! Player {player_symbol} wins!\n")
            print("\nGame over!\n")
            return

        player_symbol = switch_player_symbol(player_symbol)

    else:
        print("\nGame Over! Draw\n")
        return

def play_game():
# This function starts the game by making the board, printing the board, and
# running alternating turns until the game is over.

    board = make_board(number_of_squares)
    display_board(board)
    player_symbol = "X"

    loop_turns_until_win_or_draw(board, player_symbol)

play_game()
