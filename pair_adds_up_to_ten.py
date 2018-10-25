'''
Created on Jun 3, 2018

@author: sharina

Question from Lynda Class: "Get Ready for Your Coding Interview" in the dictionary review section:

Find the pair of numbers in an array that adds up to 10. In list [3,4,1,2,9], 9 and 1 add up to 10. Assume we'll only
have integers (no decimals). The numbers in the array can be negative or zero. What if two or more pairs exist that add
up to ten? Just print out one of them. If no pair adds up to ten, print "There's no pair that adds up to 10. Goal is to solve 
problem with Big 0(n) complexity. 
'''

#Playing with the code:

age_dict = {'Emily': 32, 'Tom': 43}
print(age_dict) # {'Emily': 32, 'Tom': 43}

age_dict['George'] = 22
print(age_dict) # {'Emily': 32, 'Tom': 43, 'George': 22}

age_dict['Luna'] = "dog"
print(age_dict) # {'Emily': 32, 'Tom': 43, 'George': 22, 'Luna': 'dog'}

if 'Luna' in age_dict:
    print('Found Luna!')
    
del age_dict['Emily']
print(age_dict)
# {'Tom': 43, 'George': 22, 'Luna': 'dog'}
    
#print the value for George:
print(age_dict['George'])  # 22

print(" ")

# Playing around with how to print out the data
numbs = {1: 1, 3: 1, 5:1, 7:1}
print(numbs) # {1: 1, 3: 1, 5: 1, 7: 1}
print(set(numbs)) # {1, 3, 5, 7}
print(tuple(numbs)) # (1, 3, 5, 7)
print(str(numbs)) # {1: 1, 3: 1, 5: 1, 7: 1}

print(" ")

# print just a key:
print(numbs.keys()) # dict_keys([1, 3, 5])
print(numbs.values()) # dict_values([1, 1, 1])
if 10 - 9 in numbs:
    print(10-9, 9)
    

# LISTS
l = [1, 2, 3, 4]
print(l.pop(1))
print(l)
l.append(4)
print(l)

###################
print(" ")
###################

# Return the name that appears twice in the list
def appears_twice(given_list):
    name_dict = {}
    
    for name in given_list:
        if name in name_dict:
            return name
        
        else:
            name_dict[name] = 1
            
    return ' '
    
print(appears_twice(['Tom', 'Tom', 'Tom', 'Joe', 'Pete', 'Danny', 'Bobby']))


# Count the number of times each element occurs in the list:
def count_occurrences(name_list):
    counter = {}
    for name in name_list:
        if name in counter:
            counter[name] += 1
        else: 
            counter[name] = 1
    return counter
    
print(count_occurrences(['Tom', 'Tom', 'Tom', 'Joe', 'Pete', 'Danny', 'Danny', 'Bobby']))
# Tom 

print(" ")


##############################################################################################################
print(" ")
print("Find a Pair of Numbers that Adds up to 10")
##############################################################################################################
'''
Find the pair of numbers in an array that adds up to 10. In list [3,4,1,2,9], 9 and 1 add up to 10. Assume we'll only
have integers (no decimals). The numbers in the array can be negative or zero. What if two or more pairs exist that add
up to ten? Just print out one of them. If no pair adds up to ten, print "There's no pair that adds up to 10. Goal is to solve 
problem with Big 0(n) complexity. 

THINKING:
If we move through the list and compare each pair, we have to iterate through a couple times, so this is n^2 and not good.
If we use sort to arrange the numbers in the list, that is 0(n log n) for at least part of the problem, so that's probably also bad. 

Dictionaries use 0(1) time to insert or read... we can therefore use a dict to store elements as keys as we iterate through 
a list. At each element of the list, check the dict to see if we've come across the matching pair to the element in question. 
10 - num will be the number we want as the matching pair. If is it there, return num and dict_compare
This lets us only iterate through the list once, since we're comparing between two different containers, adding and 
comparing to the dict container as we go. 
'''

def two_for_ten(numbs):
    dict_check = {} 
    
    for num in numbs:
        if (10 - num) in dict_check:
            return (num, 10 - num) 
        else:
            dict_check[num] = 1 

    return ("There is no pair that adds up to 10")

print(two_for_ten([3,4,1,2,-9, 19, 9, 1])) # (19, -9)


##############################################################################################################
print(" ")
print("Find All the Pairs that Add Up to 10")
#############################################################################################################


def pairs_make_10(numbs):
    dict_check = {} 
    pairs = []
    
    for num in numbs:          # ------> 0(n)
        if (10 - num) in dict_check:
            pairs.append((num, 10-num)) # print out a tuple     ------> 0(1)
            
        else:
            dict_check[num] = 1  # ------> 0(1)
    
    if pairs != []:
        return pairs
    else:
        return ("There is no pair that adds up to 10")

print(pairs_make_10([3,7,1,2,-9, 19, 9, 1]))     # [(7, 3), (19, -9), (9, 1)]

