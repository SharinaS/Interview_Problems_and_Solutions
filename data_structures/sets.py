'''A Set is an unordered collection data type that is iterable, mutable, and has no duplicate elements.'''

# SOME COOL SET METHODS:

lottery_ticket = {1,19,3,42,40}
winning_numbers = {1,19,3,86,20}

# Find the numbers that are in both sets:
for i in lottery_ticket:
    if i in winning_numbers:
        print(i)

# OR find the common numbers using a method:
print(lottery_ticket.intersection(winning_numbers))

# Combine the two sets into one set:
print(lottery_ticket.union(winning_numbers))

# Find the numbers in lottery_ticket that are not in winning_numbers:
print(lottery_ticket.difference(winning_numbers))

################################################
print(" ")
################################################

# If you start out with an empty set, use set()
setty = set()
for i in range (10):
    setty.add(i)
print(setty)


setty = {1,2,3,4}
print(max(setty))


# Determining differences in alphabet
stringy = "AAAaaaBBBbbbcc"
alphaSet = set(stringy)
print(alphaSet)
