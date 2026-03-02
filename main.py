import random
import numpy

def sudoku_solver(sudoku):
    """
    Solves a Sudoku puzzle and returns its unique solution.

    Input
        sudoku : 9x9 numpy array
            Empty cells are designated by 0.

    Output
        9x9 numpy array of integers
            It contains the solution, if there is one. If there is no solution, all array entries should be -1.
    """

    puzzle = np.array(sudoku, dtype=int)
    
    def checkNum(puzzle, row, col, val):
        #check row
        for j in range(9):
            if j != col and puzzle[row, j] == val:
                return False
    
        #check column
        for i in range(9):
            if i != row and puzzle[i, col] == val:
                return False

        #check square
        start_row = (row // 3) * 3
        start_col = (col // 3) * 3
        
        for i in range(0,3):
            for j in range(0,3):
                r = start_row + i
                c = start_col + j
                if (r != row or c != col) and puzzle[r, c] == val:  # FIXED: Changed 'and' to 'or'
                    return False
        
        return True


    def preSolutionCheck(puzzle):
        for i in range(0,9):
            for j in range(0,9):
                if puzzle[i, j] != 0:
                    if not checkNum(puzzle, i, j, puzzle[i, j]):
                        return False  
        return True

    def countOptions(puzzle, row, col):
        count = 0
        for num in range(1, 10):
            if checkNum(puzzle, row, col, num):
                count += 1
        return count
    
    def minOptionCell(puzzle):
        minOptions = 10
        best = None
        
        for i in range(0,9):
            for j in range(0,9):
                if puzzle[i, j] == 0:
                    options = countOptions(puzzle, i, j)
                    if options < minOptions:
                        minOptions = options
                        best = (i, j)
                        if minOptions == 1: 
                            return best
        return best
    
    def solve(puzzle):
        cell = minOptionCell(puzzle)
        if cell is None:
            return True #exit loop once solution found
        row, col = cell
        valid = []
        for num in range(1, 10):
            if checkNum(puzzle, row, col, num):
                valid.append(num)
        random.shuffle(valid)
        for num in valid:
            puzzle[row, col] = num
            if solve(puzzle):
                return True #upwards feedback
            puzzle[row, col] = 0 #backtrack
        return False #no solution - causes backtrack
    
    if not preSolutionCheck(puzzle):
        return np.full((9, 9), -1, dtype=int)

    if solve(puzzle):
        return puzzle
    else:
        return np.full((9, 9), -1, dtype=int)
