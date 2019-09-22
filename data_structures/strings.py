
# Turn a list into a string
# syntax: string.join(iterable)
numList = ['lab', 'retriever', 'bulldog', 'chessie']
separator = ', '
print(separator.join(numList))
print(' '.join(numList))

firstList = ['Man', 'Woman']
between = ' = '
print(between.join(firstList))

s1 = "abc"
s2 = "123"
combo = s1.join(s2)
print(type(combo))
print(combo)

first = "apple"
second = "PEAR"
first_second = first.join(second)
print(first_second)



# Using the center method
string = "Python is awesome"
new_string = string.center(40)
print(new_string)


# Clean up a string:
people = input("Enter names of people you know")
print(type(people))
people = people.replace(" ", "")
print (people)


# Put everything, even weird letters, lowercase:
string = "PYTHON IS AwESOME"
lower_string = string.casefold()
print(lower_string)

firstString = "der Fluß"  # <----------- This ß is lowercase in German
secondString = "der Fluss"

if firstString.casefold() == secondString.casefold():
    print('The strings are equal.')
else:
    print('The strings are not equal.')


#Turn string into a list (populated by individual strings)
ppl_list = people.split(",")
print(ppl_list)

# Sort letters in a string:
stringy = "clinteastwood"
print(''.join(sorted(stringy)))  # sorted turns string into a list; join makes it a string againself.

# sort letters and maeke them distinct while keeping caps:
s = "Bubble Bobble"
print(s)
print(''.join(sorted(set(s))))

# sort letters, keep duplicates, remove whitespaces:
stringy = "Hey sexy, you're hot"
print(''.join(sorted(stringy.lower())).strip())


# remove leading and trailing whitespaces
str = "  hey everyone   "
print(str)
print(str.strip())


# use indexing with strings
st = "Hey hotstuff"
print(st[2])

# turn a dictionary into a string
dicty = {"A":2, "b":1}
stringy = str(dicty)
print(stringy)
print(type(stringy))


# Manually coding out what .split() does inherently (I love split() now). This uses the first while loop to identify the start of a word, and a nested while loop to step through the string until we get to the end of the word. Then, it appends that word to a list of words.
def manual_split(str):
    words = []
    spaces = [' ']
    index_tracker = 0
    while index_tracker < len(str):
        if str[index_tracker] not in spaces:
            word_start = index_tracker # get index where word starts

            while index_tracker < len(str) and str[index_tracker] not in spaces: # get index where word ends
                index_tracker += 1

            words.append(str[word_start:index_tracker])
        index_tracker += 1

    return words
print(manual_split("   singing in the   rain   "))


# Manually coding out what reversed() does with a while loop
def reverseWhileLoop(str):
    str = str.split()  # str = ["  This", "is", "the", "best"]
    listy = []
    counter = len(str) - 1
    while counter >= 0:
        listy.append(str[counter])
        counter -= 1

    return " ".join(listy)
print(reverseWhileLoop("  This is the best  "))


# Manually coding out what reversed() does with a for loop
def reverseForLoop(arr):
    bkwrds = []
    for word in range(len(arr),0,-1):
        bkwrds.append(arr[word-1])

    return " ".join(bkwrds)
print(reverseForLoop(["Oh", "what", "a", "beautiful", "morning"]))
