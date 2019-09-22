'''
This .py file contains examples of OOP
From Udemy's "Rest API Flask and Python" class:
Chapter: @classmethod and @staticmethod
'''

# *args
# *args allow you to input numbers, which are then transformed into a list. In this case, technically the type is a tuple. You can then use list methods on *args!

def arg_things(*args):
    print(type(args))
    print(args)
    return sum(args)

print(arg_things(3,5,7,12,14,55))


 # kwargs allow input to be put into a dictionary. Solo elements will be ignored. You must have args and kwargs written next to each other, weirdly, otherwise, it will say there are too many arguments when there's only room for 0.
def kwarg_things(*args,**kwargs):
    print(kwargs)
kwarg_things(23,34,34,50, name="Trevor", location="Seattle" )

########################################


# By the way, You can set up the arguments so that the order in which you enter the arguments does not matter

def no_order(name, location):
    print(name)
    print(location)
no_order(location='Seattle', name='Trevor')
