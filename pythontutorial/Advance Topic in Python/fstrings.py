""" Fstring (Formatted String) - is a new way to format strings in Python 3.6 and above without format method """

""" String formatting with format method """
# firstName = "Frederick"
# lastName = "Castañeda"
# print("My name is {} {}".format(firstName, lastName))

""" Fstring """
# firstName = "Frederick"
# lastName = "Castañeda"
# print(f"My name is {firstName} {lastName}")

""" Fstring with functions, methods and direct computation"""
# firstName = "Frederick"
# lastName = "Castañeda"
# print(f"My name is {firstName.upper()} {lastName.upper()} {3**3}")

""" Fstring with dictionary """
# myDict = {"name": "Frederick", "age": 19}
# print(f"My name is {myDict['name']} I am {myDict['age']}")

""" Fstring with colon placeholder """
# for i in range(1, 10):  # with decimal value
#     print(f"{i:.2f}")

# for i in range(1, 10000):  # with comma separator
#     print(f"{i:,}")

# for i in range(1, 100000):  # with many formatting
#     print(f"{i:,.2f}")
