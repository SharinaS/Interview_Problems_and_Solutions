'''
Created on Apr 5, 2018

@author: sharina

Determining Palindromes for Strings and Integers
'''

###############################################################
print("SORTING OUT THE CODE:")
###############################################################
u = "trevor"
print(u[0] == u[-1])      # False

t = "trevor"
print(t[1:-1])    # revo

v = -121
v = str(abs(v))      # cannot use indexing with integers, so turn into a string
print(v[0])    # 1

a = 1221
b = list(str(a))
print(reversed(b))



# This does the same thing...
y = 6789
print(int(''.join(list(reversed(list(str(y)))))))

# ... as this... but this is broken down into the different steps. Note that abs needed if taking into account neg numbers
x = 12345
list_string = list(str(x))  # ['1', '2', '3', '4', '5']
iterable_object = (reversed(list_string))  # <list_reverseiterator object at 0x10d4263c8>
reversed_y = (list(iterable_object)) # ['5', '4', '3', '2', '1']
cleaned_upy = "".join(reversed_y)   # 54321   --------> this is type (str)
print(int(cleaned_upy))

print("^^^^")

e = 12345
print(str(e)) # 12345
print(str(e)[::-1])  # 54321
print(type(str(e)[::-1])) # <class 'str'>
print (str(e) == str(e)[::-1])  # False

e = -12321
print (str(e) == str(e)[::-1])  # False

e = 12321
print (str(e) == str(e)[::-1])  # True


print("^^^^")

###############################################################
print("Recursion to determine Palindrome for a string ############")
'''
This is a solution to find palindromes with RECURSION! Bwahaha! For each scope that is created, the end bits are 
analyzed; the end bits fall off if they are the same, ultimately leaving just 1 or 0 letters, meaning the string
was a palindrome. 
'''
###############################################################

def isPal(s):
    s = s.lower().replace(" ", "") 
    if len(s) <= 1:
        return True
    else:
        return s[0] == s[-1] and isPal(s[1:-1])
print(isPal(("Trev er")))       # False

###############################################################
print("Reversed Function for Strings made into Lists ************")
###############################################################

''' Using REVERSED FUNCTION for LISTS to identify palindromes:
Compared to extended slicing, such as range(1,4)[::-1], reversed() is easier to read, runs faster, and 
uses substantially less memory. Plus it's way more readable'''

x = "hellolleh"
t = str(''.join(reversed(list(str(x)))))

if t == x:
    print (True)
    
else: print("not a palindrome")     #True


###############################################################
print(" ")
print("INTEGER & PALIDROME ************")
###############################################################

'''
LeetCode Problem:
Determine whether an integer is a palindrome. An integer is a palindrome when it reads the same backward as forward.
Input: -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.

Issues to Address:
1. integers are not iterable, have no len() --> solutions: convert to string 
2. negative numbers need to be separated from their neg sign --> solutions: use abs()
3. what if a number has only one digit --> if <= 1, True
4. Using recursion may not be a good idea: At the first recursive loop (after going through the code to get to the else: do 
recursion code), it throws this error: bad operand type for abs(): 'str', referring string_x = str(abs(x))

############
Pseudo Code: 

0. if int is a neg no, it's not a palindrome
1/2. if int as a string is <=1, it's a palindrome
1. turn the integer into a string, into a list
2. use the list function - reversed to make it into an iterator object
3. turn it back into a list, and then into an integer.
4. If the int from step 3 is == to initial integer, it's a palindrome
'''
#***************************************************************
# USING STRINGS
#***************************************************************
# This works fine, one just doesn't need the len(x_string) to make it run!
#===============================================================================
# def integer_palindrome(x):
#     x_string = str(x)
#     
#     if x < 0:
#         return False
#     
#     elif len(x_string) <= 1:
#         return True
#     
#     else:
#         x_rev = int(''.join(list(reversed(list(str(x))))))
#         return x == x_rev 
# 
# print(integer_palindrome(1001))      # True
#===============================================================================

# x is -101 ==> False
# x is 1 ==> True

#***************************************************************
# USING STRINGS -- SIMPLER WAY:                
# Turns out the len(x_string) is not needed to make this work -- here's a simpler way:
#***************************************************************

