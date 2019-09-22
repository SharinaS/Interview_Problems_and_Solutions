'''LEETCODE Medium complexity problem:
Given two strings, check to see if they are anagrams. An anagram is when the two strings can be written using the exact same letters (so you can just rearrange the letters to get a different phrase or word). Ignore spaces and capitalization.

Notes:
Anagrams can be evaluated one of two ways:
1) if the arrays when sorted are equivalent, they are anagrams.
2) if the arrays have exactly the same elements and the same number of those elements, they are anagrams --> Most optimal, esp in an interview setting.

PseudoCode for using dictionary to solve problem:
1 - clean up the strings
2 - do an edge case check - check lengths, since if they are different lengths, they are not anograms.
3 - create a dictionary
4 - count up the letters in the first string
5 - count up the letters in the first string, but substract from the dictionary
6 - check if any of the values haven't been reduced to zero; that means the second string is different.
'''

# Use ONE dictionary, versus two to count- this is most optimal and a great interview solution, since it shows everything going on (not Python specific)
def anagramDict(string1, string2):
    dictCounter = {}
    string1 = string1.lower().replace(" ","")
    string2 = string2.lower().replace(" ","")

    if len(string1) != len(string2):
        return False

    for letter in string1:
        if letter in dictCounter:
            dictCounter[letter] += 1
        else:
            dictCounter[letter] = 1

    for letter in string2:
        if letter in dictCounter:
            dictCounter[letter] -= 1
        else: dictCounter[letter] = 1

    for value in dictCounter:
        if dictCounter[value] != 0:
            return False

    return True

print(anagramDict("clint eastwood", "old west action"))


# Using TWO dictionaries to count the characters in each string - less optimal, but what I thought of first:
def anagramDicts(string1, string2):
    dictCounter1 = {}
    dictCounter2 = {}
    string1 = string1.lower().replace(" ","") # remember, replace() doesn't change the original string
    string2 = string2.lower().replace(" ","")

    # edge case check
    if len(string1) != len(string2):
        return False

    # create dictionary (could use a default dict from collections module, but given this is an interview question, I avoided special modules)
    for letter in string1:
        if letter in dictCounter1:
            dictCounter1[letter] += 1
        else:
            dictCounter1[letter] = 1

    for letter in string2:
        if letter in dictCounter2:
            dictCounter2[letter] += 1
        else:
            dictCounter2[letter] = 1

    if dictCounter1 == dictCounter2:
        return True
    else:
        return False

print(anagramDicts("clint eastwood", "old west action"))



##################################################
print(" ")
print("SOLUTIONS USING SORTING, NOT DICTIONARIES")

# Here's the cleanest Python way to compare sorted strings:
def anagramSort(string1, string2):
    string1 = string1.lower().replace(" ","")
    string2 = string2.lower().replace(" ","")

    return sorted(string1) == sorted(string2)

print(anagramSort("clint eastwood", "old west action"))

#____________________________

# This is a neat and easy to read way, I think, to sort and compare strings. I decided to used sorted to turn the strings into lists, and skipped turning the lists back into strings with join() before comparing them, since it didn't seem necessary.

def anagramSort(string1, string2):
    string1 = sorted(string1.lower().replace(" ",""))
    string2 = sorted(string2.lower().replace(" ",""))

    if string1 == string2:
        return True
    else: return False

print(anagramSort("clint eastwood", "old west action"))

#_______________________________

# Here is an unweildy but successful function to sort and compare strings:
checker1 = []
checker2 = []
def anagram(string1, string2):
    string1 = string1.lower().replace(" ","")
    string2 = string2.lower().replace(" ","")

    for i in string1:
        if i in string2:
            checker1.append(i)
        else: return False
    for i in string2:
        if i in string1:
            checker2.append(i)
        else: return False

    checker1.sort()
    checker2.sort()

    if checker1 == checker2:
        return True
    else: return False

print(anagram("clint eastwood", "old west action"))
