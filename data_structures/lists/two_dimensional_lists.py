'''
manipulating a 2-D list as a matrix... ROWS and COLUMNS are same length
'''

tryit = [[1,2,3],
         [4,5,6],
         [7,8,9]]

# reversing the sub-rows... cool!:
print([i[::-1] for i in tryit])
# [[3, 2, 1], [6, 5, 4], [9, 8, 7]]


# Turn the columns into rows, then reverse the order of the sub-rows (makes the whole original grid rotate clocwise):
col_to_rows = list(zip(*tryit))
    # [(1, 4, 7),
    #  (2, 5, 8),
    #  (3, 6, 9)]
print([i[::-1] for i in col_to_rows])
    # [(7, 4, 1),
    #  (8, 5, 2),
    #  (9, 6, 3)]

# here are the elements from the list using indexing:"
for i in range(len(tryit)):
    for j in range(len(tryit[i])):
        print(tryit[i][j])
'''
1
2
3
4
5
6
7
8
9
'''

# Length of array:
print(len(tryit))
# 3

print("here are the elements from the list again, without using indexing:")

for i in tryit:
    for j in i:
        print(j)
'''
1
2
3
4
5
6
7
8
9
'''


print("Use a list comprehension to flatten the list (make list of lists into one big list):")
print([j for i in tryit for j in i])
# [1, 2, 3, 4, 5, 6, 7, 8, 9]

############# Columns #############

tryit = [[1,2,3],
         [4,5,6],
         [7,8,9]]

# Isolating a column or a couple columns specifically:
column = [i[0] for i in tryit]
print(column)
# [1, 4, 7]
column = [i[1] for i in tryit], [i[2] for i in tryit]
print (column)
# ([2, 5, 8], [3, 6, 9])


#printing out the elements for the second column in the matrix:
for i in tryit:
    print(i[1])
    # 2
    # 5
    # 8

print ("Here are the column elements in order after iterating through them:")
# (Careful to put the i and j in the correct order in print statement.
# If i and j are reversed, given a matrix, you'll get the ROWS, not the columns --> 1,2,3,4,5, etc.

# l = len(tryit)
for i in range(len(tryit)):
    for j in range(len(tryit)):
        print(tryit[j][i])
'''
1
4
7
2
5
8
3
6
9
'''

# Contrast with printing out the rows of the list again:
for i in range(len(tryit)):
    for j in range(len(tryit)):
        print(tryit[i][j])
'''
1
2
3
4
5
6
7
8
9
'''

#### There are 4 ways to make the columns of the matrix into their own list of lists - note that without "list" you
# get tuples.

print("columns made into tuples with zip:")
columns = [i for i in zip(*tryit)]
for i in range(len(columns)):
    print(list(columns[i]))
    # [1, 4, 7]
    # [2, 5, 8]
    # [3, 6, 9]


# Again the same way, but this time set to a variable:")
columns = [i for i in zip(*tryit)]
print(columns)
# [(1, 4, 7), (2, 5, 8), (3, 6, 9)]   --> Tuples!


# Using just list and zip is an easy way to get columns from rows.
print(list(zip(*tryit)))
# [(1, 4, 7), (2, 5, 8), (3, 6, 9)]


# Columns made into a list of lists with zip and comprehension:
print([list(i) for i in zip(*tryit)])
# [[1, 4, 7], [2, 5, 8], [3, 6, 9]]


# Make columns of original 2-D list into their own 2-D list with map, list and zip:
print(list(map(list,zip(*tryit))))
# [[1, 4, 7], [2, 5, 8], [3, 6, 9]]

# Columns made into a list of lists with a comprehension:
colComp = [[row[i] for row in tryit] for i in range(len(tryit[0]))]
print(colComp)
#[[1, 4, 7], [2, 5, 8], [3, 6, 9]]

print(" ")

# Individual columns as their own lists:
for i in range(len(colComp)):
    print(colComp[i])
