from tkinter import*
import random
import time
import tkinter.messagebox

#===========================================Calculator GUI Function=====================================================

def btnClick(numbers):
    global operator
    operator += str(numbers)
    textInput.set(operator)

def btnClear():
    global operator
    operator = ""
    textInput.set("")

def btnEquals():
    global operator
    total = str(eval(operator))
    textInput.set(total)
    operator = ""

#window
root = Tk()
root.config(background="black")
root.geometry("1650x950+0+0")
root.title("Lyka's Store System")

#=====================================MENU BAR===============================================

# menu = Menu(root) # Creates a main menu to main window
# root.config(menu=menu) # to configure tkinter that you creates a menu
#
# # ***** Creating a Main Menu ********
#
# subMenu = Menu(menu, tearoff=0) # creates a sub menu into a main menu # tearoff=0 - to remove the "----" at the submenu
#
# # add a drop down menu to the menus
# menu.add_cascade(label="File", menu=subMenu) # creates a menu without commands
# subMenu.add_command(label="New") # creates a menu with a commands
# subMenu.add_command(label="Save")
# subMenu.add_separator() # creates a line to separate in group
# subMenu.add_command(label="Exit", command=quit)
#
# editMenu = Menu(menu, tearoff=0)
# menu.add_cascade(label="Edit", menu=editMenu)
# editMenu.add_command(label="Copy")
# editMenu.add_command(label="Redo")
# editMenu.add_command(label="Cut")
# editMenu.add_separator()
# editMenu.add_command(label="Restart")
#
# lykaMenu = Menu(menu, tearoff=0)
# menu.add_cascade(label="Lyka", menu=lykaMenu)
# lykaMenu.add_command(label="Love ko!")
# lykaMenu.add_command(label="Baby kooo!")
# lykaMenu.add_command(label="Mahal na mahal koooo.")
# lykaMenu.add_separator()
# lykaMenu.add_command(label="I LOVE YOU!")

#===============================================================================================================


#global variables
textInput = StringVar()
operator = ""

Top = Frame(root, width=1600, height=150, bg="black", bd=10, relief="raised")
Top.pack(side=TOP)

#main app frame window
frame1 = Frame(root, width=800, height=700, bg="black", relief=SUNKEN)
frame1.pack(side=LEFT)

frame2 = Frame(root, width=300, height=700, relief=SUNKEN)
frame2.pack(side=RIGHT)

#title of the program
programTitle = Label(Top, font=("times new roman", 50, "bold"), text="LYKA'S SOBRANG SARI-SARI STORE", fg="hot pink", bg="black", bd=10, anchor="w")
programTitle.grid(row=0, column=0)

#time of the program
#time/date of the day
localTime = time.asctime(time.localtime(time.time()))
time = StringVar()
time.set(localTime)
programTime = Entry(Top, font=("arial", 16, "bold"), textvariable=time, fg="white", bg="black", bd=10, width=30, justify="center")
programTime.grid(row=1, column=0)

#============================================VARIABLE FOR SYSTEM===================================================

# For System GUI
candies = StringVar()
spaghetti = StringVar()
grahamBall = StringVar()
chowFan = StringVar()
biscuits = StringVar()
snacks = StringVar()
drinks = StringVar()

costOfPurchases = StringVar()
serviceCharge = StringVar()
stateTax = StringVar()
subTotal = StringVar()
totalCost = StringVar()

candies.set("0")
spaghetti.set("0")
grahamBall.set("0")
chowFan.set("0")
biscuits.set("0")
snacks.set("0")
drinks.set("0")


