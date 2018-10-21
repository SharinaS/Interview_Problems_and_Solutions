'''
Created on Feb 28, 2018

@author: sharina


 FIBONACCI SEQUENCE
simple fibonacci series
the sum of two elements defines the next set
A Fibonacci sequence is the integer sequence of 0, 1, 1, 2, 3, 5, 8....

**** For Fibonacci and classes and iterators, check out website http://www.diveintopython3.net/iterators.html for a nice
discussion ****
'''

print("Using Class, Iterator and Fibonacci:")
class Fibonacci():
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def series(self):
        while(True):
            yield(self.b)
            self.a, self.b = self.b, self.a + self.b

f = Fibonacci(0, 1)
for r in f.series():
    if r > 100: break
    print(r, end=' ')



print("\nWhile loop and Fibonacci:")
a, b = 0, 1
while b < 10000:
    print(b)
    a, b = b, a + b  # a will now be 1, and b will also be 1, (0 + 1)


# The above code has the same output as the below code (which is less pythonic)

def fibonacci_broken_down(n):
    follower = 0
    leader = 1

    while leader < n:
        print (leader)
        holder = follower
        follower = leader
        leader = follower + holder

fibonacci_broken_down(1000)

###################################

'''Recursion Examples ----> Folks "always talk about" Fibonacci and factorials when recursion comes up as a topic'''

def recur_fibo(n):
    #Recursive function to print Fibonacci sequence
    if n <= 1:
        return n
    else:
        return(recur_fibo(n-1) + recur_fibo(n-2))

nterms = 10   # Change this value for a different result
if nterms <= 0:     # check if the number of terms is valid
    print("Please enter a positive integer")
else:
    print("Fibonacci sequence:")
    for i in range(nterms):
        print("recursion and fibonacci: {}".format(recur_fibo(i)))

#OR, here's another way to write recursion and fibonacci:
#  this form requires a lot of time as n gets bigger. In fact, this is O(2n) in time:
def F(n):
    if n == 0: return 0
    elif n == 1: return 1
    else: return F(n-1)+F(n-2)
n = 10
for i in range(n):
    print(F(i))


print("\nAnother If-elif recursion and Fibonacci")
def fib(n):
    if n <= 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)

n = 20
for i in range (n):
    print(fib(i))

'''
1
1
2
3
5
8
13
21
34
55
89
144
233
377
610
987
1597
2584
4181
6765
'''



''' Output
Using Class and Fibonacci:
1 1 2 3 5 8 13 21 34 55 89
While loop and Fibonacci:
1
1
2
3
5
8
13
21
34
55
89
144
233
377
610
987
1597
2584
4181
6765
*@*@*@*@*@*
1
1
2
3
5
8
13
21
34
55
89
144
233
377
610
987
Fibonacci sequence:
recursion and fibonacci: 0
recursion and fibonacci: 1
recursion and fibonacci: 1
recursion and fibonacci: 2
recursion and fibonacci: 3
recursion and fibonacci: 5
recursion and fibonacci: 8
recursion and fibonacci: 13
recursion and fibonacci: 21
recursion and fibonacci: 34
0
1
1
2
3
5
8
13
21
34



'''
