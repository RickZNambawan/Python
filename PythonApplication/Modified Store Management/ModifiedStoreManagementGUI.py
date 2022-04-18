from tkinter import *
import tkinter.messagebox
import random
import time


class EventButton:
    def btnReset(self):
        self.candies.set(0)
        self.spaghetti.set(0)
        self.grahamBall.set(0)
        self.chowFan.set(0)
        self.biscuits.set(0)
        self.snacks.set(0)
        self.drinks.set(0)
        self.receiptNumber.set(0)
        self.costOfPurchases.set(0)
        self.stateTax.set(0)
        self.subTotal.set(0)
        self.totalCost.set(0)

    @staticmethod
    def btnExit():
        exitMessage = tkinter.messagebox.askquestion("Close Program", "Do you want to quit?")
        if exitMessage == "yes":
            quit()

    def btnTotal(self):
        self.referenceNumber = random.randint(1, 999999999)
        self.receiptNumber.set(self.referenceNumber)

        self.costOfCandies = self.candies.get()
        self.costOfSpaghetti = self.spaghetti.get()
        self.costOfGrahamBall = self.grahamBall.get()
        self.costOfChowFan = self.chowFan.get()
        self.costOfBiscuits = self.biscuits.get()
        self.costOfSnacks = self.snacks.get()
        self.costOfDrinks = self.drinks.get()

        self.priceOfCandies = self.costOfCandies * 1
        self.priceOfSpaghetti = self.costOfSpaghetti * 25
        self.priceOfGrahamBall = self.costOfGrahamBall * 6
        self.priceOfChowFan = self.costOfChowFan * 30
        self.priceOfBiscuits = self.costOfBiscuits * 8
        self.priceOfSnacks = self.costOfSnacks * 7
        self.priceOfDrinks = self.costOfDrinks * 10

        self.totalTax = (self.priceOfCandies + self.priceOfSpaghetti + self.priceOfGrahamBall + self.priceOfChowFan + self.priceOfBiscuits + self.priceOfSnacks + self.priceOfDrinks) * 0.2
        self.sumOfTheCost = (self.priceOfCandies + self.priceOfSpaghetti + self.priceOfGrahamBall + self.priceOfChowFan + self.priceOfBiscuits + self.priceOfSnacks + self.priceOfDrinks)

        self.totalPurchases = "P{:,.2f}".format(self.priceOfCandies + self.priceOfSpaghetti + self.priceOfGrahamBall + self.priceOfChowFan + self.priceOfBiscuits + self.priceOfSnacks + self.priceOfDrinks)
        self.paidTax = "P{:,.2f}".format(self.totalTax)
        self.overAllCost = "P{:,.2f}".format(self.totalTax + self.sumOfTheCost)

        self.costOfPurchases.set(self.totalPurchases)
        self.stateTax.set(self.paidTax)
        self.subTotal.set(self.totalPurchases)
        self.totalCost.set(self.overAllCost)

        # print receipt to console
        print("\nLyka's Sobrang Sari-Sari Store\n")
        print("Date & Time: {}".format(localTime))
        print("Receipt No.: #{}\n".format(self.referenceNumber))
        print("Candies: P1 x {} = P{:,.2f}".format(int(self.costOfCandies), self.priceOfCandies))
        print("Spaghetti: P25 x {} = P{:,.2f}".format(int(self.costOfSpaghetti), self.priceOfSpaghetti))
        print("Graham Ball: P6 x {} = P{:,.2f}".format(int(self.costOfGrahamBall), self.priceOfGrahamBall))
        print("Chow Fan: P30 x {} = P{:,.2f}".format(int(self.costOfChowFan), self.priceOfChowFan))
        print("Biscuits: P8 x {} = P{:,.2f}".format(int(self.costOfBiscuits), self.priceOfBiscuits))
        print("Snacks: P7 x {} = P{:,.2f}".format(int(self.costOfSnacks), self.priceOfSnacks))
        print("Drinks: P10 x {} = P{:,.2f}".format(int(self.costOfDrinks), self.priceOfDrinks))
        print("Tax: 2%")
        print("Subtotal: P{:.2f}".format(self.sumOfTheCost))
        print("Total Tax of Purchases: P{:,.2f}\n".format(self.totalTax))
        print("Total Cost: P{:,.2f}".format(self.totalTax + self.sumOfTheCost))