#===========================================Main Application GUI Function=====================================================
def btnTotal(event):
    
    costOfCandies = float(candies.get())
    costOfSpaghetti = float(spaghetti.get())
    costOfGrahamBall = float(grahamBall.get())
    costOfChowFan = float(chowFan.get())
    costOfBiscuits = float(biscuits.get())
    costOfSnacks = float(snacks.get())
    costOfDrinks = float(drinks.get())

    priceOfCandies = costOfCandies * 1
    priceOfSpaghetti = costOfSpaghetti * 25
    priceOfGrahamBall = costOfGrahamBall * 6
    priceOfChowFan = costOfChowFan * 30
    priceOfBiscuits = costOfBiscuits * 8
    priceOfSnacks = costOfSnacks * 7
    priceOfDrinks = costOfDrinks * 10

    totalPurchases = "P", str("%.2f" % (priceOfCandies + priceOfSpaghetti + priceOfGrahamBall + priceOfChowFan + priceOfBiscuits + priceOfSnacks + priceOfDrinks))
    totalTax = (priceOfCandies + priceOfSpaghetti + priceOfGrahamBall + priceOfChowFan + priceOfBiscuits + priceOfSnacks + priceOfDrinks) * 0.2
    sumOfTheCost = (priceOfCandies + priceOfSpaghetti + priceOfGrahamBall + priceOfChowFan + priceOfBiscuits + priceOfSnacks + priceOfDrinks)
    paidTax = "P", str("%.2f" % totalTax)
    overAllCost = "P", ("%.2f" % (totalTax + sumOfTheCost))

    costOfPurchases.set(totalPurchases)
    stateTax.set(paidTax)
    subTotal.set(totalPurchases)
    totalCost.set(overAllCost)

    receipt = (priceOfCandies, priceOfSpaghetti, priceOfGrahamBall, priceOfChowFan, priceOfBiscuits, priceOfSnacks, priceOfDrinks, totalCost.get(), "He is paid?") 
    result = tkinter.messagebox.askquestion("Attention!", str(receipt))

## for reference number! 
    randomNumber = random.randint(1, 9999)
    generatedNumber = str(randomNumber)

#For output receipt
    print("\n\t\t\tLyka's Sobrang Sari-Sari Store\n")
    print("Date & Time: ", localTime)
    print("Receipt No.: #", generatedNumber, sep="")
    print("")
    print("Candies: P1 x ", int(costOfCandies), " = P", priceOfCandies, sep="")
    print("Spaghetti: P25 x ", int(costOfSpaghetti), " = P", priceOfSpaghetti, sep="")
    print("Graham Ball: P6 x ", int(costOfGrahamBall), " = P", priceOfGrahamBall, sep="")
    print("Chow Fan: P30 x ", int(costOfChowFan), " = P", priceOfChowFan, sep="")
    print("Biscuits: P8 x ", int(costOfBiscuits), " = P", priceOfBiscuits, sep="")
    print("Snacks: P7 x ", int(costOfSnacks), " = P", priceOfSnacks, sep="")
    print("Drinks: P10 x ", int(costOfDrinks), " = P", priceOfDrinks, sep="")
    print("Tax: 2%" )
    print("Subtotal: ", "P{:.2f}".format(sumOfTheCost), sep="")
    print("Total Tax of Purchases: ", "P{:.2f}".format(totalTax), sep="")
    print("")
    print("Total Cost: P{:.2f}".format(totalTax + sumOfTheCost), sep="")
    print("*************************************************************************")
    
def btnReset():
    candies.set("0")
    spaghetti.set("0")
    grahamBall.set("0")
    chowFan.set("0")
    biscuits.set("0")
    snacks.set("0")
    drinks.set("0")
    costOfPurchases.set("")
    serviceCharge.set("")
    stateTax.set("")
    subTotal.set("")
    totalCost.set("")

def btnExit():
    exitMessage = tkinter.messagebox.askquestion("Close Program", "Do you want to quit?")
    if exitMessage == "yes":
        root.destroy()
    
#===========================================CALCULATOR GUI BUTTONS=====================================================

#buttons for calculator
displayText = Entry(frame2, font=("arial", 20, "bold"), textvariable=textInput, bd=30, insertwidth=4, \
                    bg="powder blue", justify="right")
displayText.grid(columnspan=4)

button0 = Button(frame2, padx=16, pady=16, bd=8, fg="black", font=("arial", 20, "bold"), text="0", \
                    bg="powder blue", command=lambda: btnClick(0)).grid(row=5, column=0)
buttonClear = Button(frame2, padx=16, pady=16, bd=8, fg="black", font=("arial", 20, "bold"), text="C", \
                    bg="powder blue", command=btnClear).grid(row=5, column=1)
buttonEquals = Button(frame2, padx=16, pady=16, bd=8, fg="black", font=("arial", 20, "bold"), text="=", \
                    bg="powder blue", command=btnEquals).grid(row=5, column=2)
