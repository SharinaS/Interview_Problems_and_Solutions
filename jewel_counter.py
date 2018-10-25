'''
LEETCODE:
You're given strings J representing the types of stones that are jewels, and S representing the stones you have.
Each character in S is a type of stone you have.  You want to know how many of the stones you have are also jewels.

The letters in J are guaranteed distinct, and all characters in J and S are letters.
Letters are case sensitive, so "a" is considered a different type of stone from "A".

Example 1:

Input: J = "aA", S = "aAAbbbb"
Output: 3
Example 2:

Input: J = "z", S = "ZZ"
Output: 0
Note:

S and J will consist of letters and have length at most 50.
The characters in J are distinct.
'''

def count_jewels(S,J):
    counts = {}
    jewels = []

    for i in S:
        if i in counts:
            counts[i] += 1
        else:
            counts[i] = 1

    for key, value in counts.items():
        if key in J:
            jewels.append(value)

    return sum(jewels)

print(count_jewels("ZZ", "z"))
