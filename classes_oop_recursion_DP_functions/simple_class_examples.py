'''
This .py file contains examples of OOP
From Udemy's "Rest API Flask and Python" class:
Chapter: Objects in Python
'''

# Classes are always defined in the same way, using class and then the class name. They really always should have the init method, which takes in self, which is the object we're creating, and any number of objects after that.

lottery_player = {
    'name': 'Rolf',
    'numbers': (5,9,12,3,1,21)
    }

# The dictionary above can't do stuff with its own data. We have to tell it to do things, like sum(lottery_player.total()). However, the class LotteryPlayer can do stuff with its own data. This is because whenever we define a method (or an action) inside a class we can have access to self. And, self is what contains the name and numbers.

class LotteryPlayer: # a class is like a blueprint
    def __init__(self):
        self.name = "Rolf"
        self.numbers = (5,9,12,3,1,21)

    def total(self):
        return sum(self.numbers)

player = LotteryPlayer() # This creates an object from the above class. This has whatever properties that were defined in the init method. The properties are self.name and self.numbers. When we create a new object, that object is self. Objects therefore not only have data, but also actions, or methods associated with it, like def total(self).

print(player.name)
print(player.numbers)
print(player.total()) # This prints out the output for the return statement in the total function.

#####################################################################

# Example with multiple instances, but no change to the data of each instance

class LotteryPlayer:
    def __init__(self):
        self.name = "Rolf"
        self.numbers = (5,9,12,3,1,21)

    def total(self):
        return sum(self.numbers)

player_one = LotteryPlayer()
player_two = LotteryPlayer()

print(player_one == player_two) # this shows that each instance is distinct! Output is False, because they are two different entetities that share the same signature.

print(player_one.name == player_two.name) # this shows that player one and player two are both self, but they are differnt instances of self. therefore, they have the same name in this case.

########################################################################

# Example with multiple instances AND different data assigned to the instances
class LotteryPlayer:
    def __init__(self, name):
        self.name = name
        self.numbers = (5,9,12,3,1,21)

    def total(self):
        return sum(self.numbers)

player_one = LotteryPlayer("Rolf")
player_one.numbers = (1,2,3,4,5)
player_two = LotteryPlayer("Pamela")

print(player_one == player_two) # if we kept self.name as equal to "Rolf", this would continue to have a True output. However, by putting self.name = name in the init function, it allows the object's name to become the parameter.

print(player_one.numbers == player_two.numbers) # When the object was created, player's one's numbers were assigned, and then replaced. The tuple was never changed; it was just removed in favor of another. Player_two has the same numbers.

#####################################################################

# Another simple example of OOP with a simple class. Remember, in a way, classes replace the need for dictionaries

class Student:
    def __init__(self, name, school):
        self.name = name
        self.school = school
        self.marks = []

    def ave_marks(self):
        return sum(self.marks) / len(self.marks)

anna = Student("Anna", "MIT")
anna.marks.append(10)
anna.marks.append(30)

print(anna.ave_marks())
print(anna.marks)

######################################################################
print("-----------------")

class Store:
    def __init__(self, name):
        self.name = name
        self.items = []

    def add_items(self, name, price):
        item = {'name': name, 'price': price}
        self.items.append(item)

    def stock_price(self):
        return sum([item['price'] for item in self.items])


table = Store("Table")
