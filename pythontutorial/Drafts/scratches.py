""" If the most common letter in English Language is in the message """
# response = input("Enter a message: ")
# print("The length of your message is: {}".format(len(response)))
# print("The most common letter in the English Language is 'e'.")
#
# if "e" in response:
#     print("Yes it is!")
# else:
#     print("Nah its not!")


""" Removing vowels in message """
# message = input("Enter a message: ")
# newMessage = ""
# vowels = "aeiou"
#
# for letter in message:
#     if letter not in vowels:
#         newMessage += letter
# print("Your message without vowels is:", newMessage)


""" Return all the vowels in the message """
# message = input("Enter a message: ")
# newMessage = ""
# vowels = "aeiou"
#
# for letter in message:
#     if letter.lower() in vowels:
#         newMessage += letter
# print("The vowels on your message are:", newMessage)


""" Slicing the word """
# word = input("Enter a word: ")
# start = int(input("Start: "))
# finish = int(input("Finish: "))
# print("word[{}:{}] is {} \n".format(start, finish, word[start:finish]))


""" Adding values to a Tuple """
# inventory = ("sword", "armor", "shield", "healing potion")
# addItems = ""
#
# while addItems != "Done":
#     addItems = input("Add items: ")
#     inventory += addItems,
#     print(inventory)
#
# print("\nYour items:")
# for items in inventory:
#     print(items)


""" Guessing the Jumbled Word """
# import random
#
# words = ("frederick", "difficult", "easy", "medium", "gago", "pota", "lakoisip")
# chosenWord = random.choice(words)
# myList = []
#
# for letter in chosenWord:
#     myList.append(letter)
# jumbledLetters = sorted(myList, reverse=True)
#
# jumbledWord = ""
# for letter in jumbledLetters:
#     jumbledWord += letter
#
# print("The jumbled word is: {}\n".format(jumbledWord))
#
# while True:
#     guess = input("Your guess: ")
#     if guess == chosenWord:
#         print("You've got the correct word!")
#         break
#     print("No! Please try again!\n")
#


""" Used of help() function """
# import math
# import random
#
# myList = [1, 2, 3]
# mySum = math.fsum(myList)
# print(sum(myList))
# print(mySum)
# print(help(random))
# print(random.__file__)


""" Using sqlite3 """
# import sqlite3
#
# conn = sqlite3.connect("sampleDatabase.db")
# c = conn.cursor()
#
# c.execute("DROP TABLE IF EXISTS ITCA")
# c.execute("CREATE TABLE ITCA (name TEXT, age INTEGER )")
#
# name = "Fred"
# age = "19"
#
# def enterStudent():
#     while True:
#         name = input("Enter name: ")
#         if name == "done":
#             break
#         else:
#             age = int(input("Enter age: "))
#             print("")
#             c.execute("INSERT INTO ITCA (name, age ) VALUES (?, ?)", (name, age))
#             conn.commit()
#
# def retrieveDB():
#     a = c.execute("SELECT name, age FROM ITCA")
#     myDict = {name: age for name, age in a}
#
#     for name, age in myDict.items():
#         print("{}: {}".format(name, age))
#
#
# enterStudent()
# retrieveDB()


""" Return the vowels and consonants of the word """
# word = input("Enter a word: ")
# upperVowels = "AEIOU".upper()
# lowerVowels = "aeiou".lower()
# for letter in word:
#     newWord = ""
#     if letter not in upperVowels and letter not in lowerVowels:
#         newWord = newWord + letter
#         print(newWord, end="")
# print()
# for letter in word:
#     newWord = ""
#     if letter in upperVowels or letter in lowerVowels:
#         newWord = newWord + letter
#         print(newWord, end="")


""" Finding largest number on the list"""
# largest = 0
# for smallest in [63, 12, 50, 23, 66, 1, 64, 77, 44, 89]:
#     if smallest > largest:
#         largest = smallest
#     print(f"Smallest Number: {smallest}\t\t\t Largest Number: {largest}")


""" Printing Pyramid """
# number = int(input("Enter a number: "))
# for i in range(1, number + 1):
#     for k in range(1, i + 1):
#         print("*", end="")
#     print()


""" Fibonacci Sequence """
# f1 = int(input("Input first number: "))
# f2 = int(input("Input second number: "))
# fibonacci = []
# iterate = iter(fibonacci)
# counter = 0
#
# fibonacci.append(f1)
# fibonacci.append(f2)
#
# while counter < 8:
#     number1 = next(iterate)
#     number2 = fibonacci[counter + 1]
#     print(number1)
#     print(number2)
#     fnext = number1 + number2
#     print(fnext)
#     fibonacci.append(fnext)
#     counter += 1
# print(fibonacci)


