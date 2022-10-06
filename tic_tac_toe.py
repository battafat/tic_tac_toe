#There's a total of 9 moves.
#X potentially gets 5.
#O gets 4.

board = list()

list_1 = ["__", "__", "__"]
list_2 = ["__", "__", "__"]
list_3 = ["__", "__", "__"]



board.append(list_1)
board.append(list_2)
board.append(list_3)

print(" ")
for lst in board:
    print(lst)

coordinates = list()

row_1 = ["1,1", "1,2", "1,3"]
row_2 = ["2,1", "2,2", "2,3"]
row_3 = ["3,1", "3,2", "3,3"]

#is it important for the input to be a tuple? Could I just make the rows list of
#strings and then the user could enter a string?

#print(type(row_1[0]))

coordinates.append(row_1)
coordinates.append(row_2)
coordinates.append(row_3)

blank = "__"





#Noam said to think about inputs for variables/arguments, I think. So what are my
#inputs for make_move?:
#   board
#   coordinates??

#def make_move()

#create a function that takes the board as an argument and then returns either a
#string of the winner or false

    #Below Determines if someone won.
    #Create lists of all the 3-item win possibilities:
    #3 horizontal, 3 vertical, and 2 diagonal.
    #Then fill those lists with the moves recorded in board. When any of those
    #lists contains all items equal to themselves, someone has won.

def find_winner(board):
    # if winner, return winner
    # else: return faslse
    horizontal_wins = []

    for row in board:
        horizontal_wins.append(row)

    #create vertical win lists
    vertical_wins = []
    x = 0


    for i in range(len(board)):
    #this repeats the below for loop the number of times that board is long.
    #3 in this case. This works because the number of rows and columns is equal.
        column_vertical_win = list()
        vertical_wins.append(column_vertical_win)
    #Above, an empty list -- column_vertical_win -- was created and appended above to vertical_wins.
    #Below, for each row in board:
    #   starting with the initial list/column in vertical_wins,
    #   and the initial index in the row of board
    #   the values from that index of board are appended to the corresponding list/column.
        for row in board:
            vertical_wins[x].append(row[x])

        x = x+1
    #this increases the value of x, or the value of the index, by 1 each time

    #This creates the diagonal win possibilities, with reference to board.

    diagonal_topleft = [board[0][0], board[1][1], board[2][2]]

    diagonal_btmleft = [board[0][2], board[1][1], board[2][0]]

    diagonal_wins = [diagonal_topleft, diagonal_btmleft]

    #Below creates a master list of win lists.

    winner_master = []
    for row in horizontal_wins:
        winner_master.append(row)

    for column in vertical_wins:
        winner_master.append(column)

    for dgnl in diagonal_wins:
        winner_master.append(dgnl)

    #The below goes through the possible win lists in winner_master.
    #first: does the list contain blank positions? In which case it cannot be a win.
    #second: if it doesn't contain blank -- ie, all moves have been made in that possible
    #       win -- are all of those moves the same?
    for win in winner_master:
        #first: does the list contain blank positions? In which case it cannot be a win.
        if win[0] != blank:
        #second: if it doesn't contain blank -- ie, all moves have been made in that possible
        #       win list -- are all of those moves equal? (all X or all O)
            if win.count(win[0]) == len(win):

                print(" ")
        #This prints the winner by simply checking which character occupies the
        #the initial index in the winning list.
                return win[0]
    return False



def move_validity(coordinates, move):
    coordinates_concatenated = [item for sublist in coordinates for item in sublist]
    if move not in (coordinates_concatenated):
        return False



def user_moves(coordinates, board, player_symbol):

    move = input(f'Player {player_symbol}, enter comma-separated integers for row and column: ')

    #need to continue if the player makes an impossible move
    #for x in coordinates:
    #    if x_coordinate not in x: #Won't work bc will check each list individuall,
                                  #not all positions all at once
    print("")

    check_validity = move_validity(coordinates, move)
    if check_validity == False:
        print("Invalid format. Repeat turn: row number,column number -- no space.")
        print("")
        user_moves(coordinates, board, player_symbol)

    for row in coordinates:

        for x in row:

            if x == move:
                #This determines the column in which to enter the move in board.
                column_index = row.index(x)
                #This determines the row in which to enter the move in board.
                row_index = coordinates.index(row)

                #The below line checks if the position is taken:
                if board[row_index][column_index] != blank :
                    print("Position taken. Enter new coordinates: ")
                    return True

                else:

                    board[row_index][column_index] = player_symbol

                    print(" ")
                    #print(positions)
                    for lst in board:
                        print(lst)

#has_winner = find_winner(board)
        #check which element (X or O) it contains and declare that person a winner

#The line below checks all the items in each list of coordinates to see if any
#of them are blank


positions = [item for sublist in board for item in sublist]

current_player = "X"



while blank in positions:

    for i in range(3):
        print(" ")


    #X's turn:
#abstract
    X_moves = user_moves(coordinates, board, current_player)
    #The below repeats X's turn if they enter a move that's already been played.
    if X_moves == True:
        user_moves(coordinates, board, "X")
#When I comment out the below positions line, the "game over" functionality doesn't work
#positions doesn't get updated without it. I checked by printing it.
    positions = [item for sublist in board for item in sublist]


    announce_winner = find_winner(board)
    if type(announce_winner) == str:
        print("X wins!")
        break
#below just switches between players
    if current_player == "X":
        current_player = "O"
    else:
        current_player = "X"

    print(" ")
    print(" ")


    for i in range(3):
        print(" ")




else:
    print("Game Over! Draw")
    print("")

#What happens if the user inputs an unuseable format or a space that's already taken?



#Maybe there’s a possibility that I could associate all the number with their
# row instead of having two numbers. For instance, row_1 could contain just
# 1, 2, 3 instead of (1,1) (1,2) (1,3)

#x_user_input = input("Enter space-separated integers for row and column: ")
#x_coordinate = tuple(int(item) for item in x_user_input.split())
#print("X coordinate: ", x_coordinate)
#print("Type of x_coordinate", type(x_coordinate))

#What are the possible ways that you can win?
#Diagonal, vertical, horizonal 3 in a row
#
