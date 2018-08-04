import queue as q
import numpy as np

array = [
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,3,0,8,5],
    [0,0,1,0,2,0,0,0,0],
    [0,0,0,5,0,7,0,0,0],
    [0,0,4,0,0,0,1,0,0],
    [0,9,0,0,0,0,0,0,0],
    [5,0,0,0,0,0,0,7,3],
    [0,0,2,0,1,0,0,0,0],
    [0,0,0,0,4,0,0,0,9]
]


# sudoku = []


# for i in range(9):
#     sudoku.append([])
#     for j in range(9):
#         if array[(i+1)*(j+1)-1] == 0:
#             sudoku[i].append([1,2,3,4,5,6,7,8,9])
#         else:
#             sudoku[i].append(array[(i+1)*(j+1)-1])
#
def empty(sudoku):
    for i in range(9):
        for j in range(9):
            if(sudoku[i][j]==0):
                return (i,j)
    return False

def printarray(sudoku):
    for i in range(9):
        print(sudoku[i])

def rows(sudoku,row,val):
    for i in range(9):
        if(sudoku[row][i] == val):
            return False
    return True

def columns(sudoku,col,val):
    for i in range(9):
        if(sudoku[i][col] == val):
            return False
    return True

def sections(sudoku,row,col,val):
    row = row - row%3
    col = col - col%3
    for i in range(3):
        for j in range(3):
            if(sudoku[row+i][col+j] == val):
                return False
    return True

def completeSudoku(sudoku):
    point = empty(sudoku)
    if(not point):
        printarray(sudoku)
        return True
    row  = point[0]
    col = point[1]
    for i in range(1,10):
        if(rows(sudoku,row,i) and columns(sudoku,col,i) and sections(sudoku,row,col,i)):
            sudoku[row][col] = i
            result = completeSudoku(sudoku)
            if(result):
                return True
            sudoku[row][col] = 0
    return False

boom = completeSudoku(array)
print(boom)