# [1, 4, 7]
# [2, 5, 8]
# [3, 6, 9]

print(" ")

############# Rows #############

for i in range(len(tryit)):
    print(tryit[i])
'''
[1, 2, 3]
[4, 5, 6]
[7, 8, 9]
'''

print(" ")

# Specify which element not wanted in output, with output being each sublist printed one after another:
for i in range(len(tryit)):
    print([j for j in tryit[i] if j !=3])
'''
[1, 2]
[4, 5, 6]
[7, 8, 9]
'''

# Specify which element not wanted in output, with output being the elements in the 2-d list:
for i in range(len(tryit)):
    for j in tryit[i]:
        if j !=3:
            print(j)
'''
1
2
4
5
6
7
8
9
'''


print("here, the rows are repeated immediately with each row type repeated to equal the # of rows in the entire list")
for i in range(len(tryit)):
    for j in range(len(tryit)):
        print(tryit[i])
'''
[1, 2, 3]
[1, 2, 3]
[1, 2, 3]
[4, 5, 6]
[4, 5, 6]
[4, 5, 6]
[7, 8, 9]
[7, 8, 9]
[7, 8, 9]
'''
print('''here, the entire list is printed as indiividual rows in order, and then repeated so the # of rows
equal the # elements in the original list''')
for i in range(len(tryit)):
    for j in range(len(tryit)):
        print(tryit[j])


print(" ")

############# Diagonals #############

l = len(tryit)
print(l)

print("diagonal values from upper L to lower R in the matrix:")
for i in range(len(tryit)):
    print(tryit[i][i])

print("diagonal values from upper R to lower L in the matrix:")
for i in range(l-1,-1,-1):
    print(tryit[l-1-i][i])

print("diagonal values from lower L to upper R:")
for i in range(len(tryit)):
    print(tryit[len(tryit)-1-i][i])

print(" ")

'''sums of the different parts of the list of lists'''

total = 0
for i in range(len(tryit)):
    for j in range(len(tryit[i])):
        total += tryit[i][j]
print("The sum of the entire list using indexing: {}".format(total))

totalagain = 0
for i in tryit:
    for j in i:
        totalagain += j
print("sum of entire list w/o indexing: {}".format(totalagain))

anothertryit = [[4, 7], [1, 1]]
x = 0
for row in anothertryit:
    for item in row:
        x += item
print(x) #adds up the entire list of lists ==> 13

compareWithSimpleList = [4, 7, 2]
x = 0
for item in compareWithSimpleList:
    x += item
print(x) #sums up items in the 1-D list, which in this case is 13.

print("sum of the entire list using a comprehension:")
print(sum([j for i in tryit for j in i]))
# 45

for i in range(len(tryit)):
    print("sum of each row: {}".format(sum(tryit[i])))
    # sum of each row: 6
    # sum of each row: 15
    # sum of each row: 24
# Can't use total += when summing each row in this case, because the things to be added to total must be integers or slices, not sublists.

total = 0
for i in range(len(tryit)):
    total += tryit[i][i]
print("the sum of the diagonal from upper L to lower R is: {} ".format(total))
# the sum of the diagonal from upper L to lower R is: 15

total = 0
for i in range(len(tryit)):
    total += tryit[l-1-i][i]
print("sum of the diagonal from lower L to upper R: {}".format(total))
# sum of the diagonal from lower L to upper R: 15

print("sum of each column:")
colSums = [i for i in zip(*tryit)]
for i in range(len(colSums)):
    print(sum(colSums[i]))
    # 12
    # 15
    # 18


print("total sum of the newly made list of lists from the columns of tryit:")
col_sums = [i for i in zip(*tryit)]
print(sum([j for i in col_sums for j in i]))

for i in range(len(column)):
    print("column sum of manually made columns is {} ".format(sum(column[i])))
    #column sum of manually made columns is 15
    #column sum of manually made columns is 18

##############

a = [[1, 2, 3, 4], [5, 6], [7, 8, 9]]

