''' Notes from Udemy's Rest API Flask and Python Class by Jose Salvatierra

NOTES ON:
- Lambda functions - An anonymous function. Lambda functions are written all in one line.
- Built-in filter method
'''

def methodception(another): # This is a method we're going to call
    return another()

print(methodception(lambda: 35 + 77)) # lambda function is what we're passing in methodception, and then that is running the function. The lamda function is the same as how we used def add_two_numbers from "passing_functions_as_parameters" file, but it doesn't have a name.

##################################################################
''' This style of programming particularly useful when working with data'''

my_list = [13, 56, 77, 484, 213]

# remove an element the basic way:
my_list.remove(13)
print(my_list)

'''... or use the built-in filter method:
Allows you to keep only some values. Takes in a function and an iterable - the function is lambda, and the iterable is my_list. Note - when you call the filter function, you have to surround it by list() if you want it to come out in the form of a list
We're saying: we're going to filter my_list using the function lambda x: x!=13'''
# remove all the elements that are even.
print(list(filter(lambda x: x != 13, my_list)))

# This is identical to the non-lambda function:
def not_thirteen(x):
    return x != 13
print(list(filter(not_thirteen, my_list)))

##################################################################

'''
Define lambda function with one parameter, x. The body of the function is x * 3.
'''
(lambda x: x * 3)(5)

# This lambda function is identical to:
def identical(x):
    return x * 3
identical(5)