def simpler_integer_pali(x):
    if x < 0:
        return False
    
    else:
        x_rev = int(''.join(list(reversed(list(str(x))))))
        return x == x_rev

print(simpler_integer_pali(1001))

#***************************************************************
# USING STRINGS WITHOUT CONVERTING BACK TO INTEGER -- THIS IS VERY PYTHONIC :)
#***************************************************************
#===============================================================================
# def integer_to_string_pali(x):
#     if str(x) == str(x)[::-1]:
#         return True
#     else: return False
# print(integer_to_string_pali(2002))
#===============================================================================
# I think this next version is better and more pythonic than the function just above.

def integer_to_string_pali(x):
    return str(x) == str(x)[::-1]

print(integer_to_string_pali(2002))   # True


print(" :) ")

#***************************************************************
# AVOIDING STRINGS ENTIRELY TO SOLVE LEETCODE PROBLEM
#***************************************************************
'''
Thinking:
- breaking up integers means using math and modulo to do so. 1001. %10 gives 1. 
- Can use a while loop to figure out how long the number is. 
- Can use a while loop to reverse the number

Summary of Code:
Start the count at 1, then divide our number by 10. Repeat this, but stop when the number drops below 1. This 
gives a counter of 4. The counter can now be used in the next while-loop to create a reversed number, by
reducing the power that 10 is multiplied by: 10**3, then 10**2, 10**1, 10**0; or 1000, 100, 10, 1.
'''
print("Sorting out the code:")
f = 1001
g = 1001 % 10
print(g)   # 1

listy = []
listy.append(g)
print(listy)  # [1]

h = f // 10
print(h)  # 100

print(h % 10) # 0

# Count the number of digits in a number -- oooooh!
f = 1001
counter = 0
while f > 0:
    counter += 1
    f = f // 10  # 100 # 10, # 1
#print(counter) # 4


#Add up the digits  of a number from last to first:
p = 1234
new_p = 0

while p > 0:
    new_p += p % 10
    p = p // 10
print(new_p)   # 10 (which is 1 + 2 + 3 + 4)


#------------------------------------------------
print("A Solution Posted By Someone on LeetCode")
#------------------------------------------------

n = 1001

digit = n    # 1001
counter = 0  # 4
digit_II = n # 1001
math = 0      # 2  # 1111
    
while digit > 0:
    counter += 1
    digit = digit // 10

while digit_II > 0:   # This reverses the integer
    math += (digit_II % 10) * 10**(counter - 1)
    counter -= 1
    digit_II = digit_II // 10    

if math == n:
    print(True)
else:
    print(False)
    
    
    
#--- Here's the breakdown of the second while loop
#while digit_II > 0:
#    math += (digit_II % 10)     # 1   # 0  # 0  # 1 ==> 2
#    counter -= 1                # 3   # 2  # 1  # 0
#    digit_II = digit_II // 10   # 100 # 10 # 1  # 0

#while digit_II > 0: 
#    math += 10**(counter - 1)    # 1000 # 100  # 1  # 1 ==> 1111
#    counter -= 1                # 3     # 2    # 1  # 0
#    digit_II = digit_II // 10   # 100   # 10   # 1  # 0
    

#------------------------------------------------
print(" ")
print("Official Solution from LeetCode")
'''
converting a number into a string requires extra non-constant space for creating the string.
If the last half of the number after being reversed is the same as the first half of the number, the number is 
a palindrome. 

Edge cases should be taken care of first: All neg numbers are not palindromes. If the last digit is a 0, the first 
digit also has to be a 0 in order for it to be a palindrome, so only 0 satisfies this property.
'''
#------------------------------------------------
# Figuring out the code:
#===============================================================================
# 
# s = 1221
# print(s % 10)   # 1
# print(s // 10)  # 122
# print(s // 10 % 10) # 2
# print (s % 10 * 10 + 2)  # 12 (2 is from s // 10 % 10) --> the reverted number)
#===============================================================================


# translating C# to python... I really like this solution, by the way
#^^^^^^^^^^^^^

def leetcode_sol(x):
    
    if x < 0 or (x % 10 == 0 and x != 0):
        return False
    
    rev_num = 0  
    
    while x > rev_num:
        rev_num = rev_num * 10 + x % 10
        x = x // 10 
        
    return x == rev_num or x == rev_num //10

print(leetcode_sol(505))  # True
    













    


