"""
@author: beatr
Beatrice Archer 
Professor Davis 
12/15/2022
SudokuGenerator
It can ether take in nothing and will randomly gereate a new sudoku board every time that follows
 all the rules and will also return the same board with numbers missing so user can try to solve the board.
 It can also take in a sudoku board orm the user and print out the solved version 

input: grid can be a 2-D matrix of a Sudoku puzzle 
to solve, or None to generate a new puzzle.
Return: compleat colution and puzzel version.


Citations to:
Shoutout to all these that helped with the code 
    Professor Davis example problems we had previously done in class
    Talk about a sudoku solver and generator https://codereview.stackexchange.com/questions/268007/sudoku-solver-and-generator-in-python
    (He has three posts I read through but I just linked the first one)Kush and his work on medium https://medium.com/codex/building-a-sudoku-solver-and-generator-in-python-1-3-f29d3ede6b23
    On Youtube Goldblade how to make a sudoku generator https://www.youtube.com/watch?v=YHvQ-Y2MXDI
    on youtube HackerShrine build your own Sudoku player in python https://www.youtube.com/watch?v=I2lOwRiGNy4
    Christinas artical online about Sudoku puzzles with Python and how to implement the rules https://lvngd.com/blog/generating-and-solving-sudoku-puzzles-python/
    THis was for the shuffle https://www.w3schools.com/python/ref_random_shuffle.asp
    exspaining backtacking https://leetcode.com/problems/unique-paths-iii/solutions/1535158/Python-Backtracking:-Easy-to-understand-with-Explanation/
    reading through how they did the  sudoku gamehttps://data-flair.training/blogs/python-sudoku-game/
    Chapter 9.5 of the textbook 
"""
 
from random import shuffle
import copy

class sudokuGenerator:
    """generates and solves Sudoku puzzle grids using a backtracking algorithm"""
    
    def __init__(self,grid=None):
        self.counter = 0
       
        self.path = []
        #if a grid is passed in, make a copy and solve it
        if grid:
            if len(grid[0]) == 9 and len(grid) == 9:
                self.grid = grid
                self.original = copy.deepcopy(grid)
                self.solveInputSudoku()
            else:
                print("input needs to be a 9x9 matrix")
        else:
            #if user does not enter passed, generate one
            self.grid = [[0 for i in range(9)] for j in range(9)]
            self.generatePuzzle()
            self.original = copy.deepcopy(self.grid)
        
    def generatePuzzle(self):

        """generates a new puzzle and solves it"""
        
        self.generateSol(self.grid)
        self.printGrid('This is the full solution')
        self.removeNumFromGrid()
        self.printGrid('The sudoku with removed numbers')
        return
    
    
    def printGrid(self, gridName=None):
        """prints the grid by row"""
        if gridName:
            print(gridName)
        for row in self.grid:
            print(row)
        return

    def testPuzzle(self,grid):
        """tests each square by looking through the rows and colums to make sure it is a valid puzzle"""
        for row in range(9):
            for col in range(9):
                num = grid[row][col]
                #remove the number from grid to test if it's valid
                grid[row][col] = 0
                if not self.wrongLocation(grid,row,col,num):
                    return False
                else:
                    #put the number back in grid
                    grid[row][col] = num
        return True

    def numInRow(self,grid,row,number):
        
        """returns True if the number has been used in that row"""
        
        if number in grid[row]:
            return True
        
        return False

    def numInColumn(self,grid,col,number):
        """returns True if the number has been used in that column"""
        
        for i in range(9):
            if grid[i][col] == number:
                return True
        return False

    def numInSubgrid(self,grid,row,col,number):
        """returns True if the number has been used in that subgrid/box"""
        
        subgridRow = (row // 3) * 3
        subgridCol = (col // 3)  * 3
        
        for i in range(subgridRow, (subgridRow + 3)): 
            for j in range(subgridCol, (subgridCol + 3)): 
                if grid[i][j] == number: 
                    return True
        return False

    def wrongLocation(self,grid,row,col,number):
        """return False if the number has been used in the row, column or subgrid"""
        
        if self.numInRow(grid, row,number):
            return False
        elif self.numInColumn(grid,col,number):
            return False
        elif self.numInSubgrid(grid,row,col,number):
            return False
        return True

    def nextEmptySquare(self,grid):
        """return the next empty square coordinates in the grid"""
        
        for i in range(9):
            for j in range(9):
                if grid[i][j] == 0:
                    return (i,j)
        return

    def solvePuzzle(self, grid):
        """solve the sudoku puzzle with backtracking"""
        
        for i in range(0,81):
            row=i//9
            col=i%9
            
            #find the  next empty cell
            if grid[row][col]==0:
                
                for number in range(1,10):
                    
                    #check that the number hasn't already been used in a row/col/subgrid
                    if self.wrongLocation(grid,row,col,number):
                        grid[row][col]=number
                        if not self.nextEmptySquare(grid):
                            self.counter+=1
                            break
                        else:
                            if self.solvePuzzle(grid):
                                return True
                break
        grid[row][col]=0  
        return False

    def generateSol(self, grid):
        """generates a full solution with backtracking"""
        
        numberList = [1,2,3,4,5,6,7,8,9]
        
        for i in range(0,81):
            row=i//9
            col=i%9
            #find the next empty cell
            
            if grid[row][col]==0:
                shuffle(numberList)      
                for number in numberList:
                    
                    if self.wrongLocation(grid,row,col,number):
                        self.path.append((number,row,col))
                        grid[row][col]=number
                        if not self.nextEmptySquare(grid):
                            return True
                        else:
                            if self.generateSol(grid):
                                #if the grid is full
                                return True
                break
        grid[row][col]=0  
        return False

    def getNonEmptySquares(self,grid):
        """returns a shuffled list of non-empty squares in the puzzle"""
        
        nonEmptySquares = []
        for i in range(len(grid)):
            for j in range(len(grid)):
                if grid[i][j] != 0:
                    nonEmptySquares.append((i,j))
                    
        shuffle(nonEmptySquares)
        return nonEmptySquares

    def removeNumFromGrid(self):
        """remove numbers from the grid to create the puzzle"""
        
        #get all non-empty squares from the grid
        nonEmptySquares = self.getNonEmptySquares(self.grid)
        nonEmptySquaresCount = len(nonEmptySquares)
        rounds = 3
        while rounds > 0 and nonEmptySquaresCount >= 17:
            #there should be at least 17 clues for it to only have one solution
            row,col = nonEmptySquares.pop()
            nonEmptySquaresCount -= 1
            #might need to put the square value back if there is more than one solution
            removedSquare = self.grid[row][col]
            self.grid[row][col]=0
            #make a copy of the grid to solve
            copyOfGrid = copy.deepcopy(self.grid)
            #initialize solutions counter to zero
            self.counter=0      
            self.solvePuzzle(copyOfGrid)   
            #if there is more than one solution, put the last removed cell back into the grid
            if self.counter!=1:
                self.grid[row][col]=removedSquare
                nonEmptySquaresCount += 1
                rounds -=1
        return
    
    def solveInputSudoku(self):
        """solves a puzzle inputed as grid"""
        self.generateSol(self.grid)
        return