divisionOperator = Button(frame2, padx=16, pady=16, bd=8, fg="black", font=("arial", 20, "bold"), text="/", \
                    bg="powder blue", command=lambda: btnClick("/")).grid(row=5, column=3)

#===============================================================================================================

button1 = Button(frame2, padx=16, pady=16, bd=8, fg="black", font=("arial", 20, "bold"), text="1", \
                    bg="powder blue", command=lambda: btnClick(1)).grid(row=4, column=0)
button2 = Button(frame2, padx=16, pady=16, bd=8, fg="black", font=("arial", 20, "bold"), text="2", \
                    bg="powder blue", command=lambda: btnClick(2)).grid(row=4, column=1)
button3 = Button(frame2, padx=16, pady=16, bd=8, fg="black", font=("arial", 20, "bold"), text="3", \
                    bg="powder blue", command=lambda: btnClick(3)).grid(row=4, column=2)
multiplicationOperator = Button(frame2, padx=16, pady=16, bd=8, fg="black", font=("arial", 20, "bold"), text="*", \
                    bg="powder blue", command=lambda: btnClick("*")).grid(row=4, column=3)

#==============================================================================================================
button4 = Button(frame2, padx=16, pady=16, bd=8, fg="black", font=("arial", 20, "bold"), text="4", \
                    bg="powder blue", command=lambda: btnClick(4)).grid(row=3, column=0)
button5 = Button(frame2, padx=16, pady=16, bd=8, fg="black", font=("arial", 20, "bold"), text="5", \
                    bg="powder blue", command=lambda: btnClick(5)).grid(row=3, column=1)
button6 = Button(frame2, padx=16, pady=16, bd=8, fg="black", font=("arial", 20, "bold"), text="6", \
                    bg="powder blue", command=lambda: btnClick(6)).grid(row=3, column=2)
subtractionOperator = Button(frame2, padx=16, pady=16, bd=8, fg="black", font=("arial", 20, "bold"), text="-", \
                    bg="powder blue", command=lambda: btnClick("-")).grid(row=3, column=3)

#===============================================================================================================
button7 = Button(frame2, padx=16, pady=16, bd=8, fg="black", font=("arial", 20, "bold"), text="7", \
                    bg="powder blue", command=lambda: btnClick(7)).grid(row=2, column=0)
button8 = Button(frame2, padx=16, pady=16, bd=8, fg="black", font=("arial", 20, "bold"), text="8", \
                    bg="powder blue", command=lambda: btnClick(8)).grid(row=2, column=1)
button9 = Button(frame2, padx=16, pady=16, bd=8, fg="black", font=("arial", 20, "bold"), text="9", \
                    bg="powder blue", command=lambda: btnClick(9)).grid(row=2, column=2)
additionOperator = Button(frame2, padx=16, pady=16, bd=8, fg="black", font=("arial", 20, "bold"), text="+", \
                    bg="powder blue", command=lambda: btnClick("+")).grid(row=2, column=3)


#========================================MAIN APPLICATION INFO 1============================================
Candies = Label(frame1, font=("arial", 16, "bold"), text="Candies", bd=16,fg="white", bg="black", anchor="w")
Candies.grid(row=0, column=0)
textboxCandies = Entry(frame1, font=("arial", 16, "bold"), textvariable=candies, bd=10, insertwidth=4, bg="powder blue", justify="left")
textboxCandies.grid(row=0, column=1)


Spaghetti = Label(frame1, font=("arial", 16, "bold"), text="Spaghetti", fg="white", bg="black", bd=16, anchor="w")
Spaghetti.grid(row=1, column=0)
textboxSpaghetti = Entry(frame1, font=("arial", 16, "bold"), textvariable=spaghetti, bd=10, insertwidth=4, bg="powder blue", justify="left")
textboxSpaghetti.grid(row=1, column=1)


GrahamBall = Label(frame1, font=("arial", 16, "bold"), text="Graham Ball", fg="white", bg="black", bd=16, anchor="w")
GrahamBall.grid(row=2, column=0)
textboxGrahamBall = Entry(frame1, font=("arial", 16, "bold"), textvariable=grahamBall, bd=10, insertwidth=4, bg="powder blue", justify="left")
textboxGrahamBall.grid(row=2, column=1)


