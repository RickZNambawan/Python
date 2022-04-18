""" String Formatting - allow us to display our information in exactly the way we want.
    String Concatenation - adding some string and variable with a "+" sign
"""

""" string concatenation """
# myDict = {"name": "Fred", "age": 19}
# print("My name is: " + myDict["name"] + " and I am " + str(myDict["age"]))  # not a good way to print string

""" sting formatting with format method """
# myDict = {"name": "Fred", "age": 19}
# print("My name is: {} and I am {}".format(myDict["name"], myDict["age"]))  # more readable than concatenation

""" sting formatting with format method with number on the placeholder """
# myDict = {"name": "Fred", "age": 19}
# print("I am {1} and My name is: {0}".format(myDict["name"], myDict["age"]))

""" string formatting with the use of dictionary """
# person = {"name": "Fred", "age": 19}
# print("I am {0[age]} and My name is: {0[name]}".format(myDict))

""" string formatting with the use of list and dictionary """
# myList = ["Fred", 19]
# myDict = {"Uno": 1, "Dos": 2}
# print("My name is: {0[0]} and I am {0[1]}. This is {1[Uno]} and this is {1[Dos]}".format(myList, myDict))

""" string formatting with the class attributes """
# class Employee:
#     def __init__(self, name, age, salary):
#         self.name = name
#         self.age = age
#         self.salary = salary

# firstEmp = Employee("Frederick", 19, 20000)
# print("My name is: {0.name} and I am {0.age}".format(firstEmp))

""" string formatting with keyword arguments """
# print("My name is {name} and I am {age}".format(name="Fred", age=19))

""" string formatting to unpack a dictionary """
# myDict = {"name": "Frederick", "age": 19}
# print("My name is {name} and I am {age}".format(**myDict))  # ** is use to unpack dictionary (**kwargs)

""" string formatting to unpack a list """
# myList = ["Fred", 19]
# print("My name is {0} and I am {1}".format(*myList))  # * is use to unpack lists (*args)

""" string formatting with local variables """
# var1 = "fred"
# var2 = 19
# print("My name is {var1} and I am {var2}".format(**locals()))

""" string formatting with global variables """
# var3 = "fred"
# var4 = 19
# def exampleFunc():
#     print("My name is {var3} and I am {var4}".format(**globals()))

""" string formatting with colon in placeholder to add 0 padding """
# for i in range(1, 10):
#     print("{:.2f}".format(i))

""" string formatting with colon placeholder to add decimal value """
# pi = 3.14159265
# print("{:.4f}".format(pi))

""" string formatting with colon placeholder to add comma separator """
# print("My money is {:,}".format(5**6))

""" string formatting with colon placeholder to add many formatting """
# print("My money is {:,.2f}".format(1000**2))
