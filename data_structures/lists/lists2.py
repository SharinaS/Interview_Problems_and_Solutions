# REMINDER - CONCATENATING TWO LISTS PRODUCES ONE BIG LIST.
list1 = [8,1]
list2 = [22,21]
print("list2 added to list1", list1 + list2)

# A couple ways to print out lists:
# '''
listA = ["Cats", "Dogs", "Birds", "Reptiles"]
for animal in listA:
    print(animal)

#OR use indexes:
for animal in range(4):
    print(listA[animal])

 #OR use indexes and length of list
for animal in range(len(listA)):
    print(listA[animal])
 # Useful for iterating through multiple lists at the same time.

'''
Turn lists into strings
'''
animals = ["cats", "dogs", "rabbits", "birds", "elephants"]
stringAnimals = ' , '.join(animals)
print ("These are all animals: {}.".format(stringAnimals))

'''
Turn strings into lists
'''
listanimals = stringAnimals.split(' , ')
print(listanimals)

'''
# lowercase of letters with list comprehension
# '''
humans = ["Asian", "Caucasian", "Hispanic", "Native American"]
lowerHumans = [i.lower() for i in humans]
print(lowerHumans)

upperHumans = [i.upper() for i in humans]
print(upperHumans)

# '''
# Making lists into nice sentences
# '''
# niceSentence = ("Humans are represented by many races, some of which include: {}, {}, {}, and {}.".format(humans[0],
#                                                                                                           humans[1], humans[2], humans[3]))
# print(niceSentence)
#
#
# '''
# addition with lists
# '''
#
# adds = [1, 2, 3, 4, 5]
#
#
# total1 = sum(adds)
#
# #OR
#
# total2 = 0
# for i in adds:
#     total2 += i
#
# print (total1)
# print (total2)
#===============================================================================

# ''' Sorting and Slicing arrays '''
#
# arr = [1,3,4,5,0,-2]
# arr.sort()
# print(arr)
# if arr[2:3] < arr[3:4]:
#     print (arr[3:4])
# else:
#     print("array is not yet in order")
#
# def sortAndSlice(arr2):
#     arr2.sort()
#     if arr2[2:3] < arr2[3:4]:
#         print (arr2[3:4])
#     else:
#         print("array is not yet in order")
#
# sortAndSlice([1,3,4,5,0,-2])
#===============================================================================

''' find the second largest number in the array. if there are 2 largest numbers, the second of the largest numbers is
the answer. If the array has nothing in it, or has 1 element in it, return None.

Here are two ways I did this:
'''

#===============================================================================
#
# def second_largest(arr):
#     biggest = 0
#     second = 0
#
#     if len(arr) <= 1:
#         return None
#
#     if len(arr) > 1 and len(arr) <= 3:
#         arr.sort()
#         return arr[-2]
#
#     for i in arr:
#         for j in arr:
#             if i > biggest:
#                 biggest = i
#             elif j < biggest and j > second and len(arr) > 3:
#                 second = j
#     return second
#
# print(second_largest([2, 2, 1, 3, 4, 7, 7, 6, 6, -1]))
#
#
#
# def second_largest(listy):
#
#     if len(listy) <=1:
#         return None
#
#     elif len(listy) > 1:
#         listy.sort()
#
#         chopped = listy[-2]
#         return chopped
#
# print(second_largest([0, 6, 3, 4, 2, 1, 5]))
#
#
# def second_largest(listy):
#
#     largest = None
#     second_largest = None
#
#     for i in listy:
#         if largest == None:
#             largest = i
#
#         elif i > largest:
#             second_largest = largest
#             largest = i
#
#
#         elif second_largest == None:
#             second_largest = i
#
#         elif i > second_largest:
#             second_largest = i
#
#     return second_largest
#
# print(second_largest([5]))
#
# def third_largest(listy):
#     largest = None
#     second = None
#     third = None
#
#     for i in listy:
#         if largest == None:
#             largest = i
#
#         elif i > largest:
#             third = second
#             second = largest
#             largest = i
#
#         elif second == None:
#             second = i
#
#         elif i > second:
#             third = second
#             second = i
#
#         elif third == None:
#             third = i
#
#         elif i > third:
#             third = i
#
#     return third
#
# print (third_largest([5, 6, 6, 3, 2]))
#===============================================================================

#===============================================================================
# a = [[1,2,3,4],[5,6,7,8]]
# print(a)
#
# for i in a:
#     for j in i:
#         print(j)
#===============================================================================

#---------ADDING TO &  DELETING FROM LISTS

#===============================================================================
# nephews = ["Huey", "Dewey", "Louie"]
# for i in range(3):
#     nephews[i] = nephews[i] + " Duck"
# print(nephews)
#
# dogs = ["bird", "hunting", "cadavor"]
# for i in range(len(dogs)):
#     dogs[i] = dogs[i] + " dogs"
# print(dogs)
#
#
# dogs.append("jogging dog")
# print(dogs)
#
# dogs.extend(["search dog"])
# print(dogs)
#
# dogs = dogs + ["army dog"]
# print(dogs)
#
# dogs.insert(0,"happy dogs")
# print(dogs)
#
# dogs.remove("happy dogs")
# print(dogs)
#
# del dogs[0]
# print(dogs)
#
# dogs.sort()
# print(dogs)
#
# #------------ Slicing
#
# bunchonumbs = [0,2,4,6,8,10]
# slicer = bunchonumbs[0:2]
# print(slicer)
# slicer = bunchonumbs[:5]
# print(slicer)
# slicer = bunchonumbs[:]
# print(slicer)
#
# #Reassign elements using slicing
# bunchonumbs[0:2] = [50, 60]
# print(bunchonumbs)
#
# #Delete elements using slicing
# del bunchonumbs[-2:]
# print(bunchonumbs)
#
# #--------- Loops
# primates = ["humans", "chimps", "gorillas", "spider monkeys"]
# for animal in primates:
#     print("Terran primate:", animal)
#
# for index, value in enumerate(primates):
#     print("Terran primate", index, "--> ", value)
#
# if "chimps" in primates:
#     print(True)
# else:
#     print(False)
#

#===============================================================================
# #Finding the sum of a 2-D lists diagonal:
# #diag = [[1,2,3], [4,5,6], [7,8,9]]
#
# def diagonal(diag):
#     total = 0
#     for i in range(len(diag)):
#         total += diag[i][i]
#     return(total)
# print(diagonal([[1,2,3], [4,5,6], [7,8,9]]))
#===============================================================================
