class FredCompany:

    payRaise = 3
    
    def __init__(self, firstName, secondName, pay):
        self.firstName = firstName
        self.secondName = secondName
        self.pay = pay

    def name(self):
        return self.firstName
    
    def fullName(self):
        fullName = self.firstName + " " + self.secondName
        return(fullName)

    def raisePay(self):
        raiseMoney = self.pay * self.payRaise
        return(raiseMoney)

name = str(input("Enter your name: "))

employee1 = FredCompany("Fred", "Castaneda", 500)
employee2 = FredCompany("Lyka", "Agad", 1000)
employee3 = FredCompany(name, "hha", 10)

print(employee3.name())
print(employee1.fullName())
print(employee1.pay)
print(employee1.raisePay())
print("\n")
print(employee2.fullName())
print(employee2.pay)
print(employee2.raisePay())

FredCompany.raisePay(employee1)
