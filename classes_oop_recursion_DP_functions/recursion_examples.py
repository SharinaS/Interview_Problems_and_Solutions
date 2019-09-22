'''
Unless noted otherwise:
From Udemy's class: Python for Data Structures, Algorithms and Interviews!, by Jose Portilla
From https://blog.angularindepth.com/learn-recursion-in-10-minutes-e3262ac08a1

--> Recursion <--

BASE CASE:
When developing a recursive solution, you must think about the base case, as the solution will need to return to the base case once all the recursive cases have been worked through.

DIFFERENT VALUES OF N:
Remember in each recursive call, each one is holding on to a different value of n. The answers then cascade back down (https://www.youtube.com/watch?v=Mv9NEXX1VHc)

KNOWING WHEN TO USE RECURSION:
"A task can also be solved using iterative solution, but it’s way more complicated because we would have to nest for loops but don’t know how deep they are nested. The unknown number of nested loops is a common characteristic of all problems that are recursive in their nature and should give you a hint that recursive solution is required.... A common mistake beginners make when designing a solution to a recursive problem is to try to imagine what happens inside the recursive call, instead of just trusting that it will return the correct result....

... do not think about a recursive program as a series of execution steps and try to reconstruct execution tree in your head....think about how the original problem can be represented as a simpler problem plus some additional operations. Identifying this simpler problem is arguably the most difficult part of solving a recursive problem.... Once you identified the simpler problem proceed to find the simplest problem your function will need to solve. This simplest problem is called base case. It is usually represented as a form of a condition which terminates recursion." - from https://blog.angularindepth.com/learn-recursion-in-10-minutes-e3262ac08a1  <== best article so far, by the way.

By the way, Tail Recursion is not implemented in Python (see Guido's blog post: http://neopythonic.blogspot.com/2009/04/tail-recursion-elimination.html)
'''

# Recursive function for finding the factorial of a number, for example, the factorial of 5 is: 5 * 4 * 3 * 2 * 1


def factorial(n):
    # base case
    if n == 0:
        return 1

    else:
        return n * factorial(n-1)

print(factorial(5))

###############################################################################
print(" ")
###############################################################################
# Recursive function to take an integer and calculate the cumulative sum of zero to that integer. So, if n=4, return 5+4+3+2+1+0, which is 15.

def cumulative_sum(n):
    #print(n)

    # base case
    if n == 0:
        return 0

    else:
        return n + cumulative_sum(n-1)

print(cumulative_sum(5))

###############################################################################
print(" :)  ")
###############################################################################

# Return the sum of all the individual digits in that integer. So, if n = 4321, return 4+3+2+1. Note that the double-slash is for "floor" division, which rounds down to nearest whole number. Classic division means that if the operands are both integers, it will perform floor division, while for floating point numbers it represents true division.

