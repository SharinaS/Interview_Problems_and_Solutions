'''
Created on Apr 3, 2018

@author: sharina

DIRECTIONS:
Try to solve this task in-place (with O(1) additional memory), since this is what you'll be asked to do during an interview.
You are given an n x n 2D matrix that represents an image. Rotate the image by 90 degrees (clockwise).
From CodeFights
'''
  
a = [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]

#Once image is rotated: 
    #[[7, 4, 1],
    #[ 8, 5, 2],
    #[ 9, 6, 3]]
    
def rotateImage(a):
    new_a = list(zip(*a))
    return [i[::-1] for i in new_a]
print(rotateImage([[1, 2, 3],[4, 5, 6],[7, 8, 9]]))    # [(7, 4, 1), (8, 5, 2), (9, 6, 3)]

############################
# The above code broken down:
############################

# get the columns from a, and make those columns the new rows:
new_a = list(zip(*a))  # Use * to unpack the list when you pass it to zip. This way, you pass two lists, instead of one list of lists
print(new_a)    #[(1, 4, 7), (2, 5, 8), (3, 6, 9)]. Now use list comprehension to reverse the elements within each row:

#now, reverse the elements in each row (note, can't do it this way for a 1-d list):
new_a_2d = [i[::-1] for i in new_a]
print(new_a_2d)     #[[(7, 4, 1), (8, 5, 2), (9, 6, 3)]]

# .... or, do it this way:
print(list(zip(*reversed(a))))       #[(7, 4, 1), (8, 5, 2), (9, 6, 3)]

# or.... compact the code into 1 list comp and do it this way:
print ([[x[i] for x in a][::-1] for i in range(len(a))])       # [[7, 4, 1], [8, 5, 2], [9, 6, 3]]


###############################################
# SIDE NOTE: 'reversed' creates an object
###########
b = [[1,2],[3,4]]
###########
b_rev = (reversed(b))
print(b_rev)        # <list_reverseiterator object at 0x10137a390>

for i in b_rev:
    print(i)    # [3, 4, 5] ---> b_rev[0] and b_rev[1] are now reversed. 
                # [1, 2, 3]
###############################################                
####### 
# Using for loops:
####### 

a = [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]
              
# Here's the printing of the elements once the array is turned ***counter-clockwise*** by 90 degrees... not the 
# correct direction AND it's O(n^2):
for i in range(len(a)):
    for j in range(len(a)):
        print(a[j][i])
'''
1
4
7
2
5
8
3
6
9
'''
print("******")

# Here's the elements printed after the array is turned ****clockwise****.... this solution though is O(n^2)
for i in range(len(a)):
    for j in range(len(a)):
        print(a[::-1][j][i])

