class Arithmetic:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def addition(self):
        z = self.x + self.y
        return "Answer is: " + str(z)

    def subtraction(self):
        z = self.x - self.y
        return "Answer is: " + str(z)
    
    def multiplication(self):
        z = self.x * self.y
        return "Answer is: " + str(z)
    
    def division(self):
        z = self.x // self.y
        return "Answer is: " + str(z)

userOpt = int(input("""Select what arithmetic operation you want to use:
1.) Addition
2.) Subtraction
3.) Multiplication
4.) Division
Answer: """))

if userOpt > 4:
    print("Invalid input! Please try again.")
    exit()
else:
    userInp1 = int(input("Enter first number: "))
    userInp2 = int(input("Enter second number: "))

app = Arithmetic(userInp1, userInp2)

if userOpt == 1:
    print(app.addition())
elif userOpt == 2:
    print(app.subtraction())
elif userOpt == 3:
    print(app.multiplication())
elif userOpt == 4:
    print(app.division())
