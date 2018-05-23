'''
Created on May 22, 2018

@author: sharina

LEETCODE QUESTION: 
Given a 32-bit signed integer, reverse digits of an integer. Assume we are dealing with an environment which could only store 
integers within the 32-bit signed integer range: [−231,  231 − 1]. For the purpose of this problem, assume that your function 
returns 0 when the reversed integer overflows.
'''

class Solution:
    def reverse(self, x):
     
        x_string = str(abs(x)) 
        rev_string = x_string[::-1]  

        if x < 0:
            new_num = int("-" + rev_string) 
        else:
            new_num = int(rev_string) 

        if new_num > -2**31 and new_num < 2**31-1:
            return new_num
        else: return 0
        
        
        
inst = Solution()
print(inst.reverse(-1234))