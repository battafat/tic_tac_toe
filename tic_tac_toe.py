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


        #check which element (X or O) it contains and declare that person a winner

#The line below checks all the items in each list of coordinates to see if any
#of them are blank.
positions = [item for sublist in board for item in sublist]


while blank in positions:

    for i in range(3):
        print(" ")

#X makes their move.

    x_coordinate = input("Player X, enter comma-separated integers for row and column: ")

    #need to continue if the player makes an impossible move
    #for x in coordinates:
    #    if x_coordinate not in x: #Won't work bc will check each list individuall,
                                  #not all positions all at once
    print("")

    for row in coordinates:

        for x in row:

            if x == x_coordinate:
                #This determines the column in which to enter the move in board.
                column_index = row.index(x)
                #This determines the row in which to enter the move in board.
                row_index = coordinates.index(row)

                #The below line checks if the position is taken:
                if board[row_index][column_index] != blank :
                    print("Position taken. Enter new coordinates: ")

                else:

                    board[row_index][column_index] = "X"
                    print(" ")
                    for lst in board:
                        print(lst)


    #Below Determines if someone won.
    #Create lists of all the 3-item win possibilities:
    #3 horizontal, 3 vertical, and 2 diagonal.
    #Then fill those lists with the moves recorded in board. When any of those
    #lists contains all items equal to themselves, someone has won.

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
                print(win[0], "wins!")
                #At this point I want to break out of the While loop, but I haven't
                #figured out a way to do so yet.
                #break


    #O's Turn:
    print(" ")
    print(" ")

    o_coordinate = input("Player O, enter comma-separated integers for row and column: ")


    for row in coordinates:

        for x in row:

            if x == o_coordinate:

                column_index = row.index(x)

                print(" ")
                print(" ")

                row_index = coordinates.index(row)

                #The below line checks if the position is taken:
                if board[row_index][column_index] != blank :
                    print("Position taken. Enter new coordinates: ")
                    continue
                else:
                    board[row_index][column_index] = "O"
                    for lst in board:
                        print(lst)
    #print("line 210, vertical_wins", vertical_wins)

    horizontal_wins = []

    for row in board:
        horizontal_wins.append(row)

    #print("line 51, horizontal_wins", horizontal_wins)

    vertical_wins = []
    x = 0


    for i in range(len(board)):
    #this repeats the below for loop the number of times that board is long. 3 in this case.
        column_vertical_win = list()
        vertical_wins.append(column_vertical_win)
        for row in board:
        #for each of the rows in board, so 3 times in this case. It goes to each row.
        #    column_vertical_win.append(row[x])
            #This appends the initial index of the row it's on to column_vertical_win

            vertical_wins[x].append(row[x])

            #this appends column_vertical_win to vertical_wins


        x = x+1
    #this increases the value of x, or the value of the index, by 1




    diagonal_topleft = [board[0][0], board[1][1], board[2][2]]
    #print("diagonal_topleft, line 76", diagonal_topleft)
    diagonal_btmleft = [board[0][2], board[1][1], board[2][0]]
    #print("diagonal_btmleft, line 78", diagonal_btmleft)

    diagonal_wins = [diagonal_topleft, diagonal_btmleft]


    winner_master = []
    for row in horizontal_wins:
        winner_master.append(row)

    for column in vertical_wins:
        winner_master.append(column)

    for dgnl in diagonal_wins:
        winner_master.append(dgnl)

    for win in winner_master:
        if win[0] != blank:
            if win.count(win[0]) == len(win):
                print("line 264, winner_master", winner_master)
                print(" ")
                print(win[0], "wins!")
                break

    for i in range(3):
        print(" ")




else:
    print("Game Over! Draw")

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
