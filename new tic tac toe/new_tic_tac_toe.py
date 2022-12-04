#write the simplest possible code to return 1
# def how_many_rows_do_you_want():
#

number_of_rows = 3
#The number_of_columns is equal to the number_of_rows because it's a square
number_of_columns = number_of_rows

possible_moves = [1, 2, 3, 4, 5, 6, 7, 8, 9]

number_of_squares = (number_of_rows)**2

# play_the_game = play_tic_tac_toe(number_of_squares, number_of_rows, board)


# play_the_game = play_tic_tac_toe(number_of_squares, number_of_rows, board)


def square_count(number_of_squares):
    number_of_squares = 9
    return number_of_squares


def make_board(number_of_squares):
    #I want to refactor to make the board create just based on the number_of_squares

    board = {}
    counter = 1
    for x in range(number_of_squares):
        board[counter] = counter
        counter = counter + 1

    return board


def display_board(board):
    print("")
    print(board[1], board[2], board[3])
    print(board[4], board[5], board[6])
    print(board[7], board[8], board[9])
    print("")

# display_board = display_board(board)
# initial_key = 1

def make_a_row(board, number_of_columns, initial_key):
#This function makes a row.
#Number_of_rows determines how many
    row = {}
    for x in range(number_of_columns):
        row[initial_key] = board[initial_key]
        initial_key += 1
    return row


# def make_rows(board, number_of_rows):
#     #see if you can append just 1 : 1 to to row_one
#     row_one = {}
#
# # def make_row
# # how do I refactor to make
#     y = 1
#     for x in range(number_of_rows):
#         row_one[y] = board[y]
#         y += 1
#     #after you run it three times, at this indent level, just add 1 to y (or initial_key)
#
#     row_two = {}
#     y = 4
#     for x in range(number_of_rows):
#         row_two[y] = board[y]
#         y += 1
#
#     row_three = {}
#     y = 7
#     for x in range(number_of_rows):
#         row_three[y] = board[y]
#         y += 1


    # row_two = {4 : 4, 5 : 5, 6 : 6}
    # row_three = {7 : 7, 8 : 8, 9 : 9}

    # row_three = {7 : 7, 8 : 8, 9 : 9}
    return row_one, row_two, row_three
    #, row_two, row_three

# a = make_rows(board, number_of_rows)

def check_move_validity(user_move, board, player_symbol):
    if user_move not in possible_moves:
        print("")
        print("Move invalid. Input one of the remaining integers between 1 and 9.")
        print("")
        return False

#The below if statement checks to see if the space in the board, the value at that key,
#is already occupied by an X or an O.

    if type(board[user_move]) != int:
        print("")
        print("Move invalid. Input one of the remaining integers between 1 and 9.")
        print("")
        return False

def make_move(board, player_symbol):
    # board = make_board(number_of_squares)
    user_move = (input(f"Player {player_symbol}, type in the integer where you want to go: "))

    try:
        int(user_move)
    except:
        


    move_is_valid = check_move_validity(user_move, board, player_symbol)
    if move_is_valid == False:
        # This repeats the turn if the user inputs an invalid move.
        make_move(board, player_symbol)
    else:
        board[user_move] = player_symbol
        display_board(board)
    return board

def check_for_winner(board, player_symbol):

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

#Things to do:





# def announce_winner():

# def check_game_over():

def switch_player_symbol(player_symbol):
    if player_symbol == "X":
        player_symbol = "O"
        # return player_symbol
    else:
        player_symbol = "X"

    return player_symbol



def loop_turns_until_win_or_draw(board, player_symbol):
    while sum(1 for value in board.values() if value == "X") < 5:

        #board = play_tic_tac_toe(number_of_squares, number_of_rows, board, player_symbol)
        board = make_move(board, player_symbol)
        win_check = check_for_winner(board, player_symbol)

        if win_check == True:
            print("")
            print(f"Congratulations, Player {player_symbol} wins!")
            print("Game over!")
            print("")
            return

        player_symbol = switch_player_symbol(player_symbol)
        # if player_symbol == "X":
        #     player_symbol = "O"
        # else:
        #     player_symbol = "X"
    else:
        print("Game Over! Draw")
        print("")
        return

# def play_tic_tac_toe(number_of_squares, number_of_rows, board, player_symbol):
# #    board = make_board(number_of_squares)
# #    display = display_board(board)
#     board = make_move(board, player_symbol)
#     return board


def start_game():

    board = make_board(number_of_squares)
    display = display_board(board)
    player_symbol = "X"

    loop_turns_until_win_or_draw(board, player_symbol)

    # while sum(1 for value in board.values() if value == "X") < 5:
    #
    #     #board = play_tic_tac_toe(number_of_squares, number_of_rows, board, player_symbol)
    #     board = make_move(board, player_symbol)
    #     if player_symbol == "X":
    #         player_symbol = "O"
    #     else:
    #         player_symbol = "X"
    # else:
    #     print("Game Over! Draw")
    #     print("")


start_game()
# def alternate_player_symbol():
#     if make_move(board, player_symbol) == "X"
#         make_move(board, "O")



# print(make_move(board, player_symbol))
#print(board[1], board[2], board[3])

# def play_game():

# print(a)

# def display_board(board):
#     #board = make_board(number_of_squares)
#
#     return print(board)
#
# display_board(board)
