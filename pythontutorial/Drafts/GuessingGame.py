import random

print("Welcome to the Guessing Game!!")


class Application:
    def __init__(self, menu):
        self.menu = menu
        self.magicNumber = 0
        self.userInp = ""
        self.tries = 1
        self.lives = 5
        self.magicNumberGenerator()
        self.randomGenerator()

    def magicNumberGenerator(self):
        if self.menu <= 0 or self.menu > 3:
            print("Invalid Input! Please try again.")
            exit()
        else:
            if self.menu == 1:
                self.magicNumber = random.randint(1, 100)
            elif self.menu == 2:
                self.magicNumber += random.randint(1, 50)
            elif self.menu == 3:
                self.magicNumber += random.randint(1, 20)

    def randomGenerator(self):
        while True:
            self.userInp = int(input("\nEnter your guess: "))
            if self.userInp > self.magicNumber:
                print("Lower!")
            elif self.userInp < self.magicNumber:
                print("Higher!")
            else:
                print("\nYou guessed it right! The magic number was {}.".format(self.magicNumber))
                print("And it only took you {} tries!\n".format(self.tries))
                break

            self.lives -= 1
            self.tries += 1
            if self.lives <= 0:
                print("\nSorry you don't have tries!")
                print("The magic number was {}".format(self.magicNumber))
                break
            print("Only", self.lives, "lives left")