""" Sum all of the Prime Number base on the user input """
# number = int(input("Enter a number: "))  # 10
# counter = 2
# anotherCounter = 2
# sumOfAllPrime = 8
# while counter < number:
#     if counter == anotherCounter:
#         sumOfAllPrime += counter
#         counter += 1
#         anotherCounter = 2
#     elif (counter % anotherCounter) == 0:
#         counter += 1
#     elif (counter % 3) == 0 or (counter % 5) == 0:
#         counter += 1
#     else:
#         anotherCounter += 1
# print(sumOfAllPrime)


""" Another way of summing all the prime numbers base on the user input """
# number = int(input("Enter a number: "))
# sumOfAllPrime = 0
# for counter in range(2, number):
#     for anotherCounter in range(2, number):
#         if counter == anotherCounter:
#             sumOfAllPrime += counter
#             break
#         elif counter % anotherCounter == 0:
#             break
# print("The sum of all prime numbers is: {:,}".format(sumOfAllPrime))


""" Determining the Palindrome Number """
# number = int(input("Enter a number: "))
# anotherNumber = number
# reverseResult = ""
# while anotherNumber != 0:
#     counter = anotherNumber % 10
#     anotherNumber //= 10
#     reverseResult += str(counter)
#``
# if int(reverseResult) == number:
#     print("Palindrome Number.")
# else:
#     print("Not Palindrome Number.")

# number = int(input("Enter a NUmber: "))
# counter = number
# anotherNumber = ""
# while counter != 0:
#     anotherCounter = counter % 10
#     counter = counter // 10
#     anotherNumber = anotherNumber + str(anotherCounter)
#
# if number == int(anotherNumber):
#     print("{} is a Palindrome Number.".format(number))
# else:
#     print("{} is not a Palindrome Number.".format(number))

# number = int(input("Enter a NUmber: "))
# Counter = number
# anotherNumber = ""
# anotherCounter = ""
# while anotherNumber != 0:
#     counter = anotherNumber % 10
#     anotherNumber = anotherNumber // 10
#     anotherCounter = str(counter)
# if number == int(anotherNumber):
#    print("{} is a Palindrome Number.".format(anotherCounter))
# else:
#     print("{} is not a Palindrome Number.".format(anotherCounter))


# number = int(input("Enter a Number: "))
# total = ""
# while number != 0:
#     counter = number % 10
#     number = number // 10
#     total = total + str(counter)
#     print(total)
# print("last total: {}".format(total))

from tkinter import *
import tkinter.messagebox

def main():
    root = Tk()
    app = SalesLogin(root)
    root.mainloop()

class SalesLogin:
    def __init__(self, root):
        self.root = root
        self.root.title("Sales Management")
        self.root.geometry("1350x750+300+100")
        self.frame = Frame(self.root, bg="cadet blue")
        self.frame.pack()
        self.name = StringVar()
        self.password = StringVar()
        self.createWidgets()

    def createWidgets(self):
        Label(self.frame, text="Sales Management Login System", font=("arial", 60, "bold"),
              bg="cadet blue", fg="Cornsilk").grid(row=0, column=0, columnspan=2, pady=20)

        self.loginFrame1 = LabelFrame(self.frame, text="Login", width=300, height=200, font=("arial", 20, "bold"),
                                    relief="ridge", bg="cadet blue", bd=40)
        self.loginFrame1.grid(row=1, column=0)
        
        Label(self.loginFrame1, text="Username: ", font=("arial", 30, "bold"), bd=22, bg="cadet blue", fg="Cornsilk").grid(row=0, column=0)
        self.nameEntry = Entry(self.loginFrame1, width=33, font=("arial", 30, "bold"), bd=7, textvariable=self.name)
        self.nameEntry.grid(row=0, column=1, padx=88)
        
        Label(self.loginFrame1, text="Password: ", font=("arial", 30, "bold"), bd=22, bg="cadet blue", fg="Cornsilk").grid(row=0, column=0)  
        self.passwordEntry = Entry(self.loginFrame1, textvariable=self.password, width=33, show="*", font=("arial", 30, "bold"), bd=7)
        self.passwordEntry.grid(row=1, column=1, columnspan=2, pady=30)

        self.loginButton = Button(self.loginFrame1, text="Login", width=15,
                                  font=("arial", 30, "bold"), bg="cadet blue", fg="Cornsilk", command=self.LoginSystem)
        self.loginButton.grid(row=2, column=1)
        
    def LoginSystem(self):
        user = self.name.get()
        pas = self.password.get()

        if user == "" and pas == "":
            self.window = Toplevel(self.root)
            SalesManagement(self.window)
        else:
            tkinter.messagebox.askyesno("Sales Management Login System", "Invalid Input")
            self.name.set("")
            self.name.set("")

##    def LoginWindow(self):
##        self.window = Toplevel(self.root)
##        self.app = SalesManagement(self.window)

class SalesManagement:
    def __init__(self, root):
        self.root = root
        self.root.title("Sales Management")
        self.root.geometry("1350x750+300+100")

if __name__ == '__main__':
    main()
