''' Notes from Udemy's Rest API Flask and Python Class by Jose Salvatierra

Notes on passing a function as a parameter to another method -- Very useful for generalizing code and for making nice readable codeself.

Part of a style of programming called declarative programming, perhaps part of functional programming. It's especially useful when we want to work with data.

'''

def methodception(another): # This is a method we're going to call
    return another()

def add_two_numbers(): # another method
    return 35 + 77

print(methodception(add_two_numbers)) # note that those two opening and closing brackets at end are missing here - instead we're passing the method add_two_numbers as a parameter to methodception, and methodception is going to run that method. It will run up under the function area of methodception, with the "return another()," and then it will run add_two_numbers so it can return 35 + 77.
####################################################
print(" ")
####################################################
''' This style of programming particularly useful when working with data'''

my_list = [13, 56, 77, 484, 213]

# can remove an element the basic way:
my_list.remove(13)
print(my_list)

''' built-in FILTER() method:
Allows you to keep only some values. Takes in a function and an iterable - the function is lambda, and the iterable is my_list. Note - when you call the filter function, you have to surround it by list() if you want it to come out in the form of a list.
We're saying: we're going to filter my_list using the function lambda x: x!=13'''
# remove all the elements that are even:
print(list(filter(lambda x: x != 13, my_list)))

'''Compare filter with list comprehension:
Note that many Python programmers prefer list comprehension, since it's easily read and can be easier to write. However, list comprehension is unique to python programming and a few other programming languages, however the concept of filter is present in many other programming languages. So, stick with filter if working with other programmers in other languages. If performance is an issue, list comprehension may be better, though, must investigate.'''
# can do the same with list comprehension as what we did with the filter method:
print([x for x in my_list if x != 13])
