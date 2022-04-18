""" *args = Arguments (lists)
    **kwargs = KeyWord Arguments (dictionary)
"""


def showArgs(title, *args):
    print(title)
    for index, items in enumerate(args, 1):
        print(index, items)


def showKwargs(title, **kwargs):
    print(title)
    for key, value in kwargs.items():
        print(key, value)


# List
titleList = "\nList in *args:"
subjectsList = ["Math", "English", "Science", "Araling Panlipunan"]
showArgs(titleList, *subjectsList)

# Tuples
titleTuple = "\nTuple in *args:"
employeesTuple = ("Frederick", "Florante", "Lyka", "Clarence")
showArgs(titleTuple, *employeesTuple)

# Dictionary
titleDictionary = "\nDictionary in **kwargs:"
numbersDictionary = {"Uno": "One", "Dos": "Two", "Tres": "Three", "Kwatro": "Four"}
showKwargs(titleDictionary, **numbersDictionary)

