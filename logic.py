#logic.py to be import int 2048.py file

#importing random package for mtehods to generate random numbers
import random

#function to initialize game/grid at the start of the game
def start_game():

    #declaring an empty list then appending 4 list each with four elements as 0
    mat=[]
    for i in range(4):
        mat.append([0]*4)
    
    #printing controls for users
    print("commands as follows")
    print("'W' or 'w' : Move Up")
    print("'S' or 's' : Move Down")
    print("'A' or 'a' : Move Left")
    print("'D' or 'd' : Move Right")

    #call a function to add a new 2 in grid after every step
    add_new_2(mat)
    return mat
#function 2 add a new 2 in grid at random emty cell
def add_new_2(mat):

    #choose a random indexfor row and column
    r = random.randint(0,3)
    c = random.randint(0,3)

    #while loop will break as the random cell chosen will be empty (or contains 0)
    while(mat[r][c] != 0):
        r = random.randint(0,3)
        c = random.randint(0,3)

    #we will place a 2 at that empty cell
    mat[r][c] = 2

#function to get the current state
def get_current_state(mat):

    #if any cells contian 2048 trigger win
    for i in range(4):
        for j in range(4):
            if(mat[i][j] == 2048):
                return 'WON'
    
    #if we are still left with a least on empty cell  game is not over
    for i in range(4):
        for j in range(4):
            if(mat[i][j] == 0):
                return 'GAME NOT OVER'
    #or if no cell is empty now but if after any move lef, right, up, down, if any 2 cells gets
    # merged and creates an empty cell than game is not over yet
    for i in range(3):
        for j in range(3):
            if (mat[i][j] == mat[i+1][j] or mat[i][j] == mat[i][j+1]):
                return 'GAME NOT OVER'
            
    for j in range(3):
        if(mat[3][j] == mat[3][j+1]):
            return 'GAME NOT OVER'
        
    for i in range(3):
        if(mat[i][3] == mat[i+1][3]):
            return 'GAME NOT OVER'
     
     #else we have lost the game
    return 'LOST'

#all the functions defined below are for left swap initially

#function to compress grid after every step before and after merging cells
def compress(mat):

    #bool variable to determine if any change happen or not
    changed = False

    #empty grid
    new_mat = []

    #with all the cells empty
    for i in range(4):
        new_mat.append([0]*4)
    
    #here we will shift entries of each cell to it's extreme left row by row loop to transverse
    #rows
    for i in range(4):
        pos = 0

        #loop to transverse columns in respective row
        for j in range(4):
            if(mat[i][j] != 0):
                
                #if cell is not empty then we  will shift it's number previous empty cell in that
                # rowdenotated by pos varibale
                new_mat[i][pos] = mat[i][j]

                if(j != pos):
                    changed =True
                pos += 1
    
    #returning new compressed matrix and the flag variable
    return new_mat, changed

# function to merge the cells in matrix after compressing
def merge(mat):
    
    changed = False

    for i in range(4):
        for j in range(3):

            #if current cell has same value as next cell inthe row and they are not empty then
            if(mat[i][j] == mat[i][j+1] and mat[i][j] != 0):

                #double current cell value and empty the next cell
                mat[i][j] = mat[i][j] * 2
                mat[i][j+1] = 0

                #make bool variable true indicating the new grid after merging is different
                changed = True

    return mat, changed

#function to reverse the matrix reversing  the content of each row (reversing the sequence)
def reverse(mat):
    new_mat = []
    for i in range(4):
        new_mat.append([])
        for j in range(4):
            new_mat[i].append(mat[i][3-j])
    return new_mat

#function to get the transpose of matrix means interchanging rows and columns
def transpose(mat):
    new_mat = []
    for i in range(4):
        new_mat.append([])
        for j in range(4):
            new_mat[i].append(mat[j][i])
    return new_mat

#functions to update the matrix

#function to move/swipe right
def move_left(grid):

    #firt we compress the grid
    new_grid, changed1 = compress(grid)

    #then merge cells
    new_grid, changed2 = merge(new_grid)

    changed = changed1 or changed2

    #again compress after merging
    new_grid, temp = compress(new_grid)

    #return new matrix and bool changed telling whether the grid is the same or different
    return new_grid, changed

#fucntion to move/ swipe right
def move_right(grid):

    #reverse the matrix
    new_grid = reverse(grid)

    #then move left
    new_grid, changed = move_left(new_grid)

    #reverse the matrix agian
    new_grid = reverse(new_grid)
    return new_grid, changed

#function to move/swipe up
def move_up(grid):

    #first transpose the matrix
    new_grid = transpose(grid)

    #then move left
    new_grid, changed = move_left(new_grid)

    #transpose again
    new_grid = transpose(new_grid)
    return new_grid, changed

#function to move grid down
def move_down(grid):

    #first transpose
    new_grid = transpose(grid)

    #then move right
    new_grid, changed = move_right(new_grid)

    #then transpose again
    new_grid = transpose(new_grid)
    return new_grid, changed

#this file only contains all the logic functions to be called in the main function present in the
#other file