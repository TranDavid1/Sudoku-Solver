# solver.py
# Implementation of recursively backtracking algorithm to solve a Sudoku Board

board = [
    [8,0,0,0,0,0,0,0,0],
    [0,0,3,6,0,0,0,0,0],
    [0,7,0,0,9,0,0,2,0],
    [0,5,0,0,0,7,0,0,0],
    [0,0,0,0,4,5,7,0,0],
    [0,0,0,1,0,0,0,3,0],
    [0,0,1,0,0,0,0,6,8],
    [0,0,8,5,0,0,0,1,0],
    [0,0,0,0,0,0,4,0,0]
]

def solve(bo):
    """
    Solves a sudoku board using backtracking algorithm, recursively calling on itself
    Base case of recursion: board is correctly filled out
    :param bo: Sudoku board, 2d list of ints
    :return: solution
    """


    find = find_empty(bo)
    # If there isn't an empty index, the board is completed, return True.
    if not find:
        return True
    # Otherwise, assign row and col to the index found in find_empty().
    else:
        row, col = find

    # Loop through all possible values of Sudoku board (1-9) and attempt to insert into the index
    # Iterate through 1 to 9, inclusively
    for i in range(1,10):
        # If index is valid, set the index equal to i.
        if valid(bo, i, (row, col)):
            bo[row][col] = i

            # Continue recursively running the function until the board is complete.
            if solve(bo):
                return True

            # If the inserted element isn't valid, backtrack and set the previous index to 0.
            bo[row][col] = 0

    return False


def valid(bo, num, pos):
    """
    Checks if the Sudoku board is valid given an element and board
    :param bo: Sudoku board, 2d list of ints
    :param pos: (row,col) index position in bo
    :param num: int being inserted into the position
    :return: bool
    """

    # Check row
    # Check through each element in the current row
    for i in range(len(bo[0])):
        # If any element in the row is equal to the inserted num and index being checked isn't where the num is being inserted, return false
        if bo[pos[0]][i] == num and pos[1] != i:
            return False

    # Check column
    for i in range(len(bo)):
        # If any element in the column is equal to the inserted num and index being checked isn't where the num is being inserted, return false
        if bo[i][pos[1]] == num and pos [0] != i:
            return False

    # Check which 3x3 box the position is in
    # Checks which box the index is in by multiples of 3, row 0 would be in box 0 (the first 3 rows), row 6 would be in box 2 (the last 3 rows).
    box_x = pos[1] // 3
    # Checks which box the index is in by multiples of 3, column 0 would be in box 0 (the first 3 columns), column 6 would be in box 2 (the last 3 columns).
    box_y = pos[0] // 3

    # Iterate through columns within the same 3x3 box
    for i in range(box_y*3, box_y*3 + 3):
        # Iterate through rows within the same 3x3 box
        for j in range(box_x*3, box_x*3+3):
            # If the any element in the box is the same as the newly inserted number, return false
            if bo[i][j] == num and (i,j) != pos:
                return False

    return True


def print_board(bo):
    """
    displays the Sudoku board
    :param bo: Sudoku board, a 2d list of ints
    :return: none
    """

    # For loop iterating through all rows of board
    for i in range(len(bo)):
        # Every 3 rows, print out a horizontal line
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - - -")

        # For loop iterating through all columns of boards
        for j in range(len(bo[0])):
            # Every 3 rows, print out a vertical line
            if j % 3 == 0 and j != 0:
                print(" | ", end="")

            # If we're at the last column
            if j == 8:
                print(bo[i][j])
            # Else print out the element and space
            else:
                print(str(bo[i][j]) + " ", end="")


def find_empty(bo):
    """
    finds an empty index in the Sudoku board, empty index has value of 0
    :param bo: partially complete board
    :return: (int, int): index where (row, col)
    """

    # Iterate through rows of board
    for i in range(len(bo)):
        #iterate through columns of board
        for j in range(len(bo[0])):
            if bo[i][j] == 0:
                # row, col
                return (i,j)

    #If there are no empty indexes, return None
    return None


print("Unsolved Sudoku board:\n")
print("_______________________\n")
print_board(board)
solve(board)
print("\n\nSolved Sudoku board:")
print("_______________________\n")
print_board(board)
