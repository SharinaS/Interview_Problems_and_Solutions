'''Interview Problem from Udemy's Python for Data Structures and Interviews
Problem: Unique Characters in String: Given a string, determine if it is comprised of all unique characters. For example, the string 'abcde' has all unique characters and should return True. The string 'aabcde' contains duplicate characters and should return False.
'''
# My Solution -- let interviewer know you can do this, but ideal interview solution is below.
def dups (stri):
    setty = set(stri)
    if len(setty) == len(stri):
        return True
    else:
        return False
print(dups("abcdddefg"))

# Class pythonic solution - not ideal for interview, but great in real life
def dups2(stri):
    return len(set(stri)) == len(stri)
print(dups2("abcde"))


# My Solution, and class solution.
def dup_checker (stri):
    setty = set()
    for char in stri:
        if char not in setty:
            setty.add(char)
        elif char in setty:
            return False
    return True # if it never returns false in the if statement, we know we can return true
print(dup_checker("abcdeeef"))
