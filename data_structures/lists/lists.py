
people = input("Enter names of people you know")

# Turn string into a list and Clean up the list in one foul swoop:
pple_cleaned_up = [name.strip().capitalize() for name in people.split(",")]
print(pple_cleaned_up)

# a simple example of a string turned into a list, without cleanup
ppl_list = people.split(",")
print(ppl_list)

# Turn a list into a string
# syntax: string.join(iterable)
numList = ['lab', 'retriever', 'bulldog', 'chessie']
seperator = ', '
print(seperator.join(numList))
print(' '.join(numList))


print("#################")

# a standard list
l = [1,2,3]
print(l)

for elem in l:
    print(elem)

l.append(4)
print(l)


print("#################")
# printing a list backwards

aList = [1,2,3,4]
aList.reverse()
print(aList)

print("#################")

#finding the product of a list...
def multiply(nums):
    total = 1
    for num in nums:
        total *= num
    return total
print(multiply([1,2,3,4]))


from functools import reduce
def multiply2(nums):
    return reduce(lambda x,y: x*y, nums)
print(multiply2([1,2,3,4]))

print("#################")

# Replacing parts of a List
cool_list = [1,2,3,4]
cool_list[1] = 3
print(cool_list)

print("####################")

# computer science - identifying bytes allocated to a List
# and, formatting the output so it's readable
import sys
n=10
data=[]
for i in range(n):
    a=len(data)
    b=sys.getsizeof(data)
    print('Length: {0:3d}; Size in bytes: {1:4d} '.format(a,b))
    data.append(n)
# As we add more elements, there is no increase in bytes until there are memory usage jumps. The list grabs more space and memory in chunks, so it doesn't need to do it with each element.

print("####################")

#sorted() function returns a new sorted list. More convenient than list.sort(), slightly less efficient than  list.sort(), accepts any iterable versus just lists.
listy_to_be_sorted = [4,2,1,6,3,5]
print (sorted(listy_to_be_sorted))

#list.sort() method modifies the list in-place and returns None to avoid confusion. Less convenient than sorted() but, if you don't need the original list, it's slightly more efficient. Only accepts lists to be sorted.
listySort = [4,2,1,6,3,5]
listySort.sort()
print(listySort)

print("####################")

list_short = [1,2,3,4]
#print(list_short[4]) #prints "IndexError: list index out of range"

print("####################")
# ----- Get the index value of an element
listy = [1,2,3]
print(listy.index(2))

print("####################")
# ----- slicing
origList = [1,2,3,4]
print(origList[1::])
# if using return within a function, must create a new variable while slicing that list, then return that new variable.

# ----- pop() returns the highest index value, or a specified index.
a_list = [10,11,12,13,14]
print(a_list.pop())
print(a_list)

par_list = "[{()}]"
par_list = list(par_list)
print(par_list)
print(par_list.pop())

print("####################")
# ----- Make a list of individual strings into one string within a list using join. Join is a string method. The result of join is always a string, but the object to be joined can be of many types (generators, list, tuples, etc). join is faster b/c it only allocates memory once. Note there is a .joined and a .join.

letters = ['a','b','c','d']
letters_joined = ''.join(letters)
letters_joined_in_list = [''.join(letters)]


print(letters_joined) # abcd
print(letters_joined_in_list) # ['abcd']


#############################################
print(" ")
#############################################

# ----- Replacing something at a particular index.

a = [1, 2, 3]
print(a)
a[0] = 6
print(a)
