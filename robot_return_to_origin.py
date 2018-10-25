'''
LeetCode Problem: Robot Returns to Origin
There is a robot starting at position (0, 0), the origin, on a 2D plane. Given a sequence of its moves,
judge if this robot ends up at (0, 0) after it completes its moves.

The move sequence is represented by a string, and the character moves[i] represents its
ith move. Valid moves are R (right), L (left), U (up), and D (down). If the robot returns
to the origin after it finishes all of its moves, return true. Otherwise, return false.

Note: The way that the robot is "facing" is irrelevant. "R" will always make the robot move
to the right once, "L" will always make it move left, etc. Also, assume that the magnitude of
the robot's movement is the same for each move.

Example 1:
Input: "UD"
Output: true
Explanation: The robot moves up once, and then down once. All moves have the same magnitude, so it
ended up at the origin where it started. Therefore, we return true.

Example 2:
Input: "LL"
Output: false
Explanation: The robot moves left twice. It ends up two "moves" to the left of the origin. We return false
because it is not at the origin at the end of its moves.

########################


Set R, L, U, D to numbers, indicating x and y axis travel
R = +1
U = +1
L = -1
D = -1
Create a dictionary with keys being directions and values being values.
A while loop can be used, limited by the length of the string, so a pointer can move along the string,
and correlating to the dictionary. If R or L exist in the dict, put their values into a list that shows the
x coordinates. Put the values for U and D in the list that shows the y coordinates. sum each list, so
if the sum of both lists is 0, the robot is home (back at (0,0))
'''
def robot(moves):
    directions_dict = {"R":1, "L":-1,"U":1, "D":-1}
    i = 0
    x_values = []
    y_values = []
    while i < len(moves):
        if moves[i] == "R" or moves[i]=="L":
            x_values.append(directions_dict[moves[i]])
        else:
            y_values.append(directions_dict[moves[i]])
        i=i+1
    if sum(x_values) == 0 and sum(y_values) == 0:
        return True
    else:
        return False
print(robot("RRDD"))

'''
Here's code written on LeetCode that takes into account python's count method. It's O(n) complexity, and
uses built in method, which could be less buggy. This one is much faster than my while loop solution above.
20ms, versus above was 248ms.
'''
def robot_one_liner(moves):
    return moves.count("L") == moves.count("R") and moves.count("U") == moves.count("D")
print(robot_one_liner("RRDD"))
