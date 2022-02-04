import random
import time
random.seed(time.time())

board = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0]
]



def resetBoard(board):
    for i in range(len(board[0])):
        for j in range(len(board)):
            board[i][j] = 0
    return board



def solve(board):
    find = findEmpty(board)
    if not find:
        return True
    else:
        row, col = find

    for i in range(1,10):
        if isValid(board, i, (row, col)):
            board[row][col] = i # add into the board
            # recursively try finish solution
            # if we cant solve board then we reset that value
            if solve(board):
                return True
            # Backtracks if the above if doesnt return True
            board[row][col] = 0
    return False



def isValid (board, num, pos):
    # For each row check columns
    for i in range(len(board[0])):
        if board[pos[0]][i] == num and pos[1] != i:
            return False

    # For each columns check the rows
    for i in range(len(board)):
        if board[i][pos[1]] == num and pos[0] != i:
            return False

    # Check box
    xBox = (pos[1] // 3) * 3
    yBox = (pos[0] // 3) * 3

    for i in range(yBox, yBox + 3):
        for j in range(xBox, xBox + 3):
            if board[i][j] == num and (i,j) != pos:
                return False
    return True



def findEmpty(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 0:
                return (i, j) # row, col
    return None



def printBoard(board):
    # Row of board, Length of Board is a list
    for i in range(len(board)):
        if i % 3 == 0 and i != 0:
            print("-----------------------")
        # Column of board, Length of each row
        for j in range(len(board[0])):
            # on every third number you will print |
            # print ( , end="") means you can on printin in same line
            if j % 3 == 0 and j != 0:
                print(" | ", end="")
            # on the last column of the row Board[i][8]. It will print new line
            if j == 8:
                print(board[i][j], end= "\n")
            else:
                print(str(board[i][j]) + " ", end="")


def mutate(board):
    # Reverse board. from top to down is from down to top
    # print("BEFORE")
    # printBoard(board)
    # board.reverse()

    numberList = [1,2,3,4,5,6,7,8,9]
    while len(numberList) > 1:
        swapNumber1 = random.choice(numberList)
        swapNumber2 = random.choice(numberList)

        if swapNumber1 in numberList and swapNumber2 in numberList and swapNumber1 != swapNumber2:
            numberList.remove(swapNumber1)
            numberList.remove(swapNumber2)
            output = f"swapNumber1 is {swapNumber1} and swapNumber2 is {swapNumber2}"
            #print (output)

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == swapNumber1:
                    board[i][j] = swapNumber2
                elif board[i][j] == swapNumber2:
                    board[i][j] = swapNumber1


def generatePuzzle(board):
    row = random.randint(0, len(board[0]) - 1)
    col = random.randint(0, len(board) - 1)
    num = random.randint(1, 9)
    output = f"row is {row}, column is {col} and random number is {num}"
    #print (output)
    # makes a 'random' puzzle
    board[row][col] = num
    solve(board)
    # print("First board")
    # printBoard(board)
    mutate(board)
    # print("Mutated board")
    # printBoard(board)

    #Fill it with Empty Zeroes
    emptyCubes = random.randint(40, 60)
    while emptyCubes > 0:
        row1 = random.randint(0, len(board[0]) - 1)
        col1 = random.randint(0, len(board) - 1)
        if board[row1][col1] != 0:
            board [row1][col1] = 0
            emptyCubes = emptyCubes - 1
    return board



def main (board):
    run = True
    print("Welcome to the Sudoku Puzzle")
    while run:
        action = input("Press (1) for a new puzzle, (2) to solve it or (3) to quit \n")
        if action == '1':
            resetBoard(board)
            generatePuzzle(board)
            printBoard(board)
        elif action == '2':
            solve(board)
            printBoard(board)
        elif action == '3':
            run = False
        else:
            run = False

if __name__ == "__main__":
    main(board)
