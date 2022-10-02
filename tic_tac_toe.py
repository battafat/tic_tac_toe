#
#print("X always goes first. Choose your coordinates: row, column. Ie. 2,3 would be the middle of the third column. ")

#There's a total of 9 moves.
#X always gets 5.
#O gets 4.
#I'll have the same thing repeat 4 times. And then I'll do one extra of X moves.
# for move in range(4):
row_count = 3

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



# horizontal_wins = []
#
# for row in board:
#     horizontal_wins.append(row)
#
# #print("line 51, horizontal_wins", horizontal_wins)
#
# # horizontal_1 = [list_1]
# # horizontal_2 = [list_2]
# # horizontal_3 = [list_3]
#
# vertical_wins = []
# x = 0
#
# #print("line 60, len(board): ", len(board))
#
# #See what am I trying to accomplish?
# #Then see what I think it is accomplishing.
# #Then figure out why it's not accomplishing that.
#
#
#
# for i in range(len(board)):
# #this repeats the below for loop the number of times that board is long. 3 in this case.
#     column_vertical_win = list()
#     vertical_wins.append(column_vertical_win)
#     for row in board:
#     #for each of the rows in board, so 3 times in this case. It goes to each row.
#     #        print("line 64, x value", x)
#     #    column_vertical_win.append(row[x])
#         #This appends the initial index of the row it's on to column_vertical_win
#     #        print("line 67, x value: ", x)
#         vertical_wins[x].append(row[x])
#
#         #this appends column_vertical_win to vertical_wins
#
#         print("line 71, column_vertical_win", column_vertical_win)
#         print("line 72, vertical_wins", vertical_wins)
#
#     x = x+1
# #this increases the value of x, or the value of the index, by 1
#
# print("line 73, vertical_wins", vertical_wins)
#
# #print("line 73, vertical_wins: ", vertical_wins)
#
# # lst in board:
# #     board.append(lst[0])
# # vertical_1 = [list_1[0], list_2[0], list_3[0]]
# # vertical_2 = [list_1[1], list_2[1], list_3[1]]
# # vertical_3 = [list_1[2], list_2[2], list_3[2]]
# diagonal_topleft = [board[0][0], board[1][1], board[2][2]]
# #print("diagonal_topleft, line 76", diagonal_topleft)
# diagonal_btmleft = [board[0][2], board[1][1], board[2][0]]
# #print("diagonal_btmleft, line 78", diagonal_btmleft)
#
# diagonal_wins = [diagonal_topleft, diagonal_btmleft]
#
#
# winner_master = []
# for row in horizontal_wins:
#     winner_master.append(row)
#
# for column in vertical_wins:
#     winner_master.append(column)
#
# for dgnl in diagonal_wins:
#     winner_master.append(dgnl)

#print("line, 92 winner_master: ", winner_master)




        #check which element (X or O) it contains and declare that person a winner

#I can't remember what the below line does. I think it's supposed to end the
#game by figuring out if there are no more blanks left in the board.

while blank in (item for sublist in board for item in sublist):

    for i in range(3):
        print(" ")
    x_coordinate = input("Player X, enter comma-separated integers for row and column: ")

#print(x_coordinate)

#for row in coordinates:
#    print(row)

#trying to figure out how to let the game know that all the positions have been filled.
#One option is I could figure out how to pop the spaces from a list every time an
#X or an O is played. And when the list is empty, that could mark the end.
#Or
#Maybe after each turn, it could check to see if there are any positions left that aren't
#filled with an X or an O.
#Figure out how to do this, I think.
#X always has the last turn. So I only need to end the game after X's turn.

#X's Turn:
#need a way to check if the user's input position is already taken.
#And if so, need to print "Position already filled. Please choose another."

#determining if someone won
    # for win in winner_master:
    #     if win[0] != blank:
    #         if win.count(win[0]) == len(win):
    #             print(win[0], "wins!")

    for row in coordinates:
    #    print(row)
        for x in row:
    #        print(x)
    #        print(x_coordinate)
            if x == x_coordinate:
    #    if x == x_coordinate:
                #print("found it: ", x)
                #print("Index of x: ", row.index(x))
                column_index = row.index(x)
                #print("column index: ", coordinates.index(row))
                row_index = coordinates.index(row)
    #                row[row_index] = "X"
                #here I want to replace item "x" with the letter "X"
                #I think the below line will check if the position is taken:
                if board[row_index][column_index] != blank :
                    print("Position taken. Enter new coordinates: ")
                else:
                    board[row_index][column_index] = "X"
                    print(" ")
                    for lst in board:
                        print(lst)
    #print(winner_master)
    #print("line 175, vertical wins:", vertical_wins)
    #print("line 176, diagonal_wins", diagonal_wins)
    #print("line 177, diagonal_topleft", diagonal_topleft)
                #convert the row_index, column_index to a string
                #Wait, can I make this all in terms of board?

                #determining if someone won
    # for win in winner_master:
    #     if win[0] != blank:
    #         if win.count(win[0]) == len(win):
    #             print(win[0], "wins!")
    #             break

    horizontal_wins = []

    for row in board:
        horizontal_wins.append(row)

    #print("line 51, horizontal_wins", horizontal_wins)

    # horizontal_1 = [list_1]
    # horizontal_2 = [list_2]
    # horizontal_3 = [list_3]

    vertical_wins = []
    x = 0

    #print("line 60, len(board): ", len(board))

    #See what am I trying to accomplish?
    #Then see what I think it is accomplishing.
    #Then figure out why it's not accomplishing that.



    for i in range(len(board)):
    #this repeats the below for loop the number of times that board is long. 3 in this case.
        column_vertical_win = list()
        vertical_wins.append(column_vertical_win)
        for row in board:
        #for each of the rows in board, so 3 times in this case. It goes to each row.
        #        print("line 64, x value", x)
        #    column_vertical_win.append(row[x])
            #This appends the initial index of the row it's on to column_vertical_win
        #        print("line 67, x value: ", x)
            vertical_wins[x].append(row[x])

            #this appends column_vertical_win to vertical_wins

            print("line 71, column_vertical_win", column_vertical_win)
            print("line 72, vertical_wins", vertical_wins)

        x = x+1
    #this increases the value of x, or the value of the index, by 1

    print("line 73, vertical_wins", vertical_wins)

    #print("line 73, vertical_wins: ", vertical_wins)


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


    #O's Turn:
    print(" ")
    print(" ")

    o_coordinate = input("Player O, enter comma-separated integers for row and column: ")

    #if o_coordinate not in coordinates:
    #    print("That position is not available. Please enter new coordinates.")


    for row in coordinates:

    #    print(row)
        for x in row:
    #        print(x)
    #        print(x_coordinate)
            if x == o_coordinate:

                #print("found it: ", x)
                #print("Index of x: ", row.index(x))
                column_index = row.index(x)
                #print("column index: ", coordinates.index(row))
                print(" ")
                print(" ")
                row_index = coordinates.index(row)
    #                row[row_index] = "O"
                #here I want to replace item "x" with the letter "O"
                if board[row_index][column_index] != blank :
                    print("Position taken. Enter new coordinates: ")
                    continue
                else:
                    board[row_index][column_index] = "O"
                    for lst in board:
                        print(lst)
    print("line 210, vertical_wins", vertical_wins)

    for win in winner_master:
        if win[0] != blank:
            if win.count(win[0]) == len(win):
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
