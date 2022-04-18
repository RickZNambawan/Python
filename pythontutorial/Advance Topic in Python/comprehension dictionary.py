""" Dictionary Comprehension is the easy way to use a Dictionary and in good way """

""" usual way to create a key, value in dictionary with for loop """
# zip function to pair two set of list
# heroes = ["Spider-Man", "Iron-Man", "Hulk", "Captain America", "Black Widow"]
# names = ["Peter", "Tony", "Bruce", "Steve", "Natasha"]

# myDict = {}
# for hero, name in zip(heroes, names):
#     myDict[hero] = name
# print(myDict)

""" dictionary comprehension to create a key, value with for loop """
# by  the use of zip function
# heroes = ["Spider-Man", "Iron-Man", "Hulk", "Captain America", "Black Widow"]
# names = ["Peter", "Tony", "Bruce", "Steve", "Natasha"]
# myDict = {hero: name for hero, name in zip(heroes, names) if name != "Tony"}
# myDict = {(hero, name) for hero, name in zip(heroes, names)} # or maybe this syntax
# print(myDict)

""" generator expression """
# numbers = [1, 2, 3, 4, 5]
#
# def generatorFunc(numbers):
#     for number in numbers:
#         yield number * number
#
# generatorFunc(numbers)
#
# for i in generatorFunc(numbers):
#     print(i)

""" generator expression like comprehension"""
# numbers = [1, 2, 3, 4, 5]
# generatorFunc = (number * number for number in numbers)
#
# for i in generatorFunc:
#     print(i)
