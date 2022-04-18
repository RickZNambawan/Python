""" Namedtuple is easier way to create a tuple to make code more readable and less code
    It is more likely a tuple with a dictionary but more easy than dictionary
"""
from collections import namedtuple  # import this

""" regular tuple and dictionary """
tupleColor = (254, 223, 2323, 234)
dictTupleColor = {"blue": 244, "red": 424, "green": 232}
print(tupleColor[2])
print(dictTupleColor["green"])


""" create color tuple using namedtuple to be more readable and easy to use """
Color = namedtuple("Color", ["red", "green", "blue"])
white = Color(253, 324, 5235)
black = Color(255, 255, 255)

print(white)
print(white.red)
print(white[0])
print("")

print(black)
print(black.green)
print(black[1])
print("")

""" create employee tuple with the use of namedtuple """
Employee = namedtuple("Employee", ["name", "age", "pay"])
firstEmployee = Employee("Frederick", 19, 20000)
secondEmployee = Employee("Lyka", 18, 50000)

print(firstEmployee)
print(firstEmployee.name)
print("")

print(secondEmployee)
print(secondEmployee.pay)
print("")

""" with use of for loops """
myList = [employee for employee in firstEmployee]
for items in myList:
    print(items)

myDict = {}
for employeeOne, employeeTwo in zip(firstEmployee, secondEmployee):
    myDict[firstEmployee] = secondEmployee

def eSort(emp):
    return emp.name

haha = sorted(myDict, key=eSort)
print(haha)