ChowFan = Label(frame1, font=("arial", 16, "bold"), text="Chow Fan", fg="white", bg="black", bd=16, anchor="w")
ChowFan.grid(row=3, column=0)
textboxChowFan = Entry(frame1, font=("arial", 16, "bold"), textvariable=chowFan, bd=10, insertwidth=4, bg="powder blue", justify="left")
textboxChowFan.grid(row=3, column=1)


Biscuit = Label(frame1, font=("arial", 16, "bold"), text="Biscuits", fg="white", bg="black", bd=16, anchor="w")
Biscuit.grid(row=4, column=0)
textboxBiscuit = Entry(frame1, font=("arial", 16, "bold"), textvariable=biscuits, bd=10, insertwidth=4, bg="powder blue", justify="left")
textboxBiscuit.grid(row=4, column=1)

Snacks = Label(frame1, font=("arial", 16, "bold"), text="Snacks", fg="white", bg="black", bd=16, anchor="w")
Snacks.grid(row=5, column=0)
textboxSnacks = Entry(frame1, font=("arial", 16, "bold"), textvariable=snacks, bd=10, insertwidth=4, bg="powder blue", justify="left")
textboxSnacks.grid(row=5, column=1)

#========================================MAIN APPLICATION INFO 2============================================

Drinks = Label(frame1, font=("arial", 16, "bold"), text="Drinks", fg="white", bg="black", bd=16, anchor="w")
Drinks.grid(row=0, column=2)
textboxDrinks = Entry(frame1, font=("arial", 16, "bold"), textvariable=drinks, bd=10, insertwidth=4, bg="powder blue", justify="left")
textboxDrinks.grid(row=0, column=3)
textboxDrinks.bind("<Return>", btnTotal)

CostOfPurchases = Label(frame1, font=("arial", 16, "bold"), text="Cost of Purchases", fg="white", bg="black", bd=16, anchor="w")
CostOfPurchases.grid(row=1, column=2)
textboxCostOfPurchases = Entry(frame1, font=("arial", 16, "bold"), textvariable=costOfPurchases, bd=10, insertwidth=4,  justify="left")
textboxCostOfPurchases.grid(row=1, column=3)

StateTax = Label(frame1, font=("arial", 16, "bold"), text="State Tax", fg="white", bg="black", bd=16, anchor="w")
StateTax.grid(row=2, column=2)
textboxStateTax = Entry(frame1, font=("arial", 16, "bold"), textvariable=stateTax, bd=10, insertwidth=4,  justify="left")
textboxStateTax.grid(row=2, column=3)

SubTotal = Label(frame1, font=("arial", 16, "bold"), text="Sub Total", fg="white", bg="black", bd=16, anchor="w")
SubTotal.grid(row=3, column=2)
textboxSubTotal = Entry(frame1, font=("arial", 16, "bold"), textvariable=subTotal, bd=10, insertwidth=4, justify="left")
textboxSubTotal.grid(row=3, column=3)

TotalCost = Label(frame1, font=("arial", 16, "bold"), text="Total Cost", fg="white", bg="black", bd=16, anchor="w")
TotalCost.grid(row=4, column=2)
textboxTotalCost = Entry(frame1, font=("arial", 16, "bold"), textvariable=totalCost, bd=10, insertwidth=4, justify="left", fg="red")
textboxTotalCost.grid(row=4, column=3)

#=======================================================MAIN APPLICATION BUTTONS===================================================

buttonTotal = Button(frame1, padx=16, pady=8, bd=16, fg="black", font=("arial", 16, "bold"), width=10, text="Total", bg="powder blue")
buttonTotal.grid(row=7, column=1)
buttonTotal.bind("<Button-1>", btnTotal)

buttonReset = Button(frame1, padx=16, pady=8, bd=16, fg="black", font=("arial", 16, "bold"), width=10, text="Reset", bg="powder blue", command=btnReset)\
    .grid(row=7, column=2)

buttonExit = Button(frame1, padx=16, pady=8, bd=16, fg="black", font=("arial", 16, "bold"), width=10, text="Exit", bg="powder blue", command=btnExit)\
    .grid(row=7, column=3)


root.mainloop()
