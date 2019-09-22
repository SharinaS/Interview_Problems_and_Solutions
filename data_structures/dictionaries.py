'''
==> Dictionaries are also known as associative arrays <==
in Python shell, type in: help(dict) to get all the methods and what they do'''


dicty = {'{': '}', '(': ')', '[':']'}
if dicty['{'] == '}':
    print("It's a balanced thing!")

print("*******************")

# Making the dictionary into a string, with keys followed by values
dicty = {"A":2, "b":1}
stringy = str(dicty)
print(stringy)

new_stringy = stringy.replace(":", "")
print(new_stringy)


print("*******************")
#MAKING A DICTIONARY
address = {'Bob':'1234 main', 'Jim':1234}
print (address)

#ADDING TO A DICTIONARY
inventory = {}
inventory['apples'] = 140
inventory['bananas'] = 15
inventory['grapes'] = 2
inventory['peaches'] = 60
print(inventory)

print(" ")

#OUTPUT A VALUE FROM A KEY IN THE DICTIONARY
print(inventory['apples'])

if inventory['apples'] == 140:
    print("There are 140 apples")

print("look here:")
if 15 in inventory:
    print(inventory[15])

print(" ")

#OUTPUT OF A LIST OF KEYS:
print(inventory.keys())
print(list(inventory.keys()))

key = list(inventory.keys())[0]
print(key)

#OUTPUT A LIST OF VALUES:
print(inventory.values())
print(list(inventory.values()))

#OUTPUT A LIST OF KEYS AND VALUES: PRODUCES A **LIST OF TUPLES**
print(inventory.items())

print(" ")
#UPDATING A VALUE FOR A KEY IN THE DICTIONARY
inventory['bananas'] = 100
print(inventory['bananas'])

print("^^^^^^^^^^^^^ ")
# IF A VALUE IS EQUIVALENT TO SOMETHING, PRINT KEY
for key, value in inventory.items():
    if value == 60:
        print(key)

print("^^^^^^^^^^^^^")
#DELETING SOMETHING IN THE DICTIONARY
del inventory['peaches']
print(inventory)

#MEMBERSHIP TESTS (BOOLEAN STATEMENTS)
print('apples' in inventory)
print('peaches' in inventory)
if 'apples' in inventory:
    print('There are apples available\n')


#NESTED DICTIONARIES:
#A THREE-KEY DICTIONARY, WITH A NESTED DICT FOR THE NAME TO SUPPORT MULPTIPLE PARTS, AND A NESTED FOR THE PIECE TO LIST
#MULTIPLE PIECES:
print("all about D")
D = {'Composer': {'first': 'Johannes', 'last' : 'Brahms'},
         'Period': 'Romantic',
         'Piece' : ['Piano Concerto No. 1', 'Piano Concerto No. 2',
            'Symphony No. 1', 'Symphony No. 2',
            'Violin Concerto in D Major',
            'Hungarian Dances'] }
print(D['Composer'])
print(D['Composer']['last'])
print(D['Piece'][-1])
D['Piece'].append('Variations on a Them by Paganini')
print(D)

#A NESTED DICTIOANARY, WITH THE GOAL OF RETRIEVING JUST A SINGLE LAST NAME:
d = {"employees":[{"firstName": "John", "lastName": "Doe"},
                {"firstName": "Anna", "lastName": "Smith"},
                {"firstName": "Peter", "lastName": "Jones"}],
"owners":[{"firstName": "Jack", "lastName": "Petter"},
          {"firstName": "Jessy", "lastName": "Petter"}]}
print(d["employees"][-2]["lastName"])

print(" ")

#ANOTHER DICTIONARY:
from pprint import pprint
movie = {
    "title": "Gattaca",
    "is_awesome": True,
    "won_oscar": False,
    "actors": ["Ethan Hawke", "Uma Therman", "Alan Arkin", "Loren Dean"],
    "budget": None,
    "credits": {
        "director": "Andrew Niccol",
        "writer": "Andrew Niccol",
        "composer": "Michael Nyman",
        "cenematographer": "Slawomir Idziak"
        }
         }
pprint (movie)

#---------- Dictionaries
# capitals = {'France': 'Paris',
#             'Italy': 'Rome',
#             'USA': 'WA DC'}
# print(capitals)
#
# #Add key and value:
# capitals['Spain'] = "Madrid"
# print(capitals)
#
# if 'Madrid' in capitals:
#     print(True)
# else: print(False) #False
#
# morecapitals = {'Germany': 'Berlin',
#                 'United Kingdom': 'London'}
# capitals.update(morecapitals)
# print(capitals)
#
# del capitals['USA']
# print(capitals)
#
# for key in capitals:
#     print()

print("%%%%%%%%%%%%%%")

cache = {0:0, 1:1, 2:1, 3:2, 4:3, 5:5, 6:8, 7:13}
def check_for_key(n):
    if n in cache:
        return cache[n]
print(check_for_key(7))
