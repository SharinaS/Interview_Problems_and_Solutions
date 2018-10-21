'''
Created on Mar 17, 2018

@author: sharina

FROM CODEFIGHTS

PROBLEM:
Write a solution that only iterates over the string once and uses 0(1) additional memory. Find and return the first instance
of a non-repeating character in it. ****If there is no such character, return '_' ****. For "abacabad", the answer is "c". for
"gogo", the answer is "_"


COOL SOLUTION... from someone...:
Uses a dictionary counter. From stackoverflow -- O(n) solution: We loop through the string once. When we come across a new character,
we store it in counts with a value of 1, and append it to order. When we come across a character we've seen before,
we increment its value in counts. Finally, we loop through order until we find a character with a value of 1 in counts
and return it.
'''


def fn(s):
    order = [] #['g','o','l','e']
    counts = {} # {'g':2, 'o':2, 'l':1,'e':1 }

    for i in s:
        if i in counts:
            counts[i] += 1  # this says that everytime this letter is come across, it adds one to the count for this number.
        else:
            counts[i] = 1
            order.append(i)

    for i in order:
        if counts[i] == 1:
            return i

    return "__________"

print(fn("google"))
# l

#########################################################################

# creating a set that counts up the number of each characters

st = "abacdadb"
listy = list(st)
# print(listy)
# ['a', 'b', 'a', 'c', 'd', 'a', 'd', 'b']



count_listy = [[x, listy.count(x)] for x in set(listy)]
print(count_listy)
# [['d', 2], ['c', 1], ['a', 3], ['b', 2]]
