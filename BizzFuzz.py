'''
Created on Mar 19, 2018

@author: sharina
'''


def main():
    bf_range = 100
    fizz_start = 3
    buzz_start = 4
    for i in range (bf_range):
        if (i % fizz_start == 0) and (i % buzz_start == 0):
            print (i, "fizzbuzz")
        elif i % fizz_start == 0:
            print (i, "fizz")
        elif i % buzz_start == 0:
            print (i, "buzz")
        else: print (i)
           
if __name__ == "__main__": main()


''' Output:
0 fizzbuzz
1
2
3 fizz
4 buzz
5
6 fizz
7
8 buzz
9 fizz
10
11
12 fizzbuzz
13
14
15 fizz
16 buzz
17
18 fizz
19
20 buzz
21 fizz
22
23
24 fizzbuzz
25
26
27 fizz
28 buzz
29
30 fizz
31
32 buzz
33 fizz
34
35
36 fizzbuzz
37
38
39 fizz
40 buzz
41
42 fizz
43
44 buzz
45 fizz
46
47
48 fizzbuzz
49
50
51 fizz
52 buzz
53
54 fizz
55
56 buzz
57 fizz
58
59
60 fizzbuzz
61
62
63 fizz
64 buzz
65
66 fizz
67
68 buzz
69 fizz
70
71
72 fizzbuzz
73
74
75 fizz
76 buzz
77
78 fizz
79
80 buzz
81 fizz
82
83
84 fizzbuzz
85
86
87 fizz
88 buzz
89
90 fizz
91
92 buzz
93 fizz
94
95
96 fizzbuzz
97
98
99 fizz



'''