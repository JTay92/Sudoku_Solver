# This is a program that will solve instances of the Sudoku Puzzle game

board = [
    [0,4,9,0,2,0,0,0,5],
    [6,1,0,5,0,0,0,7,0],
    [3,5,0,7,0,0,1,0,9],
    [0,0,0,8,1,7,2,0,6],
    [0,7,0,0,9,0,0,0,0],
    [9,0,0,0,6,0,0,4,0],
    [1,0,3,0,0,0,6,0,0],
    [0,0,7,0,0,1,0,0,2],
    [0,0,0,0,0,0,9,0,7]
]



def draw_grid(bo):
    # Draw line break after 3 rows
    for i in range(len(bo)) : 
        if i % 3 == 0 and i != 0:
            print ("- - - - - - - - - - - - - ")

        # Draw line break after 3 columns and print values in grid
        for j in range(len(bo[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")

            if j == 8:
                print(bo[i][j])
            else:
                print(str(bo[i][j]) + " ", end="")

def find_empty(bo):
    for i in range(len(bo)):    # for each row
        for j in range(len(bo[0])): # for each col
            if bo[i][j] == 0:
                return (i, j)   # return (row, col)

draw_grid(board)
