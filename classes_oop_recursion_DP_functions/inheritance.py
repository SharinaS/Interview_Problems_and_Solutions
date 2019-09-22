'''
This .py file contains examples of OOP
From Udemy's "Rest API Flask and Python" class:
Chapter: @classmethod and @staticmethod

It works closely with the args_and_kwargs.py file, as args and kwargs are desperately needed when passing in an unlimited number of positional arguments to an inherited class.
'''

class Student:
    def __init__(self, name, school):
        self.name = name
        self.school = school
        self.marks = []

    def average(self):
        return sum(self.marks) / len(self.marks)

    def friend(self, friend_name):
        return Student(friend_name, self.school)

razzle = Student("Razzle", "Oxford")
friend = razzle.friend("Trevor")
print(friend.name)
print(friend.school)

#############
print("^^^^^^^^^^^^^^^^^^^^^^")
# Basic example of inheritence:

class WorkingStudent(Student): # think of this as though we copied and pasted the Student class, which is the super class. When we inherit, we can re-implement the init method with more stuff.
    def __init__(self, name, school, salary): # since working student inherits from student, we must call Student's init method by using super().__init...
        super().__init__(name, school) # this is like copy-paste from above.
        self.salary = salary

anna = WorkingStudent("Anna", "Oxford", 20.00)
print(anna.salary) #20

#########################################################################
print(" ")
############################################################################
 # The code can get really complicated when you try to add numerous arguments to an inherited class. So, when you don't know how many arguments may be added, or it's more than one new one, use *args and cls! see args file, but essentially args converts whatever number of elements into a tuple, so you don't have to worry about reserving space for x number of arguments.

class CoolStudent:
    def __init__(self, name, school):
        self.name = name
        self.school = school
        self.marks = []

    def average(self):
        return sum(self.marks) / len(self.marks)

    @classmethod
    def friend(cls, origin, friend_name, *args, **kwargs):
        return cls(friend_name, origin.school, *args, **kwargs)


class CoolWorkingStudent(CoolStudent):
    def __init__(self, name, school, salary, job_title):
        super().__init__(name, school)
        self.salary = salary
        self.job_title = job_title

anna = CoolWorkingStudent("Anna", "Oxford", 20.00, "Airline Pilot")
print(anna.salary)

friend = CoolWorkingStudent.friend(anna, "Trevor", 80.00, job_title = "Airline Pilot")
print(friend.name)
print(friend.school)
print(friend.salary)
