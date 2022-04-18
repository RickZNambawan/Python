""" List Comprehension is the easy way to use a List and in good way """

""" the usually way for using a list in for loop"""
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# myList = []
#
# for number in numbers:
#     myList.append(number)
# print(myList)

""" list comprehension: easy way to use list """
# printing what's inside the list
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# myList = [number for number in numbers]
# print(myList)

# printing what the square for every items in the list
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# myList = [2**number for number in numbers]
# print(myList)

""" usual way to print even in the list """
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# myList = []
# for number in numbers:
#     if (number % 2) == 0:
#         myList.append(number)
# print(myList)

""" list comprehension for printing even"""
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# myList = [number for number in numbers if (number % 2) == 0]
# print(myList)

""" usual way to print pair of items in nested for loop """
# myList = []
# for letter in "abcd":
#     for number in range(4):
#         myList.append((letter, number))
# print(myList)

""" list comprehension for printing pair of items in nested for loop """
# myList = [(letter, number) for letter in "abcd" for number in range(4)]
# print(myList)