for row in a:
    print(' '.join([str(elem) for elem in row]))

# 1 2 3 4
# 5 6
# 7 8 9

################ Adding up all the elements
a = [[1, 2, 3, 4], [5, 6], [7, 8, 9]]
s = 0
for i in range(len(a)):
    for j in range(len(a[i])):
        s += a[i][j]
print(s)
# 45

a = [[1, 2, 3, 4], [5, 6], [7, 8, 9]]
s = 0
for row in a:
    for elem in row:
        s += elem
print(s)
# 45
################ Creating a 2-D list / grid

n = 3
m = 4
a = [[0] * m for i in range(n)]
print(a)
# [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]

################# Building 2-D lists

n = 4
a = [[0] * n for i in range(n)]
for i in range(n):
    for j in range(n):
        if i < j:
            a[i][j] = 0
        elif i > j:
            a[i][j] = 2
        else:
            a[i][j] = 1
for row in a:
    print(' '.join([str(elem) for elem in row]))
# 1 0 0 0
# 2 1 0 0
# 2 2 1 0
# 2 2 2 1

#Another Way to do it:

n = 4
a = [[0] * n for i in range(n)]
print(a)
#[[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]

for i in range(n):
    for j in range(0, i):
        a[i][j] = 2
    a[i][i] = 1
    for j in range(i + 1, n):
        a[i][j] = 0
for row in a:
    print(' '.join([str(elem) for elem in row]))
# 1 0 0 0
# 2 1 0 0
# 2 2 1 0
# 2 2 2 1
################################################################################
print(" ")
print(" ")
################# Building 2-D lists by appending a list to a list

lista = []
lista2 = []
lista3 = [3, 4]

lista2.append(1)
lista2.append(2)
print(lista2)

lista.append(lista2)
print(lista)

lista.append(lista3)
print(lista)

lista.pop(0)
print(lista)

print("lista2 is", lista2) # [1,2]
print("lista3 is", lista3) # [3,4]
print("lista is", lista) # [[3,4]]

lista4 = [[i for i in lista2]]
print("lista4 is", lista4)



################################################################################
print(" ")
print(" ")
#########################################################
# making and isolating sub-lists from a 2D list:
# making 3x3 lists from the 6x6 list

grid = [['.', '.', '1', '.', '4', '.', '.', '2', '.'],
        ['.', '.', '6', '.', '.', '.', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '1', '.', '.', '.'],
        ['.', '6', '7', '.', '.', '.', '.', '.', '9'],
        ['.', '.', '.', '.', '.', '.', '8', '1', '.'],
        ['.', '3', '.', '.', '.', '.', '.', '.', '6'],
        ['.', '.', '.', '.', '.', '7', '.', '.', '.'],
        ['.', '.', '.', '5', '.', '.', '.', '7', '.']]

# Split the block of rows into 3's (since this is an original block of 9 rows, it turns it into 3 blocks):
'''
First, we establish how many sub-lists we want in each new 2D list, by establishing where to start-stop-skip, with the
for loop and range function. So, we say, start at 0, check the length of the array (9), then essentially divide 9 by 3, returning
0, 3, 6 as the numbers we'll plug into the next part of the instructions, since we're skipping every 3 numbers when we count up
the length.

Then, slice away at the grid, using the values for i we have created, to create 3 sub-lists for every new 2D list. Because
the original grid is 9 rows, it breaks the grid into 3 parts. We first start at i==0, so we start at grid[0], and slice off everything
that comes after grid[0+3]... which is the 4th row onward. So, we keep the 1st, 2nd and 3rd rows. We're not done iterating,
so then we increase i to 3, which means we start our new sub-row at grid[3], and slice off everything after grid[3+3]. That leaves
us the 4th, 5th and 6th rows. We finish up the iteration by using i==6, which means we are left with the 7th, 8th and 9th rows
as our last sub-list.
'''
for i in range(0,len(grid), 3):  #0 #3  #6
    print(i)
    print(grid[i:i+3]) # slices based on i being first 0, then 3, then 6.

    # 0
    # [['.', '.', '1', '.', '4', '.', '.', '2', '.'], ['.', '.', '6', '.', '.', '.', '.', '.', '.'], ['.', '.', '.', '.', '.', '.', '.', '.', '.']]
    # 3
    # [['.', '.', '.', '.', '.', '1', '.', '.', '.'], ['.', '6', '7', '.', '.', '.', '.', '.', '9'], ['.', '.', '.', '.', '.', '.', '8', '1', '.']]
    # 6
    # [['.', '3', '.', '.', '.', '.', '.', '.', '6'], ['.', '.', '.', '.', '.', '7', '.', '.', '.'], ['.', '.', '.', '5', '.', '.', '.', '7', '.']]

    # So, the snippet when i==0 looks like this, when manually put in a grid:
    # [['.', '.', '1', '.', '4', '.', '.', '2', '.'],
    # ['.', '.', '6', '.', '.', '.', '.', '.', '.'],
    # ['.', '.', '.', '.', '.', '.', '.', '.', '.']]

