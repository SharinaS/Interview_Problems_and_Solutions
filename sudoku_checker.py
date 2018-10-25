'''
Created on Apr 7, 2018

@author: sharina

FROM CODEFIGHTS

Sudoku is a number-placement puzzle. The objective is to fill a 9 × 9 grid with numbers in such a way that each column, each row, 
and each of the nine 3 × 3 sub-grids that compose the grid all contain all of the numbers from 1 to 9 one time.

Implement an algorithm that will check whether the given grid of numbers represents a valid Sudoku puzzle according to the layout 
rules described above. Note that the puzzle represented by grid does not have to be solvable.

grid = [['.', '.', '.', '1', '4', '.', '.', '2', '.'],
        ['.', '.', '6', '.', '.', '.', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.', '.', '.', '.'],
        ['.', '.', '1', '.', '.', '.', '.', '.', '.'],
        ['.', '6', '7', '.', '.', '.', '.', '.', '9'],
        ['.', '.', '.', '.', '.', '.', '8', '1', '.'],
        ['.', '3', '.', '.', '.', '.', '.', '.', '6'],
        ['.', '.', '.', '.', '.', '7', '.', '.', '.'],
        ['.', '.', '.', '5', '.', '.', '.', '7', '.']]
        
    Output should be True (follows sudoko rules)
    
grid = [['.', '.', '.', '.', '2', '.', '.', '9', '.'],
        ['.', '.', '.', '.', '6', '.', '.', '.', '.'],
        ['7', '1', '.', '.', '7', '5', '.', '.', '.'],
        ['.', '7', '.', '.', '.', '.', '.', '.', '.'],
        ['.', '.', '.', '.', '8', '3', '.', '.', '.'],
        ['.', '.', '8', '.', '.', '7', '.', '6', '.'],
        ['.', '.', '.', '.', '.', '2', '.', '.', '.'],
        ['.', '1', '.', '2', '.', '.', '.', '.', '.'],
        ['.', '2', '.', '.', '3', '.', '.', '.', '.']]
    
    Output should be False (There are two 1's in the second column)
    
#######
Thoughts:
1. Sets prevent duplication
2. Muliple functions could be used to check rows, columns and the 3x3 grid
3. There are multiple periods, careful to ignore those, by only checking numbers/integers
4. 3x3 sub-grids: Use % to divide up row into 3s...? and then compare to a set to check for duplicates within 3x3 sub-grid....

#######
'''
grid = [['.', '.', '.', '1', '4', '.', '.', '2', '.'],
        ['.', '.', '6', '.', '.', '.', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.', '.', '.', '.'],
        ['.', '.', '1', '.', '.', '.', '.', '.', '.'],
        ['.', '6', '7', '.', '.', '.', '.', '.', '9'],
        ['.', '.', '.', '.', '.', '.', '8', '1', '.'],
        ['.', '3', '.', '.', '.', '.', '.', '.', '6'],
        ['.', '.', '.', '.', '.', '7', '.', '.', '.'],
        ['.', '.', '.', '5', '.', '.', '.', '7', '.']]
# print(grid[1][2])
# 6

'''
1.) Create a function called dot_free_rows that takes each row in the grid and removes the dots.
2.) Create a function called row_checker that counts the number of times each element occurs in each row. Note that if you put the code that removes the dots
into the function that counts the number of times an element appears, you will be counting the number of elements for the entire grid as a whole, not 
each row individually. You have to have the function row_checker inherit dot_free_rows, so that row_checker will analzye each row that is passed in from dot_free_rows 
before moving onto the next. 
3.) Make sure to indicate in the dot_free_rows function that it is to produce an output from row_checker. So, grid is put into dot_free_rows, which makes grid into
a bunch of rows that are dot-free, but as it's doing so, it's sending that code into the function row_checker. This counts the number of occurrences of elements in 
each row, then evaluates to either True or False depending on if there are more than 1 of each element in each row. If at any point the function row_checker
becomes False, function dot_free_rows says to break out of the program, and output that result. Otherwise, it ends up outputting True, since nothing made the 
code stop the loops.


EUREKA!
>>>>> "If not" statement: <<<<<<
Example:
def foo(bar = None):
    if not bar:
        bar = 2
if not bar: will execute if bar is any kind of zero or empty container, or False. Many people do use not bar where they really do mean bar is not None.

>>>>> These say the same thing from function row_checker: <<<<<
for i in order_keeper:
        if dict_counter[i] > 1:
            sudoku_checker = False
if dict_counter[max(dict_counter, key=dict_counter.get)] > 1:
    sudoku_checker = False

'''    

####### CODE THAT ONLY WORKS TO IDENTIFY WHETHER ROWS IN THE SUDOKU GRID PASS OR FAIL: ###########
#===============================================================================
# def row_checker(dot_free_rows):
#     dict_counter = {}
#     order_keeper = []
#     sudoku_checker = True
#             
#     if len(dot_free_rows) > 0:  
#                
#         for i in dot_free_rows:
#             if i in dict_counter:
#                 dict_counter[i] += 1
#                 print(dict_counter)
#             else:
#                 dict_counter[i] = 1
#                 order_keeper.append(i)
#        
#     for i in order_keeper:
#         if dict_counter[i] > 1:
#             sudoku_checker = False
#       
#     return sudoku_checker
# 
# 
# def dot_free_rows(grid):
#         
#     for i in range(len(grid)):       
#         dot_free_rows = [int(j) for j in grid[i] if j != '.']
#         
#         if row_checker(dot_free_rows) == False:
#             break
#      
#     return row_checker(dot_free_rows)
#    
# print(dot_free_rows([
#         ['.', '.', '1', '.', '4', '.', '.', '2', '.'],
#         ['.', '.', '6', '.', '.', '.', '.', '.', '.'],
#         ['.', '.', '.', '.', '.', '.', '.', '.', '.'],
#         ['.', '.', '1', '.', '.', '.', '.', '.', '.'],
#         ['.', '6', '7', '.', '.', '.', '.', '.', '9'],
#         ['.', '.', '.', '.', '.', '.', '8', '1', '.'],
#         ['.', '3', '.', '.', '.', '.', '.', '.', '6'],
#         ['.', '.', '.', '.', '7', '.', '.', '.', '.'],
#         ['.', '.', '.', '5', '.', '2', '.', '7', '.']]))        
#===============================================================================

####### STEP 2: CODE THAT IDENTIFIES WHETHER ROWS AND COLUMNS IN THE SUDOKU GRID PASS OR FAIL: ###########
#===============================================================================
# def row_checker(dot_free_rows):
#     dict_counter = {}
#     order_keeper = []
#     sudoku_checker = True
#             
#     if len(dot_free_rows) > 0:  
#                
#         for i in dot_free_rows:
#             if i in dict_counter:
#                 dict_counter[i] += 1
#                 print(dict_counter)
#             else:
#                 dict_counter[i] = 1
#                 order_keeper.append(i)
#        
#     for i in order_keeper:
#         if dict_counter[i] > 1:
#             sudoku_checker = False
#       
#     return sudoku_checker
# 
# 
# def dot_free_rows(grid):
#         
#     for i in range(len(grid)):       
#         dot_free_rows = [int(j) for j in grid[i] if j != '.']
#         
#         if row_checker(dot_free_rows) == False:
#             break
#      
#     return row_checker(dot_free_rows)
# 
# def sudoku_body(grid):
#     
#     rows_are_good = dot_free_rows(grid)
#     columns_are_good = dot_free_rows(list(zip(*grid)))
#     
#     if rows_are_good and columns_are_good == True:
#         return True
#     else:
#         return False
#    
# print(sudoku_body([
#         ['.', '.', '1', '.', '4', '.', '.', '2', '.'],
#         ['.', '.', '6', '.', '.', '.', '.', '.', '.'],
#         ['.', '.', '.', '.', '.', '.', '.', '.', '.'],
#         ['.', '.', '.', '.', '.', '.', '.', '.', '.'],
#         ['.', '6', '7', '.', '.', '.', '.', '.', '9'],
#         ['.', '.', '.', '.', '.', '.', '8', '1', '.'],
#         ['.', '3', '.', '.', '.', '.', '.', '.', '6'],
#         ['.', '.', '.', '.', '7', '.', '.', '.', '.'],
#         ['.', '.', '.', '5', '.', '2', '.', '7', '.']]))        
#===============================================================================

########################

def row_checker(dot_free_rows):
    dict_counter = {}
    order_keeper = []
    sudoku_checker = True
            
    if len(dot_free_rows) > 0:  
               
        for i in dot_free_rows:
            if i in dict_counter:
                dict_counter[i] += 1
                print(dict_counter)
            else:
                dict_counter[i] = 1
                order_keeper.append(i)
       
    for i in order_keeper:
        if dict_counter[i] > 1:
            sudoku_checker = False
      
    return sudoku_checker


def dot_free_rows(grid):
        
    for i in range(len(grid)):       
        dot_free_rows = [int(j) for j in grid[i] if j != '.']
        
        if row_checker(dot_free_rows) == False:
            break
     
    return row_checker(dot_free_rows)

def sudoku_body(grid):
    
    rows_status= dot_free_rows(grid)
    columns_status = dot_free_rows(list(zip(*grid)))
    
    # Next, write code to identify 3x3 sub-grids.
    # [start, stop, step] will separate the columns
    for i in range (0, len(grid), 3): # 0  3  6
        sub_grid = grid[i:i+3]
        #print(sub_grid)

# [['.', '.', '1', '.', '4', '.', '.', '2', '.'], ['.', '.', '6', '.', '.', '.', '.', '.', '.'], ['.', '.', '.', '.', '.', '.', '.', '.', '.']]
# [['.', '.', '.', '.', '.', '.', '.', '.', '.'], ['.', '6', '7', '.', '.', '.', '.', '.', '9'], ['.', '.', '.', '.', '.', '.', '8', '1', '.']]
# [['.', '3', '.', '.', '.', '.', '.', '.', '6'], ['.', '.', '.', '.', '7', '.', '.', '.', '.'], ['.', '.', '.', '5', '.', '2', '.', '7', '.']]

        
        for j in range(0,len(grid[0]),3):
            tmp_grid = [x[j:j+3] for x in sub_grid]
            #print(tmp_grid)

# [['.', '.', '1'], ['.', '.', '6'], ['.', '.', '.']]
# [['.', '4', '.'], ['.', '.', '.'], ['.', '.', '.']]
# [['.', '2', '.'], ['.', '.', '.'], ['.', '.', '.']]
# [['.', '.', '.'], ['.', '6', '7'], ['.', '.', '.']]
# [['.', '.', '.'], ['.', '.', '.'], ['.', '.', '.']]
# [['.', '.', '.'], ['.', '.', '9'], ['8', '1', '.']]
# [['.', '3', '.'], ['.', '.', '.'], ['.', '.', '.']]
# [['.', '.', '.'], ['.', '7', '.'], ['5', '.', '2']]
# [['.', '.', '6'], ['.', '.', '.'], ['.', '7', '.']]

            new_tmp_grid = [tmp_grid[k][l] for k in range(len(tmp_grid)) for l in range(len(tmp_grid[k]))]
            #print(new_tmp_grid)
            
# ['.', '.', '1', '.', '.', '6', '.', '.', '.']
# ['.', '4', '.', '.', '.', '.', '.', '.', '.']
# ['.', '2', '.', '.', '.', '.', '.', '.', '.']
# ['.', '.', '.', '.', '6', '7', '.', '.', '.']
# ['.', '.', '.', '.', '.', '.', '.', '.', '.']
# ['.', '.', '.', '.', '.', '9', '8', '1', '.']
# ['.', '3', '.', '.', '.', '.', '.', '.', '.']
# ['.', '.', '.', '.', '7', '.', '5', '.', '2']
# ['.', '.', '6', '.', '.', '.', '.', '7', '.']

            clean_row = [x for x in new_tmp_grid if x != '.']
            #print(clean_row)
            
# ['1', '6']
# ['4']
# ['2']
# ['6', '7']
# []
# ['9', '8', '1']
# ['3']
# ['7', '5', '2']
# ['6', '7']
            grid3x3_status = row_checker(clean_row)
            print(grid3x3_status)
# True
# True
# True
# True
# True
# True
# True
# True
# True
            if grid3x3_status == False:
                break   
            '''this is not breaking out of the loop, even though the first result is False.'''
            
    if rows_status and columns_status and grid3x3_status == True:
        return True
    else:
        return False

print(sudoku_body([
        ['.', '.', '1', '.', '4', '.', '.', '2', '.'],
        ['.', '.', '6', '.', '.', '.', '.', '.', '.'],
        ['6', '.', '.', '.', '.', '.', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.', '.', '.', '.'],
        ['.', '6', '7', '.', '.', '.', '.', '.', '9'],
        ['.', '.', '.', '.', '.', '.', '8', '1', '.'],
        ['.', '3', '.', '.', '.', '.', '.', '.', '6'],
        ['.', '.', '.', '.', '7', '.', '.', '.', '.'],
        ['.', '.', '.', '5', '.', '2', '.', '7', '.']]))        


##############################################################
print(" ")
##############################################################


def line_is_valid(row):
       
    tmp_dict = {}    
    valid = True
        
    if len(row) > 0:
        for r in row:
            if r in tmp_dict:
                tmp_dict[r] += 1
            else:
                tmp_dict[r] = 1
            #print(tmp_dict)
         
        if tmp_dict[max(tmp_dict, key=tmp_dict.get)] > 1:
            valid = False
      
    return valid 
    
def grid_is_valid(grid):
        
    valid = True
        
    for i in range(len(grid)):       
        row = [int(x) for x in grid[i] if x != '.']
        #print(row)
        
        valid = line_is_valid(row)
        if not valid:
            break
                    
    return valid
    
def sudoku2(grid):
        
    result = False
        
    # check rows:
    rows_valid = grid_is_valid(grid)
            
    # check columns:
    col_valid = grid_is_valid(list(zip(*grid)))
              
    #check 3x3 grids:
    grid3x3_valid = True
    
    for i in range(0,len(grid), 3):
             
        if not grid3x3_valid:
                break
                     
        sub_mat = grid[i:i+3]
        #print(sub_mat)
             
        for j in range(0,len(grid[0]),3):
                 
            tmp_list = [x[j:j+3] for x in sub_mat]
            #print(tmp_list)
            tmp_list = [tmp_list[k][l] for k in range(len(tmp_list)) for l in range(len(tmp_list[k]))]
            #print(tmp_list)
                 
            row = [int(x) for x in tmp_list if x != '.']
            #print(row)
            grid3x3_valid = line_is_valid(row)
            #print(grid3x3_valid)
                 
            if not grid3x3_valid:
                break
            
                
    if rows_valid and col_valid and grid3x3_valid:
        result = True
            
    return result
   
print(sudoku2([['.', '.', '1', '.', '4', '.', '.', '2', '.'],
               ['.', '.', '6', '.', '.', '.', '.', '.', '.'],
               ['6', '.', '.', '.', '.', '.', '.', '.', '.'],
               ['.', '.', '.', '.', '.', '1', '.', '.', '.'],
               ['.', '6', '7', '.', '.', '.', '.', '.', '9'],
               ['.', '.', '.', '.', '.', '.', '8', '1', '.'],
               ['.', '3', '.', '.', '.', '.', '.', '.', '6'],
               ['.', '.', '.', '.', '.', '7', '.', '.', '.'],
               ['.', '.', '.', '5', '.', '.', '.', '7', '.']])) 
          
            


