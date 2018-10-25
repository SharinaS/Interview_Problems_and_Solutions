'''
Created on Mar 19, 2018

@author: sharina
'''

'''Practice Problem involving a chessboard filled only with rooks, which move only vertically or horizonatally any number of spaces. 
if the program returns true, it means none of the rooks can attack each other. If it returns false, it means these rooks can attack each
other. Lesson learned here: Counting each row and each column is easier than I was trying to make it. You also just have to make sure to put
the counter in the correct spot, so each row or each column is counted, versus the entire list of lists.'''

def rookSafety(board):  
    n = len(board) 
    
    for row_i in range(n): #0 1 2
        row_count = 0 #variable to keep track of rooks seen so far
        for col_i in range(n): # go over each item in the row
            row_count += board[row_i][col_i] #count the # of rooks in each row
        if row_count > 1: # at the end of this for loop, if row count is > 1, there are multiple rooks in this row.
            return False #indicates these rooks will be able to attack each other.
    
    for col_i in range(n): #check each column index
        col_count = 0 #initialize col_count to zero.
        for row_i in range(n):
            col_count += board[row_i][col_i]
        if col_count > 1:
            return False
    
    return True #if program gets to this line, it means none of the rooks are able to attack each other, whether via rows or by columns

print(rookSafety([[0,0,1],[0,0,0],[0,1,0]]))    # prints True to the terminal

#    [0,0,1]
#    [0,0,0]
#    [0,1,0]

'''
how efficient is the rookSafety solution above? Or, what is the time complexity of the solution?
The time it takes to count the number of rooks in each row is n times big O of one. Total run time for all the rows combined is n times 
big O of n squared. We also need to count the number of rooks in each column. The runtime for that would be big O of n squared for
all the columns combined. Adding them up, we get two times big O of n squared, which is big O of n squared (a constant doesn't change 
anything in Big O). 
'''

