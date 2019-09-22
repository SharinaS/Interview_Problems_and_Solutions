'''
Examples of doing things to tuples
'''
letters = ('a', 'b', 'c')
numbers = (1, 2, 3)

# make a tuple into a list
tuple_to_list_of_lists = [list(i) for i in letters]

into_list = [i for i in numbers]

# make that list_of_lists into a list:
list_of_lists_to_list = [j for i in tuple_to_list_of_lists for j in i]

# make a tuple of integers into a string:
stringy = " ".join(str(i) for i in numbers)



print(tuple_to_list_of_lists) # [['a'], ['b'], ['c']]
print(into_list) #[1, 2, 3]
print(list_of_lists_to_list)
print(stringy) # 1 2 3
