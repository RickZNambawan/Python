""" Set Comprehension is the easy way to use a Set and in good way """

""" set() is like a list except it has a unique values """
# usual way to create a set
# numbers = [1, 2, 3, 1, 2, 10, 2, 3, 4, 5, 5, 6, 1, 10]
# mySet = set()
#
# for number in numbers:
#     mySet.add(number)  # instead of append() use add()
# print(mySet)

""" set comprehension """
# numbers = [1, 2, 3, 1, 2, 10, 2, 3, 4, 5, 5, 6, 1, 10]
# mySet = {number for number in numbers}  # instead of braces uses curly braces
# print(mySet)
