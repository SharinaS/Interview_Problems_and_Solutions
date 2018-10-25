'''
From LeetCode (easy): Given an array A of non-negative integers, return an array consisting of all the even elements of A,
followed by all the odd elements of A.
You may return any answer array that satisfies this condition.

Example 1:
Input: [3,1,2,4]
Output: [2,4,3,1]
The outputs [4,2,3,1], [2,4,1,3], and [4,2,1,3] would also be accepted.

Note:
1 <= A.length <= 5000
0 <= A[i] <= 5000
'''

def sortArrayByParity(A):
    even=[]
    odd=[]
    for i in A:
        if i%2==0:
            even.append(i)
        else:
            if i%2 != 0:
                odd.append(i)
    return even+odd

print(sortArrayByParity([3,1,2,4,9,15,432,83,7,26]))
