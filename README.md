# Sudoku_game_-generator
It can ether take in nothing and will randomly generate a new sudoku board every time that follows  all the rules and will also return the same board with numbers missing so user can try to solve the board.  It can also take in a sudoku board orm the user and print out the solved version  input: grid can be a 2-D matrix of a Sudoku puzzle  to solve, or None to generate a new puzzle. Return: complete solution and puzzel version.
README.txt
--->This exspains how to run my Sudoku python file

input: grid can be a 2-D matrix of a Sudoku puzzle 
to solve, or None to generate a new puzzle.
Return: compleat colution and puzzel version.
So first run the code then in the concole you can call
sudokuGenerator() or sudokuGenerator(None)
both work
----example of what will come out---
sudokuGenerator()
This is the full solution
[3, 4, 5, 7, 8, 1, 9, 6, 2]
[9, 1, 2, 3, 4, 6, 8, 7, 5]
[7, 6, 8, 9, 2, 5, 1, 4, 3]
[6, 2, 3, 5, 7, 9, 4, 1, 8]
[5, 8, 7, 2, 1, 4, 6, 3, 9]
[1, 9, 4, 8, 6, 3, 5, 2, 7]
[2, 5, 6, 1, 9, 7, 3, 8, 4]
[4, 7, 9, 6, 3, 8, 2, 5, 1]
[8, 3, 1, 4, 5, 2, 7, 9, 6]
The sudoku with removed numbers
[0, 4, 0, 0, 0, 0, 0, 0, 0]
[9, 1, 0, 0, 4, 0, 0, 0, 5]
[7, 0, 8, 9, 2, 0, 0, 4, 3]
[6, 2, 0, 0, 0, 9, 4, 0, 8]
[0, 8, 0, 0, 0, 0, 6, 3, 0]
[0, 9, 0, 0, 6, 3, 0, 0, 0]
[0, 0, 0, 1, 0, 0, 0, 0, 0]
[4, 7, 9, 0, 0, 0, 0, 5, 0]
[0, 0, 0, 4, 5, 0, 7, 9, 0]
Out[3]: <__main__.sudokuGenerator at 0x1c413ddc9a0>

Once its called it will run and generate a compleate sudoku board solution and then 
it will also return a nother version of that smae board but it will have some mubers 
shuffled and replaced with 0's. for the user to inpute there own board they must 
first run the program.
Then in the concole set there unsolves sudoku grid this is an example one
 grid = [
            [5, 3, 0, 0, 7, 0, 0, 0, 0],
            [6, 0, 0, 1, 9, 5, 0, 0, 0],
            [0, 9, 8, 0, 0, 0, 0, 6, 0],
            [8, 0, 0, 0, 6, 0, 0, 0, 3],
            [4, 0, 0, 8, 0, 3, 0, 0, 1],
            [7, 0, 0, 0, 2, 0, 0, 0, 6],
            [0, 6, 0, 0, 0, 0, 2, 8, 0],
            [0, 0, 0, 4, 1, 9, 0, 0, 5],
            [0, 0, 0, 0, 8, 0, 0, 7, 9]
        ]
Then ender into the concole
solved=sudokuGenerator(grid)
or you can enter just sudokuGenerator(grid) as long as you have still 
defined the grid befor.
So if you set it = to solved this is is setting the variable solved as the solution 
to the grid the user just entered as its called in the function so
 its this is making the program solve the grid so the function solveInputSudoku() 
will be called and generate the solution for the grid entered by the user.
Then the user must put in the console.

for row in solved.grid:

     print(row)

This is basically say to print each row of the new solved grid variable which will
basically make it print out the solution row by row.           

For the sudokuGenerater() parameter you can basically enter it with empty 
parentheses or sudokuGenerater(None) both work for making it generate a new solution
everything else will cause an error

---------------------------------------------
--->>>known circumstances which causes it to crash. or bug out.


For the sudokuGenerater() parameter you can basically enter it with empty 
parentheses or sudokuGenerater(None) both work for making it generate a new solution
everything else will cause an error
For the user inputted one the user first has to always enter or assine a grid
and that grid can only contain numbers not letters however there is a bug that 
parts can contain numbers greater the 0-9 example setting parts in the grid to
already have those numbers 
grid = [
    [5, 34, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 33, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 000, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]
solved=sudokuGenerator(grid)

for row in solved.grid:
    print(row)
    
[5, 34, 4, 3, 7, 6, 9, 1, 2]
[6, 7, 2, 1, 9, 5, 3, 4, 8]
[1, 9, 33, 2, 4, 8, 5, 6, 7]
[8, 5, 9, 7, 6, 1, 4, 2, 3]
[4, 2, 6, 8, 5, 3, 7, 9, 1]
[7, 1, 3, 9, 2, 4, 8, 5, 6]
[9, 6, 1, 5, 3, 7, 2, 8, 4]
[2, 8, 7, 4, 1, 9, 6, 3, 5]
[3, 4, 5, 6, 8, 2, 1, 7, 9]
As you can see testing 34 and 33 and 000 the 000 it will still solve as its
 just reading it as 0 for the others I believe its not truly reading them 
as the 33 is were the 8 for that row and collom should be but its just ignoring it 
and leaving it there but its also not putting any extras 8s anywhere. So the
program is wrong but doesn't crash.



-----------------------------------

--->>>>Any additional python modules in project list her module
No installed additional Anaconda Python modules only ones we already had in spyder
from random import shuffle
import copy