print(" ")

# ... In contrast, split the block of rows into 2's
for i in range(0,len(grid), 2):
    print(i)
    print(grid[i:i+2])

    # 0
    # [['.', '.', '1', '.', '4', '.', '.', '2', '.'], ['.', '.', '6', '.', '.', '.', '.', '.', '.']]
    # 2
    # [['.', '.', '.', '.', '.', '.', '.', '.', '.'], ['.', '.', '.', '.', '.', '1', '.', '.', '.']]
    # 4
    # [['.', '6', '7', '.', '.', '.', '.', '.', '9'], ['.', '.', '.', '.', '.', '.', '8', '1', '.']]
    # 6
    # [['.', '3', '.', '.', '.', '.', '.', '.', '6'], ['.', '.', '.', '.', '.', '7', '.', '.', '.']]
    # 8
    # [['.', '.', '.', '5', '.', '.', '.', '7', '.']]

print(" ")

# Back to the original example:
for i in range(0,len(grid), 3):  #0 #3  #6
    first_chop = grid[i:i+3]
    #print(first_chop)

    for j in range(0,len(grid[0]), 3): #0 #3 #6
        second_chop = [x[j:j+3] for x in first_chop]
        #print(second_chop)
        '''
[['.', '.', '1', '.', '4', '.', '.', '2', '.'], ['.', '.', '6', '.', '.', '.', '.', '.', '.'], ['.', '.', '.', '.', '.', '.', '.', '.', '.']]
[['.', '.', '1'], ['.', '.', '6'], ['.', '.', '.']]
[['.', '4', '.'], ['.', '.', '.'], ['.', '.', '.']]
[['.', '2', '.'], ['.', '.', '.'], ['.', '.', '.']]
[['.', '.', '.', '.', '.', '1', '.', '.', '.'], ['.', '6', '7', '.', '.', '.', '.', '.', '9'], ['.', '.', '.', '.', '.', '.', '8', '1', '.']]
[['.', '.', '.'], ['.', '6', '7'], ['.', '.', '.']]
[['.', '.', '1'], ['.', '.', '.'], ['.', '.', '.']]
[['.', '.', '.'], ['.', '.', '9'], ['8', '1', '.']]
[['.', '3', '.', '.', '.', '.', '.', '.', '6'], ['.', '.', '.', '.', '.', '7', '.', '.', '.'], ['.', '.', '.', '5', '.', '.', '.', '7', '.']]
[['.', '3', '.'], ['.', '.', '.'], ['.', '.', '.']]
[['.', '.', '.'], ['.', '.', '7'], ['5', '.', '.']]
[['.', '.', '6'], ['.', '.', '.'], ['.', '7', '.']]
'''
        second_chop = [first_chop[k][l] for k in range(len(first_chop)) for l in range(len(first_chop[k]))]
        print(second_chop)
