""" Decorator - function that are use to extend the behavior of a certain method from
    the class without modifying it
    @staticmethod - used as a regular function
    @classmethod - used as an alternative constructor
"""

class Employee:
    raiseSalary = 1.05

    def __init__(self, name, age, pay):
        self.name = name
        self.age = age
        self.pay = pay

    def __str__(self):
        return self.name

    def raiseAmountOfSalary(self):
        self.pay *= self.raiseSalary

    @staticmethod  # used as a regular function without using the instance of a class but has a connection to a class
    def exit():  # use it when you'll not use the self as argument.
        quit()

    @classmethod  # used as an alternative constructor
    def payRaise(cls, amount):
        cls.raiseSalary = amount  # changed the amount of global variable raiseSalary


emp1 = Employee("Frederick", 19, 10000)
emp2 = Employee("Lyka", 18, 20000)

emp1.payRaise(1.2)  # @classmethod with a use of alternative constructor below the code
print(emp1.pay)
emp1.raiseAmountOfSalary()  # it works when this method is called
print(f"{emp1.pay:,.0f}")

# it will not work when an instance method is not called.
emp2.payRaise(1.5)
print(emp2.pay)
print(f"{emp2.pay:,.0f}")
