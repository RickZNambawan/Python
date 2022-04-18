""" Decorator - function that are use to extend the behavior of a certain method from
    the class without modifying it
    @property decorator with setter and deleter
"""


class Car:
    def __init__(self, firstName, lastName, brand):
        self.firstNameOfCar = firstName
        self.lastNameOfCar = lastName
        self.brandOfCar = brand

    # first example
    @property  # can use a method below it as an class attribute
    def displayName(self):
        return "{} {}".format(self.firstNameOfCar, self.lastNameOfCar)

    @displayName.setter  # property decorator implements .setter for you to set new value to the property attribute
    def displayName(self, fullName):
        firstName, lastName = fullName.split(" ")
        self.firstNameOfCar = firstName
        self.lastNameOfCar = lastName

    @displayName.deleter  # used to change or delete the past attribute value
    def displayName(self):
        print("Deleted Name")
        self.firstNameOfCar = None
        self.lastNameOfCar = None

    # second example
    @property
    def displayBrand(self):
        return self.brandOfCar

    @displayBrand.setter
    def displayBrand(self, newBrand):
        self.brandOfCar = newBrand

    @displayBrand.deleter  # used just to change the value
    def displayBrand(self):
        self.brandOfCar = "No brand yet"

# first example
carOne = Car("Ferrari", "Ford", "Racing Car")
print(carOne.displayName)  # past value

carOne.displayName = "Frederick Castaneda"
print(carOne.displayName)  # new value after assigning setter

del carOne.displayName  # del keyword used to delete the past value
carOne.displayName = "Lyka Agad"
print(carOne.displayName)

# second example
carTwo = Car("BMW", "GT", "Super Car")
print(carTwo.displayBrand)  # past value

carTwo.brandOfCar = "BearBrand"
print(carTwo.displayBrand)  # new value

del carTwo.displayBrand  # it changes the value but not deleting it.
print(carTwo.displayBrand)

# change instance attribute
print(carOne.firstNameOfCar)
carOne.firstNameOfCar = "haha"
print(carOne.firstNameOfCar)