class Main(Frame, EventButton):
    def __init__(self, master):
        super().__init__(master, width=800, height=700, relief=SUNKEN)
        self.pack(side=LEFT)

        self.candies = IntVar()
        self.spaghetti = IntVar()
        self.grahamBall = IntVar()
        self.chowFan = IntVar()
        self.biscuits = IntVar()
        self.snacks = IntVar()
        self.drinks = IntVar()

        self.receiptNumber = IntVar()
        self.costOfPurchases = IntVar()
        self.stateTax = IntVar()
        self.subTotal = IntVar()
        self.totalCost = IntVar()

        self.widgets()
        self.buttons()

    def widgets(self):
        Label(self, font=("arial", 16, "bold"), text="Candies", bd=16, fg="black", anchor="w").grid(row=0, column=0)
        self.textBoxCandies = Entry(self, font=("arial", 16, "bold"), textvariable=self.candies, bd=10, insertwidth=4, bg="powder blue", justify="left")
        self.textBoxCandies.grid(row=0, column=1)

        Label(self, font=("arial", 16, "bold"), text="Spaghetti", fg="black", bd=16, anchor="w").grid(row=1, column=0)
        self.textBoxSpaghetti = Entry(self, font=("arial", 16, "bold"), textvariable=self.spaghetti, bd=10, insertwidth=4, bg="powder blue", justify="left")
        self.textBoxSpaghetti.grid(row=1, column=1)

        Label(self, font=("arial", 16, "bold"), text="Graham Ball", fg="black", bd=16, anchor="w").grid(row=2, column=0)
        self.textBoxGrahamBall = Entry(self, font=("arial", 16, "bold"), textvariable=self.grahamBall, bd=10, insertwidth=4, bg="powder blue", justify="left")
        self.textBoxGrahamBall.grid(row=2, column=1)

        Label(self, font=("arial", 16, "bold"), text="Chow Fan", fg="black", bd=16, anchor="w").grid(row=3, column=0)
        self.textBoxChowFan = Entry(self, font=("arial", 16, "bold"), textvariable=self.chowFan, bd=10, insertwidth=4, bg="powder blue", justify="left")
        self.textBoxChowFan.grid(row=3, column=1)

        Label(self, font=("arial", 16, "bold"), text="Biscuits", fg="black", bd=16, anchor="w").grid(row=4, column=0)
        self.textBoxBiscuit = Entry(self, font=("arial", 16, "bold"), textvariable=self.biscuits, bd=10, insertwidth=4, bg="powder blue", justify="left")
        self.textBoxBiscuit.grid(row=4, column=1)

        Label(self, font=("arial", 16, "bold"), text="Snacks", fg="black", bd=16, anchor="w").grid(row=5, column=0)
        self.textBoxSnacks = Entry(self, font=("arial", 16, "bold"), textvariable=self.snacks, bd=10, insertwidth=4, bg="powder blue", justify="left")
        self.textBoxSnacks.grid(row=5, column=1)

        Label(self, font=("arial", 16, "bold"), text="Drinks", fg="black", bd=16, anchor="w").grid(row=0, column=2)
        self.textBoxDrinks = Entry(self, font=("arial", 16, "bold"), textvariable=self.drinks, bd=10, insertwidth=4, bg="powder blue", justify="left")
        self.textBoxDrinks.grid(row=0, column=3)

        Label(self, font=("arial", 16, "bold"), text="Receipt #", fg="black", bd=16, anchor="w").grid(row=1, column=2)
        self.textBoxOfReceiptNumber = Entry(self, font=("arial", 16, "bold"), textvariable=self.receiptNumber, bd=10, insertwidth=4, justify="left")
        self.textBoxOfReceiptNumber.grid(row=1, column=3)

        Label(self, font=("arial", 16, "bold"), text="Cost of Purchases", fg="black", bd=16, anchor="w").grid(row=2, column=2)
        self.textBoxCostOfPurchases = Entry(self, font=("arial", 16, "bold"), textvariable=self.costOfPurchases, bd=10, insertwidth=4, justify="left")
        self.textBoxCostOfPurchases.grid(row=2, column=3)

        Label(self, font=("arial", 16, "bold"), text="State Tax", fg="black", bd=16, anchor="w").grid(row=3, column=2)
        self.textBoxStateTax = Entry(self, font=("arial", 16, "bold"), textvariable=self.stateTax, bd=10, insertwidth=4, justify="left")
        self.textBoxStateTax.grid(row=3, column=3)

        Label(self, font=("arial", 16, "bold"), text="Sub Total", fg="black", bd=16, anchor="w").grid(row=4, column=2)
        self.textBoxSubTotal = Entry(self, font=("arial", 16, "bold"), textvariable=self.subTotal, bd=10, insertwidth=4, justify="left")
        self.textBoxSubTotal.grid(row=4, column=3)

        Label(self, font=("arial", 16, "bold"), text="Total Cost", fg="black", bd=16, anchor="w").grid(row=5, column=2)
        self.textBoxTotalCost = Entry(self, font=("arial", 16, "bold"), textvariable=self.totalCost, bd=10, insertwidth=4, justify="left", fg="red")
        self.textBoxTotalCost.grid(row=5, column=3)

    def buttons(self):
        self.buttonTotal = Button(self, padx=16, pady=8, bd=16, fg="black", font=("arial", 16, "bold"), width=10, text="Total", bg="powder blue", command=self.btnTotal)
        self.buttonTotal.grid(row=7, column=1)
        self.buttonReset = Button(self, padx=16, pady=8, bd=16, fg="black", font=("arial", 16, "bold"), width=10, text="Reset", bg="powder blue", command=self.btnReset).grid(row=7, column=2)
        self.buttonExit = Button(self, padx=16, pady=8, bd=16, fg="black", font=("arial", 16, "bold"), width=10, text="Exit", bg="powder blue", command=self.btnExit).grid(row=7, column=3)


class TopFrame(Frame):
    def __init__(self, master):
        super().__init__(master, width=1600, height=150, bg="black", bd=10, relief="raised")
        self.pack(side=TOP)
        self.timeSet = IntVar()
        self.widgets()

    def widgets(self):
        self.timeSet.set(localTime)

        self.programTitle = Label(self, font=("times new roman", 50, "bold"), text="LYKA'S SOBRANG SARI-SARI STORE", fg="hot pink", bg="black", bd=10, anchor="w")
        self.programTitle.grid(row=0, column=0)

        self.programTime = Entry(self, font=("arial", 16, "bold"), textvariable=self.timeSet, fg="white", bg="black", bd=10, width=30, justify="center")
        self.programTime.grid(row=1, column=0)

# creating GUI
root = Tk()
root.title("Lyka's Store System")
root.geometry("1650x950+120+25")

# global variable
localTime = time.asctime()

# main application
topFrame = TopFrame(root)
mainFrame = Main(root)
root.mainloop()
