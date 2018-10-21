'''
Description: (From LeetCode):
The Hamming distance between two integers is the number of positions at which the corresponding bits are different.
Given two integers x and y, calculate the Hamming distance.
Note:
0 ≤ x, y < 231.
Example:
    Input: x = 1, y = 4
    Output: 2
    Explanation:
    1   (0 0 0 1)
    4   (0 1 0 0)
           ↑   ↑
    The above arrows point to positions where the corresponding bits are different.

Solution created by: Sharina Stubbs
Last revised: October 1, 2018
'''

def hamming_distance(x,y):
    # convert numbers into binary
    x = '{0:032b}'.format(x)
    y = '{0:032b}'.format(y)
    # merge the strings using zip(), and compare the concatenation of each tuple.
    zipped_xy = zip(x,y)
    num_string = []
    for x,y in zipped_xy:
        if x+y=="01" or x+y=="10":
            num_string.append(x+y)
    return len(num_string)

print(hamming_distance(1,4))

'''
REMEMBER:
• When comparing elements of two lists/strings,etc, immediately think about zip()
• Addition of strings leads to concatenation, not math.

NOTES ON CONVERTING INTEGER TO BINARY:
{} places a variable into a string
0 takes the variable at argument position 0
: adds formatting options for this variable (otherwise it would represent decimal 6)
032 formats the number to 32 digits zero-padded on the left (which accomidates for the problem range)
b converts the number to its binary representation

BREAKDOWN OF ZIP:
    zipped_xy = zip(x,y)   <-- if x,y == 1,4
    for i in zipped_xy:
        print (i)
    output is the following:
('0', '0')
('0', '0')
('0', '0')
('0', '0')
('0', '0')
('0', '0')
('0', '0')
('0', '0')
('0', '0')
('0', '0')
('0', '0')
('0', '0')
('0', '0')
('0', '0')
('0', '0')
('0', '0')
('0', '0')
('0', '0')
('0', '0')
('0', '0')
('0', '0')
('0', '0')
('0', '0')
('0', '0')
('0', '0')
('0', '0')
('0', '0')
('0', '0')
('0', '0')
('0', '1')
('0', '0')
('1', '0')
'''

# List concatenation of same problem from anonther programmer on LeetCode: I like this one; it
# helped me build my code above.

def hammingDistance(x, y):
    binx = '{0:032b}'.format(x)
    biny = '{0:032b}'.format(y)
    return sum([1 for x,y in zip(binx,biny) if x!=y])
print(hammingDistance(1,4))
