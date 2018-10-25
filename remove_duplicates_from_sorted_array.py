'''
Created on May 7, 2018

@author: sharina

From Leet Code: Remove Duplicates from Sorted Array
Given a SORTED array nums, remove the duplicates in-place such that each element appear only once and return the new length.
Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

NOTE:
Converting a list to a set requires that every item in the list be visited once, O(n). Inserting an element into a set is O(1), 
so the overall time complexity would be O(n).
Space required for the new set is less than or equal to the length of the list, so that is also O(n).


'''
     
#################################
# Figuring out the Code
nums = [1,1,2]
newNumbs = set(nums)
print(newNumbs) # {1, 2}
print(list(newNumbs)) # [1, 2]
print(len(newNumbs)) # 2

     
#################################
print(" ")
''' Thoughts on creating an O(n) solution:
1. if it's not in the set, add to set and increase count by 1. 
2. if it is in the set, counter does not increase'''
#################################

# Here's an O(n) solution I designed:

def no_duplicates(nums):       
    setty = set()
    counter = 0
    #new_list = []

     
    for i in nums:
        if i not in setty:
            setty.add(i)
            counter += 1
            #new_list.append(i)

    #return new_list # [0, 1, 2, 3, 4]
    return counter # 5
         
print(no_duplicates([0, 0, 1, 2, 3, 3, 4]))   

##################################################################
##################################################################
print(" ")


# figuring out the code

listy = [1, 1, 2, 3, 3]
print(listy[0+1]) # 1
print(listy[0+2]) # 2
print(len(listy)-1)  # 4 (which is index 4, which is the number 3! Yay!)

#*********
print("solution based on prior experience so far")
#*********
'''
This function moves through the list from right to left. 

BUT LeetCode DIDN'T ACCEPT THIS. It does, however produce an accurate count, so maybe the time 
or space complexity is not what they're looking for?  Or maybe they don't like the list being reversed :p

LOGIC/PSEUDO-CODE:
Start at last index and see if this last element is greater or equal to the element prior (Moving backwards through
list seems to make it easier to stop the while loop when it reaches the beginning of the list).
If it's greater, increase count by 1, then move one element to the left. Otherwise, move one spot to the left and 
repeat. return count when the index value (the element) drops to zero.

'''

def notta_dup1(sorted_list):
    count = 1 
    element = len(sorted_list)-1 # starts at --> 1
    new_list = []

     
    if sorted_list == []:
        return 0
    if len(sorted_list) == 1:
        return 1
    
    while element > 0:
        if sorted_list[element] == sorted_list[element-1]:
            element -= 1
            
        else:
            count += 1
            new_list.append(sorted_list[element])
            element -=1
     
    #return count  # 5
    return new_list # [7, 6, 5, 4]
             
print(notta_dup1([2, 4, 4, 4, 5, 6, 7]))

##################################################################
''' Here is a function that moves through the sorted list from left to right.
It compares each element with the one next to it, then moves to the right.
'''

def notta_dup2(sorted_list):
    count = 1  # 2
    element = 0 # 2
    #new_list = [] # [2 ]

     
    if sorted_list == []:
        return 0
    
    
    while element+1 < len (sorted_list):
        if sorted_list[element] == sorted_list[element+1]:
            element += 1
            
        else:
            count += 1
            #new_list.append(sorted_list[element])
            element +=1
     
    return count  # 5
    #return new_list 
             
#print(notta_dup2([2, 4, 4, 4, 5, 6, 7]))  # [7, 6, 5, 4]
print(notta_dup2([1, 2, 2]))   # 2

##################################################################
#===============================================================================
print("solution derived from a leetcode discussion:")
#===============================================================================

''' HERE'S A NICE SOLUTION -- the only solution listed here which was accepted by
LeetCode, which is 0(n) Time Complexity and 0(1) Space Complexity, 
and is based on the official solution:

NOTE: the command -- if not listy -- will execute if listy is any kind of zero or empty container, or False. 
Many people do use not listy where they really do mean listy is not None.


Pseudo code:
Edge cases: 
(1) If list doesn't contain anything, return 0. 
(2) If len(list) == 1: return 1

Start at index 0. If at index 0, at index 1 is the same number, compare the num at index 0 with 
the num at index 2, and so on.
Keep increasing element_next_store's count (which starts at index 1) until a number is found that 
is greater than the number at index 0.

DISCUSSION FROM LEETCODE (edited to fit this solution):
Since the array is already sorted, we can keep two variables -- element, and element_next_door, 
where element_next_door is the fast-runner while element is the slow-runner. 
As long as nums[element] == nums[element_next_door], we increment element_next_door to skip the duplicate.

When we encounter nums[element] != nums[element_next_door], the duplicate run has ended, 
so we must copy its value to nums[element + 1]... effectively allowing element to catch up.
Element is then incremented and we repeat the same process again until element_next_door reaches the end 
of the array.
...

'''

def notta_dup3(nums):
    element = 0 # 4
    element_next_door = 1  # 7
    new_list = []
    
    if nums == []: 
        return 0
     
    while element_next_door < len(nums): 
       
        if nums[element] == nums[element_next_door]:
            element_next_door += 1
          
        else:
            element += 1 #(element is also our counter)
            nums[element] = nums[element_next_door] # 6
            element_next_door +=1
            new_list.append(nums[element])
      
    #return element+1
    return new_list  
    
#print(notta_dup3([2, 4, 4, 4, 5, 6, 7]))   # new_list = [4, 5, 6, 7], element+1 = 5
print(notta_dup3([1, 1, 2])) 

