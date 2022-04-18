""" Magic Method or Dunder
    Magic Method = Special Method of a Class
    Dunder = Double Underscore
    It is use when you call the name of the class only by itself without methods or attributes
"""


class ProgrammingClass:
    # constructor
    def __init__(self, name, grade):  # the codes inside it called once you create an instance of a class
        self.studentName = name
        self.studentGrade = grade
        self.call_a_constructor()

    def __str__(self):  # for the user-friendly or read only by user
        return self.studentName

    def __repr__(self):  # for the developer who will read the code
        return self.studentName

    def __len__(self):  # return length of the name
        return len(self.studentName)

    def __add__(self, other):
        return self.studentGrade + other.studentGrade

    @staticmethod
    def call_a_constructor():
        print("Constructor")


frederick = ProgrammingClass("Frederick", 95)
florante = ProgrammingClass("Florante", 94)

print(frederick)  # returning string name
print(repr(frederick))  # returning string name
print(len(florante))  # returning the length of the name
print(frederick + florante)  # returning the sum of their grade
