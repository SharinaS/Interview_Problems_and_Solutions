'''
Created on Jun 9, 2018

@author: sharina

DESCRIPTION FROM LEETCODE: "Roman to Integer"
Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.
For example, two is written as II in Roman numeral, just two one's added together.
Twelve is written as, XII, which is simply X + II. The number twenty seven is written as XXVII, which is XX + V + II.
Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII.
Instead, the number four is written as IV. Because the one is before the five we subtract it making four.
The same principle applies to the number nine, which is written as IX.

There are six instances where subtraction is used:
- I can be placed before V (5) and X (10) to make 4 and 9.
- X can be placed before L (50) and C (100) to make 40 and 90.
- C can be placed before D (500) and M (1000) to make 400 and 900.

Given a roman numeral, convert it to an integer. Input is guaranteed to be within the range from 1 to 3999.

'''

# PLAYING WITH THE CODE:
dict_roman = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}

# Subtraction using dictionaries (wow)
minus_values = dict_roman["V"] - dict_roman["I"] # this is 5 - 1
print(minus_values)  # 4

plus_values = dict_roman["C"] - dict_roman["V"]    # this is 100 - 5
print(plus_values) # 95

sample_length = "IX"
print(len(sample_length)) # 2


###################################################################################
print(" ")
###################################################################################
'''Got confused and starting making it more complicated... so had to look at
other people's code. Created roman_to_integer function based on another's code that uses mathematical patterns based
on roman numeral rules, not the rules themselves, to create this simple function.

Lesson 1: Look at the patterns
of the numbers, beyond the human expressed rules. Lesson 2: Easily create an element to follow another element by setting
the follower initially to a very high value, which is then replaced with the initial value of the main element at the end of the
for loop. That way the next for loop starts with the follower being what the main element was, and the main element now being
the next one down the line. They can then be compared and actions ordered based on their relationship.

if you add up the elements first, to stay compliant with the core code, and then do the subtraction, you get:
In IV, 16-(1*2) = 14
In XL, 60-(10*2) = 40
In CD, 600-(100*2) = 400

First, write a loop that includes code to do the meat of the issue: Add!
Then, one of the first steps, after creating the core code, is creating an impossible variable (has a value beyond what
would ever be found, given the scenario). Then, make it the trailing element in the for-loop by immediately setting it
equivalent to the first element. Then, the next element is compared to it, which is important when the element follows a lesser value.'''



def roman_to_integer(s):
    dict_roman = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    integer_total = 0
    following_roman = "M"

    for roman in s:
        if dict_roman[roman] > dict_roman[following_roman]:
            integer_total -= dict_roman[following_roman]*2 # subtract the following element, but doubled.
        integer_total += dict_roman[roman] # here is the basic code: add! The program starts here.
        following_roman = roman  # The program then jumps to here, to set the follower to what the initial element was.

    return integer_total

print(roman_to_integer("CD")) # 400


###################################################################################
print(" ")
###################################################################################
''' This one is inspired by another person's code, but I removed some code and compacted code to make it mine'''

def roman_to_integer2(s):
    dict_roman = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    integer_total = 0
    following_roman = ""

    for roman in s:
        if following_roman in list('IXC') and dict_roman[following_roman] < dict_roman[roman]:

            #integer_total -= dict_roman[following_roman]
            integer_total += dict_roman[roman] - 2*(dict_roman[following_roman])

        else:
            integer_total += dict_roman[roman]

        following_roman = roman

    return integer_total

print(roman_to_integer2("XXIV"))  #24
