'''
LeetCode Problem: Flipping an Image

Given a binary matrix A, we want to flip the image horizontally, then invert it, and return the resulting image.
To flip an image horizontally means that each row of the image is reversed.
For example, flipping [1, 1, 0] horizontally results in [0, 1, 1].

To invert an image means that each 0 is replaced by 1, and each 1 is replaced by 0.
For example, inverting [0, 1, 1] results in [1, 0, 0].

Example 1:
Input:
[[1,1,0],
 [1,0,1],
 [0,0,0]]
Output: [[1,0,0],[0,1,0],[1,1,1]]
Explanation: First reverse each row: [[0,1,1],[1,0,1],[0,0,0]].
Then, invert the image:
[[1,0,0],
 [0,1,0],
 [1,1,1]]

Example 2:
Input: [[1,1,0,0],[1,0,0,1],[0,1,1,1],[1,0,1,0]]
Output: [[1,1,0,0],[0,1,1,0],[0,0,0,1],[1,0,1,0]]
Explanation: First reverse each row: [[0,0,1,1],[1,0,0,1],[1,1,1,0],[0,1,0,1]].
Then invert the image: [[1,1,0,0],[0,1,1,0],[0,0,0,1],[1,0,1,0]]

Notes:
1 <= A.length = A[0].length <= 20
0 <= A[i][j] <= 1'''

#############################################################

''' Here's a more precise way and more pythonic way to code this problem, inspired by a another
Leetcode entry. Here, a list comprehension is used to build a new 2D list. This list comprehension seems
to be really the most effective way to do this, unless you go for my original and more step_filled code below
Runtime: 48 ms, faster than 98.80% of Python3 online submissions for Flipping an Image.'''




def image_flipper(image):
    flipped_list = []
    for i in range(len(image)):
        flipped_list.append(reversed(image[i]))
    inverted_list = [[0 if j==1 else 1 for j in i] for i in flipped_list]
    return inverted_list

print(image_flipper([[1,0,0],[0,1,0],[1,1,1]]))



'''
NOTE: List Comprehensions are faster:
List comprehension is basically just a "syntactic sugar" for the regular for loop. In this case the reason that it
performs better is because it doesn't need to load the append attribute of the list and call it as a function at
each iteration. In other words and in general, list comprehensions perform faster because suspending and resuming
a function's frame, or multiple functions in other cases, is slower than creating a list on demand.
'''
##################################################################
'''Here's a solution to the problem, inspired by another LeetCode entry, which also has a runtime of 48 ms, and faster
than 98.80% of the LeetCode programming solutions... but it's not as easily readable in my option as the function
just above. At least the above code has a portion of the code written outside of a list comprehension.'''

def image_flipper(image):
    flipped_list = [reversed(image[i]) for i in range(len(image))]
    inverted_list = [[0 if j==1 else 1 for j in i] for i in flipped_list]
    return inverted_list

print(image_flipper([[1,0,0],[0,1,0],[1,1,1]]))

#######################################################################################
#######################################################################################
'''PSEUDOCODE for the following code:
Reverse each row using list comprehension and iterating backwards to get a new 2D,
then 1D list.

Then, replace the 1's with 0's and the 0's with 1's to invert the 1D list.
If element == 1: element = 0; if element == 0: element = 1.
Use a dictionary -->  invert_dict = {"1": 0, "0": 1}

Then, take the 1D list and make it into a 2D list, with the length of its sublists
defined by the number of sublists in the original 2D list.
##############################################################
RUNTIME NOTES:
52 ms, faster than 70.85% of Python3 online submissions for Flipping an Image on LeetCode
'''

def image_flipper(image):
    len_image = len(image)
    invert_dict = {1: 0, 0: 1}
    i = 0
    new_list = []

    # reverse each sublist and then flatten the 2D list into 1D
    reversed_image = [i[::-1] for i in image]
    flattened_list = [j for i in reversed_image for j in i]

    # use the dictionary to make a new 1D inverted list
    while i < len(flattened_list):
        if flattened_list[i] == 0:
            new_list.append(invert_dict[flattened_list[i]])
        elif flattened_list[i] == 1:
            new_list.append(invert_dict[flattened_list[i]])
        i=i+1

    # make the new 1D list into a 2D list
    two_dim = [new_list[i:i+len_image] for i in range(0, len(new_list), len_image)]

    return two_dim

print(image_flipper([[1,0,0],[0,1,0],[1,1,1]]))


#########################################################
'''Here's a simpler way to code this problem, inspired by another LeetCode solution:
Runtime: 52 ms, faster than 69.93% of Python3 online submissions for Flipping an Image.
Explaination: 0 % 1 = 1, while 1 % 2 = 0, effectively inverting the list.'''

def flipandinvert(image):
    new_image = []
    for i in image:
        updated = [(j+1)%2 for j in i]
        updated.reverse()
        new_image.append(updated)
    return new_image
print(flipandinvert([[1,0,0],[0,1,0],[1,1,1]]))
