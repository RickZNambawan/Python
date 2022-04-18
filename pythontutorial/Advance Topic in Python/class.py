""" Class - are use to group certain codes into a container
    Methods = functions inside a class
    Attributes = variables inside  a class
    Objects = All of the Methods and Attributes of a class. It starts with dot notation
"""

class Employee:
    def __init__(self, name, position, salary, salaryIncrease):
        self.name = name
        self.position = position
        self.salary = salary
        self.salaryIncrease = salaryIncrease
        self.welcomingEmployee()

    def welcomingEmployee(self):
        print("\nHi {}! Welcome to my Company.".format(self.name))
        print("Your current position in my Company is {}".format(self.position))
        print("Your current salary for now will be: {:,}".format(self.salary))

    def raiseSalary(self):
        self.salary = int(self.salary * self.salaryIncrease)
        print("Your salary increases. It is now {:,}".format(self.salary))

firstEmp = Employee("Frederick", "Web Developer", 25000, 1.1)
firstEmp.raiseSalary()

secondEmp = Employee("Florante", "Game Developer", 30000, 1.5)
secondEmp.raiseSalary()

thirdEmp = Employee("Lyka", "Manager", 50000, 2)
thirdEmp.raiseSalary()

fourthEmp = Employee("Clarence", "Janitor", 5000, 1.2)
fourthEmp.raiseSalary()

