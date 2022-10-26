#write the simplest possible code to return 1
number_of_squares = 9

def square_count(number_of_squares):
    number_of_squares = 9
    return number_of_squares

def make_board(number_of_squares):
    #I want to refactor to make the board create just based on the number_of_squares


    #how to add 9:9 to a dictionary, based on number_of_squares
    board = {}
    counter = 1
    for x in range(number_of_squares):
        board[counter] = counter
        counter = counter + 1

    # board = {}
    # board[number_of_squares] = number_of_squares
    # board[number_of_squares - 1] = number_of_squares - 1
    # board[number_of_squares - 2] = number_of_squares - 2
    # board[number_of_squares - 3] = number_of_squares - 3
    # board[number_of_squares - 4] = number_of_squares - 4
    # board[number_of_squares - 5] = number_of_squares - 5
    # board[number_of_squares - 6] = number_of_squares - 6
    # board[number_of_squares - 7] = number_of_squares - 7
    # board[number_of_squares - 8] = number_of_squares - 8

    return board
