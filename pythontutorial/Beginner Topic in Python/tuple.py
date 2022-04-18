""" Tuples - are likely list but the values cannot be change
    Mutable - Can be change
    Immutable - Cannot be change
"""

""" Declaration """
myTuple = ("Frederick", "Lyka", "Florante", "Clarence")  # declare tuple with parenthesis
print(myTuple)

newTuple = ("Facebook",)  # declare tuple with only one value needs a comma after the first value
print(newTuple)

""" Mutable """
# list of strings
firstList = ["IT", "HRM", "Engineer", "Accoutancy"]
firstList[3] = "Dentistry"  # can modify/change the value
print(firstList)

# list of numbers
secondList = [1, 2, 6, 4, 5]
secondList[2] = 3
print(secondList)

""" Immutable """
programmingLang = ("Python", "Java", "Swift", "JavaScript")
print(programmingLang)
# programmingLang[2] = "PHP"  # error: cannot modify

""" Methods of Tuple """
# count() method
names = ("Fred", "Fred", "Lyka", "Florante")
print(names.count("Fred"))  # return how many the inserted value

# index() method
surnames = ("castaneda", "agad", "ralotin", "roque")
print(surnames.index("agad"))  # return the index position of the value

""" Adding Values """
courses = ("Math",)
courses += "Science",
print(courses)
