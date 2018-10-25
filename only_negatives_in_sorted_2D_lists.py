'''
Created on Mar 28, 2018

@author: sharina

Here is a 2-D array problem: a matrix has sorted rows and sorted columns. So, if you look at the columns from top to bottom, or the 
rows from left to right, the numbers will either increase or stay the same. 

You need to write a function that takes the array as input and returns the number of negative numbers in it. 
First write an O(n^2) solution, then an O(n) solution
'''
##########################
negs = [[-4,-3,-2,0],[-2,-2,1,2],[-1,1,2,3],[1,2,4,5]] #function should return 6 negative numbers
##########################

# Solution using for loops and assessing length of a newly made list.

def num_negs(negs):
    allnegs = []
    for i in negs:
        for j in i:
            if j < 0:
                allnegs.append(j)
    return(len(allnegs))
print(num_negs([[-4,-3,-2,0],[-2,-2,1,2],[-1,1,2,3],[1,2,4,5]]))

#-------------------------------------------------------------------------
#Here's a list comprehension for the same outcome:
the_negs = [j for i in negs for j in i if j < 0]
print(len(the_negs))

#-------------------------------------------------------------------------
# Solution using a counter and definitely big O(n^2) time complexity
def num_negs2(negs):
    counter = 0
    for i in negs:
        for j in i:
            if j < 0:
                counter += 1
    return counter
print(num_negs2([[-4,-3,-2,0],[-2,-2,1,2],[-1,1,2,3],[1,2,4,5]]))

####################################################################################################################
# MORE EFFICIENCT: O(n) Solution

#    [-4,-3,-2, 0]
#    [-2,-2, 1, 2]
#    [-1, 1, 2, 3]
#    [ 1, 2, 4, 5]

# start at top right corner of aray. Then, keep going left until we see a neg #. That's the right most neg # in this row.
# As soon as we see this, in this case, we know there are 3 neg #s in this row without looking further, 'cause each row is sorted.
# Go to the next row, but instead of going to beginning, we'll just go down one cell directly from the right most neg # in the current row.
# Again, find the right most neg # in the row, and we'll know there are 2 neg #s in the second row. 
# Continue on until we get to the last row, or when there aren't any more neg #s to count. 
# Add up the #s of neg #s from each row. 
# Worst case scenario, the number of elements to check will be about 2n.

###########
# This solution uses a while loop with the idea that you don't need to iterate through something that is sorted. Instead start somewhere
# specific, ie, top right of the array. Tthen intentionally move step by step to the left, to count the occurrences of either pos or
# neg #s. For both counting negatives and positives, it was easiest to move right to left, b/c the negative number became the flag that
# makes the program move on to the next row (since due to the sorted array, all the numbers to the left of the neg number will also
# be negatives, and thus not something to worry about). 
###########

#----- Messing around with the code a bit....
sorted_arr = [[-4,-3,-2,0],[-2,-2,1,2],[-1,1,2,3],[1,2,4,5]]

first = sorted_arr[0]
print(first)            # [-4, -3, -2, 0]
print (len(first) -1)   # 3 (this is sending us to the lats column of this array.
print(sorted_arr[1])    # [-2, -2, 1, 2]
print(sorted_arr[1][2]) # prints 1
#########################################################################################

#------- Here's the solution, from Lynda's class: "Get Ready for Your Coding Interview"

def count_negatives(sorted_arr):  
    count = 0       # keeps track of # of neg #s seen so far
    row_i = 0       # this and col_i keeps track of which # is being currently examined. Initializes row i to 0 for starting location.
    col_i = len(sorted_arr[0]) - 1 # allows us to start at the last column of this array.
    
    while col_i >= 0 and row_i < len(sorted_arr): #means that we have more columns and more rows to examine
    # col_i starts at 3, counts down; row_i starts at 0 and counts up to 4             #
        
        if sorted_arr[row_i][col_i] < 0: # left side is the current number we're looking at
            count += (col_i + 1)    # we add 3 to count for the first row
            row_i += 1 #    move onto the next row
        
        else: 
            col_i -= 1 # if there are no more neg #s to count, move to the column to the left. 
    
    return count

print(count_negatives([[-4,-3,-2,-1],[-2,-2,1,2],[-1,1,2,3],[1,2,4,5]])) # prints 7

#    [-4,-3,-2,-1]  
#    [-2,-2, 1, 2]    
#    [-1, 1, 2, 3]
#    [ 1, 2, 4, 5]

#########################################################################################

def count_positives(sorted_arr):  
    count = 0       
    row_i = 0      
    col_i = len(sorted_arr[0]) - 1 # col_i = 3 to start
    arr_len = len(sorted_arr[0])
    
    while col_i >= 0 and row_i < len(sorted_arr):
        
        if sorted_arr[row_i][col_i] > 0:    
            count += arr_len - (col_i)  
            col_i -= 1    
        
        else: 
            row_i += 1 
            
    return count

print(count_positives([[-4,-3,-2, 1],[-2,-2,1,2],[-1,1,2,3],[1,2,4,5]])) # returns 10
print(count_positives([[-2,1],[1,2]])) # returns 3

#    [-4,-3,-2, 1]      [-2, 1]
#    [-2,-2, 1, 2]      [1, 2]
#    [-1, 1, 2, 3]
#    [ 1, 2, 4, 5]

