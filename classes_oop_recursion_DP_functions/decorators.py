'''
This .py file contains examples of OOP
From Udemy's "Rest API Flask and Python" class:
Chapters: "@classmethod and @staticmethod", "Decorators in Python", and "Advanced Decorators"
'''
# Use decorators when you don't need to use self.

# Class method:
# This removes the need for self in the function name. However, you must pass in "cls." When we call something a class method, what we pass is not the object, but the class, Student. Within cls is Student. This is shown by the second print statement here. Note that __main__ is b/c we are within the main file, while the class is Student. Note that with this method, you can now simply call the go-to-school function by writing Student.go_to_school, given it doesn't matter whether anna or rolf calls it, as it's the same regardless. So, might as well just call it with the class itself.
class Student:
    def __init__(self, name, school):
        self.name = name
        self.school = school
        self.marks = []

    def ave_marks(self):
        return sum(self.marks) / len(self.marks)

    @classmethod
    def go_to_school(cls):
        print("I'm going to school")
        print("I'm a {}".format(cls))

anna = Student("Anna", "MIT")
anna.go_to_school()

# Static Method:
# No need to pass in anything; it allows you to not have to put in self or any other arguments. Note that with this method, you can now simply call the go-to-school function by writing Student.go_to_school, given it doesn't matter whether anna or rolf calls it, as it's the same regardless. So, might as well just call it with the class itself. In the static method, all objects share the same method - they all print the same thing out.

class Student:
    def __init__(self, name, school):
        self.name = name
        self.school = school
        self.marks = []

    def ave_marks(self):
        return sum(self.marks) / len(self.marks)

    @staticmethod
    def go_to_school():
        print("I'm going to school")

anna = Student("Anna", "MIT")
rolf = Student("Rolf", "Oxford")
Student.go_to_school()

####################################################################################
print("^^^^^^^^^^^^^^^^^^^^^^^^^")
#This is a class problem which required filling in some blanks to the code. The goal was to practice working with the decorators classmethod and staticmethod.

class Store:
    def __init__(self, name): # the init method has two properties - name and items.
        self.name = name
        self.items = []

    def add_item(self, name, price):
        self.items.append({
            'name': name,
            'price': price
        })

    def stock_price(self):
        total = 0
        for item in self.items:
            total += item['price']
        return total

    @classmethod
    def franchise(cls, store):
        # Return another store, with the same name as the argument's name, plus " - franchise" - have to create a store object that includes franchise.
        new_store = Store(store.name + " - franchise") # note that you can replace Store(store.name...) with cls(store.name...) since cls is equivalent to the class name
        return new_store


    @staticmethod
    def store_details(store):
        # Return a string representing the argument
        # It should be in the format 'NAME, total stock price: TOTAL'
        return '{}, total stock price: {}'.format(store.name, int(store.stock_price()))

store = Store("Whole Foods")
store2 = Store("PCC")
store2.add_item("Carrots", 2.99)

#####################################################################
# Decorators - in order to declare / create a decorator, you have to use a decorator.
# Decorators are a function that is called before another function. In order to write decorators, we need to import functools library. A decorator will use the library to do its thing.
#####################################################################
''' Decorators that do not accept arguments:'''

import functools

# decorator is defined:
def my_decorator(func):
    @functools.wraps(func)
    def function_that_runs_func():
        print("In the decorator!")
        func()
        print("After the decorator!")
    return function_that_runs_func

    # def function_that_runs_fun wraps around the func() that is passed in as a parameter. this way you can do things before or after the function.

# apply the decorator to my_function():
@my_decorator
def my_function():
    print("I'm the function!")

my_function()

# my_function executes, and then my_function is passed to my_decorator as func (in the first line of the def my_function). Then, a function - function function_that_runs_fun is created that wraps around it. It will print "I'm a decorator," then it will run func(), which is the parameter to def my_decorator, which therefore is def my_function(), which will then print "I'm a function!". Once func() has initiated, "After the decorator will print out" The return function function_that_runs_fun is the function that replaces my_function. Note that the decorator should always call the function, seen in this case, since the decorator calls my_function(). So, in summary, you're passing your function to the decorator, then you're wrapping another function around it, then returns a value that is what is replacing your function.

#####################################################################
print(" ")
#####################################################################

'''More complex decorators: DECORATORS THAT ACCEPT PARAMETERS --> These accept arguments.

Decorators with arguments:
- very useful if we need to pass in A USER'S PERMISSIONS in a website with an admin page.
- insert elements to a database, but only if they match a certain criteria
- admin page shown to only certain people
- careful not to overuse them

Sometimes your function may take in parameters, such as the x,y in the def my_function_too. Therefore, your decorator - the def function_that_runs_func, should always take in args and kwargs, and you should always pass args and kwarks into the function, func() - under else: -- that way, when we call the function, with numbers such as  - my_function_too at the bottom - we can have arguments passed in. So, when we call the function my_function_too, they will be passed into def function_that_runs_func, and they will be passed to func - in the if/else clause. So, to recap, my_function_too is the func that's found in the else statement. the 57 is the "number" in def decorator_with_arguments.
'''

# note that import functools occurred at the top of this page

def decorator_with_arguments(number):
    def my_decorator(func):
        @functools.wraps(func)
        def function_that_runs_func(*args, **kwargs):
            print("In the decorator!")
            if number == 57:
                print("Not running the function!")
            else:
                func(*args, *kwargs)
            print("After the decorator!")
        return function_that_runs_func
    return my_decorator
# The above has 3 levels of functions nested one inside another. It doesn't go deeper than this though.
# In the above portion, we have access to the number, so we can create if/then statements based on what number is used.

# we can create a decorator that will accept arguments:
@decorator_with_arguments(56) # the decorator is getting a set of arguments. This is very useful if we need to pass in A USER'S PERMISSIONS in a website with an admin page.
def my_function_too(x,y):
    print(x + y)


my_function_too(57, 67)
