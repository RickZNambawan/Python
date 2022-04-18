""" Ways to sort a list of items using many ways """

""" sorted function and sort method """
# items = [0, 10, 7, 5, 6, 3, 4, 9, 8, 1, 2]
# itemsSort = sorted(items)  # function
# print(itemsSort)

# items.sort()  # method
# print(items)

# but can't assign to a variable
# itemsSorted = items.sort()
# print(itemsSorted)  # it will return None

""" sorted function and sort method with parameter"""
# items = [0, 10, 7, 5, 6, 3, 4, 9, 8, 1, 2]
# itemsSort = sorted(items, reverse=True)  # function: print in descending order
# print(itemsSort)
#
# items.sort(reverse=True)  # method: print in descending order
# print(items)

""" SORTED IS A MUST USE. IT GIVES MORE FLEXIBILITY WHEN PASSING A LIST OF ITEMS ON PARAMETER """

""" Sorted Function with Tuple """
# tup = (0, 10, 7, 5, 6, 3, 4, 9, 8, 1, 2)
# tupSort = sorted(tup, reverse=True)  # descending order values
# print(tupSort)

""" Sorted Function with Dictionary """
# myDict = {"Spider Man": "Peter", "Iron Man": "Tony", "Captain America": "Steve"}
# myDictSort = sorted(myDict)  # it will sort only the keys
# print(myDictSort)

""" Sorted Function with key parameter """
# absNumber = [-6, -5, -4, 1, 2, 3]
# absNumberSort = sorted(absNumber, key=abs)  # it sorted it with the absolute value
# print(absNumberSort)

""" Sorted Function with Class Object and key parameter """
# class Employee:
#     def __init__(self, name, age, pay):
#         self.name = name
#         self.age = age
#         self.pay = pay
#
#     def __repr__(self):
#         return "{}: {}: {}".format(self.name, self.age, self.pay)

# from operator import attrgetter

# emp1 = Employee("Frederick", 19, 20000)
# emp2 = Employee("Lyka", 18, 50000)
# emp3 = Employee("Florante", 19, 25000)

# with the use of function as a key parameter value
# def empSorted(emp):
#     return emp.pay
#
# employees = [emp1, emp2, emp3]
# empSort = sorted(employees, key=empSorted)
# print(empSort)

# with the use of lambda
# employees = [emp1, emp2, emp3]
# empSort = sorted(employees, key=lambda emp: emp.age)
# print(empSort)

# with the use of attrgetter
# employees = [emp1, emp2, emp3]
# empSort = sorted(employees, key=attrgetter("pay"), reverse=True)
# print(empSort)

