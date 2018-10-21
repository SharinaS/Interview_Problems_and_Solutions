'''
Created on Mar 11, 2018

@author: sharina

From CodeFights

Note: Write a solution with O(n) time complexity and O(1) additional space complexity, since this is what you would be asked 
to do during a real interview.

Given an array a that contains only numbers in the range from 1 to a.length, find the first duplicate number for which 
the second occurrence has the minimal index. In other words, if there are more than 1 duplicated numbers, return the 
number for which the second occurrence has a smaller index than the second occurrence of the other number does. If 
there are no such elements, return -1.
'''
#=========================================================
#Compare contents of the list to containers holding those list elements that do not allow for duplication. 
'''
PROBLEM: return the first duplicated number in the list
SOLUTION: add i to a set() from the list until i is repeated; at this point return i (at the repeated point).
if no repeats found between list and set comparison, just return -1.
'''

#==============================================================
#favorite solution
def firstDup(a):
    aSet = set()
    
    for i in a:
        if i in aSet:
            return(i)
        aSet.add(i)
    return(-1)
print(firstDup([2,3,1,3,5,1])) #set contains 2,3,1,5
# 3

#==============================================================

#Same thing, just with different elements:
def identifyingDups(alist):
    aset = set()
    for i in alist:
        if i in aset:
            return(i)
        aset.add(i)
    return("there were no duplicates")
print(identifyingDups(["Paul", "Tom", "Peter", "Tom", "Paul"]))
# Tom

#-----
#Figure this out....

def firstDuplicate(numbs):
    counter_dict = dict()
    for i in numbs:
        if counter_dict.get(str(i)):
            return i
        else:
            counter_dict[str(i)] = 1
    return -1
print(firstDup([2,3,1,1,3,5,1]))
# 1



#===============================================================================
# a = [2,3,3,1,5,2]
# aSet = set()
# 
# for i in a:
#     if i in aSet:
#         print(i)
#     aSet.add(i)
# print(-1)
#===============================================================================

#=========================================================
#To find duplicates and print them out - O(n):
from collections import Counter
mylist = [20, 30, 25, 20, 25]
print([k for k,v in Counter(mylist).items() if v>1]) #[20, 25]
# [20, 25]

#=========================================================
#Find the duplicates and print out their indexes with a library:
from collections import defaultdict
D = defaultdict(list)
for i,item in enumerate(mylist):
    D[item].append(i)
D = {k:v for k,v in D.items() if len(v)>1}
print(D) #prints dictionary of duplicates with their indices

#=========================================================
#Find the indices of the list without a library:
a = [2,3,3,1,5,2]
unique_entries = set(a)
indices = { value: [i for i, v in enumerate(a) if v == value ] for value in unique_entries }
print(indices)

#Find the lengths of each value group in the dict:
lengths = [len(v) for v in indices.values()]
print(lengths)

#=========================================================
#Removing all duplicates from the list using .append.
a = [2,3,3,1,5,2]
checked = []
for i in a:
    if i not in checked:
        checked.append(i)
print(checked) #[2,3,1,5]

#=========================================================
#Removing duplicates from the list using a set:
listy = [2,6,4,4,6,9,10,10,2,7]
sety= set()

for i in listy:
    sety.add(i)
print(sety) #{2,4,6,7,9,10}
print(list(sety)) #[2,4,6,7,9,10]

#=========================================================
for index, item in enumerate(a):
    print(index, item)
    

    
    
''' Output:
3
Tom
1
[20, 25]
{20: [0, 3], 25: [2, 4]}
{1: [3], 2: [0, 5], 3: [1, 2], 5: [4]}
[1, 2, 2, 1]
[2, 3, 1, 5]
{2, 4, 6, 7, 9, 10}
[2, 4, 6, 7, 9, 10]
0 2
1 3
2 3
3 1
4 5
5 2
'''
