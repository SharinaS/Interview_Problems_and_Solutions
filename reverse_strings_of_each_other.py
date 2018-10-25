'''
Created on Mar 28, 2018

@author: sharina

Write a function that takes two strings and returns True if they are reverses of each other. "ABC" is the reverse of "CBA". Assume 
the two strings are not empty and have the same length.
'''

def are_reverse(string_1, string_2):
    
    for i in range (len(string_1)):
        i_2 = len(string_2) - i - 1
        if string_1[i] != string_2[i_2]:
            return False
    return True

print(are_reverse("sharina", "anirahs"))