def sum_individual(n):
    # base case
    #if len(str(n)) == 1:  # remember, integers don't have the length property
        #return n
    if not n:
        return n

    else:
        # strip a digit off n
        return n % 10 + sum_individual(n // 10)
print(sum_individual(4321))

###############################################################################
print(" :) ")
###############################################################################

# Create a function that takes in a string and a set list of words. The function will then determine if it can split the string in a way words can be made from the list of words. In other words, if the list contains the words within the phrase, output those words within the phrase as a list of strings. Assume the phrase will only contain words found in the dictionary if it is completely splittable.

# Notes on solution: output = None in argument b/c this will be a recursive function; if output is set to a list as a default parameter, it will overwrite the output list every time the recursive function runs. Instead, with it this way, output is set to an empty list only on the first instance of the recursion. Note that startswith() is a pythonic way to do something if a string starts with another string (otherwise can use indexing and length). Here's a very pythonic solution provided from the Udemy class.

def word_split(stringy, list_of_words, output = None):
    if output is None:
        output = []

    for word in list_of_words:
        # note - if the current phrase begins with the word, we have a split point. There are two ways to show this - startswith() or using indexing to splice out the word.

        if stringy.startswith(word):
        #if stringy[:len(word)] == word:
            output.append(word)

            # recursively call the split portion on the remainging portion of the phrase --- phrase[len(word):]. Remember to pass along the output and list of words.
            return word_split(stringy[len(word):], list_of_words,  output)

    # return output if no stringy.startswith(word) returns True
    return output



print(word_split("helloworld", ['hellos', 'worlds']))
print(word_split("Johnlovesdogs", ['i','am','a','dogs','lover','loves','John']))

###############################################################################
print(" ")
###############################################################################

# REFRESHER on indexing and string splitting

word = 'hellothere'
print("length of word:", len(word))
print("splitting word from 0-4:", word[0:4]) # hell
print("splitting word from 0-4:", word[:4]) # hell
print("everything but the first letter:", word[1:])
print("splitting word from 4-end:", word[4:]) # o
print("letter at index 4:", word[4]) # o
print("splitting word from the length of that word onward:", word[len(word):])
print("splitting word from 0 to the length of the word:", word[:len(word)])

###############################################################################
print(" ")
###############################################################################

# Reverse a string using recursion. Do not slice or use iteration. - From Udemy's Python for data structures, algorithms and interviews

def recursive_reversal(str):
    # base case:

    #if len(str) <= 1:
    if not str:
        return str

    # recursion
    else:
        #return str[-1] + recursive_reversal(str[:-1])
        # or, can flip this, by writing:
        return recursive_reversal(str[1:]) + str[0]


print(recursive_reversal("hello"))


###############################################################################
print("********************* ")
###############################################################################

# PROBLEM - Write a function that sums all numbers in an array that can have nested sub-arrays. Do not use loops. - from article by Max Koretskyi (https://blog.angularindepth.com/learn-recursion-in-10-minutes-e3262ac08a1)

# Thoughts on RECURSION: a simpler problem than the given --> an array without nested subarrays. Even simpler than is --> a sum of n-1 elements (the length of the array; -1 accomodates for the fact that indexing starts at zero) and only need to add the current element to this sum. Simplest case --> when no elements are left to be added - return 0.

# SUMMING OF A SIMPLE LIST USING RECURSION:
def sum_of_a_list(listy):

    # base case - if no more elements are left to be added:
    #if len(listy) == 0:
    if not listy:
        return 0

    # else add the current element to the sum in recursive steps:
    return listy[0] + sum_of_a_list(listy[1:])


# SUMMING UP A SIMPLE LIST USING A FOR LOOP / ITERATION:
def list_sum(listy):

    result = 0

    for i in range(len(listy)):
        result += listy[i]

    return result


# HERE'S A FUNCTION FOR FLATTENING A LIST (note some of the hastags are optional ways to write the code)
# Note - The isinstance() function in python checks if the object (first argument) is an instance or subclass of classinfo class (second argument).

def flatten_a_list_of_lists(listy):

    #if listy == []:
    if not listy:
        return listy

    #if isinstance(listy[0], list):
    #if type(listy[0]) == list:
    #if type(listy[0]) is not int:
    if type(listy[0]) is list: # as in, it's not an integer
        return flatten_a_list_of_lists(listy[0]) + flatten_a_list_of_lists(listy[1:])

    #else:
    return listy[:1] + flatten_a_list_of_lists(listy[1:]) # as in, a list + recurse over rest of list.


# USING RECURSION WITHIN A FOR STATEMENT to sum up a list of lists after looking again at article: https://blog.angularindepth.com/learn-recursion-in-10-minutes-e3262ac08a1: It says: "This task can also be solved using iterative solution, but it’s way more complicated because we would have to nest for loops but don’t know how deep they are nested. The unknown number of nested loops is a common characteristic of all problems that are recursive in their nature and should give you a hint that recursive solution is required." This function is bult on the iterative function above, called def list_sum. Note: "...do not think what will happen once sum_list_of_lists function is executed. This is not a useful way to think about recursion. Instead trust that it returns correct sum for all elements of an array a[i].  Also, do not think about a recursive program as a series of execution steps."

def sum_list_of_lists(listy):

    result = 0

    for i in range(len(listy)):
        # if type(listy[i]) is list:
        if isinstance(listy[i], list):
            result += sum_list_of_lists(listy[i])

        else:
            result += listy[i]

    return result


# Calling the Functions from Above:
print("recursively flattening a list:", flatten_a_list_of_lists([1,[11,42,[8, 1], 4, [22,21]]]))

print("recursive sum of a simple list:", sum_of_a_list([1,11,42,8, 1, 4, 22,21]))
print("iterative sum of a simple list:", list_sum([1,11,42,8, 1, 4, 22,21]))

print("calling a recursive function with a recursive function to sum a list of lists:", sum_of_a_list(flatten_a_list_of_lists([1,[11,42,[8, 1], 4, [22,21]]]))) # <== Found the sum of a list of lists by writing two functions, then passed one function as a parameter to another function, so as to create more readable code, and deal with multiple recursive functions.

print("recursively summing a list of lists:", sum_list_of_lists([1,[11,42,[8, 1], 4, [22,21]]]))


###############################################################################
print(" ")
###############################################################################

# REFRESHER on indexing of list of lists (lol) and on slicing by implicit integer index:

lol = [1,[11,42,[8, 1], 4, [22,21]]]
print("index 0 is an integer type:", type(lol[0]), lol[0])
print("index 1 is a list type:", type(lol[1]), lol[1])
#print("index 2:", lol[2]) --> this fails; it returns error: out of range.
print("first element of list as a list:", lol[:1])
print("everything of list but first element, as a list:", lol[1:])

###############################################################################
print(">>>>>>>>>>>>>>>>>>>>>> ")
###############################################################################

# Write a function that GENERATES ALL POSSIBLE COMBINATIONS OF 1 AND 0 FOR N BITS. For example, if the function receives 2 as the number of bits, it should produce the following 4 combinations: 00,01,10,11. You cannot use any mathematical operators. This involves PERMUTATION.

def binary_combos(bit_length):
    if bit_length == 0:




print(binary_combos(4))

###############################################################################
print("<<<<<<<<<<<<<<<<<<<<<< ")
###############################################################################

# REFRESHER on expressing an integer as a binary number:

# using bin:
print(bin(173)) #<== adds 0b to the beginning of the binary no... +2 in no. length
print(int(0b10101101)) #  <== 0b means "base 2" (aka the number is in binary)

# binary string / bit pattern in a string:
binary_numb_string = "{0:b}".format(37)
print(binary_numb_string) #'100101'
print(type(binary_numb_string)) # <class 'str'>

# convert the string from above into an integer
binary_num_int = int(binary_numb_string)
print(binary_num_int, "... type:", type(binary_num_int))

# Side note --> if the length of a bit string is b, the number of possible values(N) is 2**b = N. So, if I am given a string that is 4 bits, the number of possible values is 16. (https://en.m.wikipedia.org/wiki/Computer_number_format)






# Note - signed integer vs unsigned integer: signed integer can be both positive and negative; unsigned integer can only be positive. Unsigned uses the leading bit as a part of the value, while the signed version uses the left-most-bit to identify if the number is positive or negative.
