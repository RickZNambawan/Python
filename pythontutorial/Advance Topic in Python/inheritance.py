""" Inheritance are use to get the capability of one class to another class
    Inherit the Parent Class into Child Class
    Super Class = Parent Class
    Sub Classes = Child Classes
"""


class Company:
    def __init__(self, full_name, age, position, pay):
        self.full_name = full_name
        self.age = age
        self.position = position
        self.pay = pay
        self.salary_raise = 1.2

    def __str__(self):
        return self.full_name

    def salary_increase(self):
        self.pay = int(self.pay * self.salary_raise)
        print("Your salary increase {}% to: {:,}".format(self.salary_raise, self.pay))


class Developer(Company):
    def __init__(self, full_name, age, position, pay, programming_language):
        Company.__init__(self, full_name, age, position, pay)
        self.min_salary_increase = 1.5
        self.programming_language = programming_language


class Manager(Company):
    def __init__(self, full_name, age, position, pay):
        Company.__init__(self, full_name, age, position, pay)
        self.salary_raise = 1.7
        self.employee_list = []
        self.welcome_employee(self.full_name, self.position, self.pay)

    @staticmethod
    def welcome_employee(full_name, position, pay):
        print("Welcome {} to my company!".format(full_name))
        print("Your position on my company is: {}".format(position))
        print("YOur current salary is: {:,}\n".format(pay))

    def add_employee(self, employee):
        if employee.full_name not in self.employee_list:
            print("{} is successfully added as your employee!".format(employee))
            self.welcome_employee(employee.full_name, employee.position, employee.pay)
            self.employee_list.append(employee.full_name)
        else:
            print("{} is already your employee.".format(employee.full_name))

    def remove_employee(self, employee):
        if employee.full_name in self.employee_list:
            print("{} is removed as your employee.".format(employee.full_name))
            self.employee_list.remove(employee.full_name)

    def show_employee_list(self):
        print("\nList of Employee")
        for index, employee in enumerate(self.employee_list, 1):
            print("{}.) {}".format(index, employee))


game_dev = Developer("Frederick", 19, "Game Developer", 30000, "Java")
web_dev = Developer("Florante", 18, "Web Developer", 20000, "JavaScript")
mobile_dev = Developer("Clarence", 19, "Mobile Developer", 25000, "C#")
software_dev = Developer("Ledesma", 18, "Software Developer", 27000, "Python")
manager = Manager("Lyka", 18, "Manager", 50000)

manager.add_employee(game_dev)
manager.add_employee(web_dev)

manager.remove_employee(game_dev)

manager.show_employee_list()

print("\n{}, Your salary is: {:,}".format(manager, manager.pay))
manager.salary_increase()

print("\n{}, Your salary is: {:,}".format(game_dev, game_dev.pay))
game_dev.salary_increase()
