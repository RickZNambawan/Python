from tkinter import*
import random
import time;

#window
root = Tk()
root.geometry("1600x800+0+0")
root.title("Fred's Iron Works Data System")

def doNothing():
    print("Do nothing")

menu = Menu(root) # Creates a main menu to main window
root.config(menu=menu) # to configure tkinter that you creates a menu

# ***** Creating a Main Menu ********

subMenu = Menu(menu, tearoff=0) # creates a sub menu into a main menu # tearoff=0 - to remove the "----" at the submenu

# add a drop down menu to the menus
menu.add_cascade(label="File", menu=subMenu) # creates a menu without commands
subMenu.add_command(label="New", command=doNothing) # creates a menu with a commands
subMenu.add_command(label="Save", command=doNothing)
subMenu.add_separator() # creates a line to separate in group
subMenu.add_command(label="Exit", command=quit)

editMenu = Menu(menu, tearoff=0)
menu.add_cascade(label="Edit", menu=editMenu)
editMenu.add_command(label="Copy", command=doNothing)
editMenu.add_command(label="Redo", command=doNothing)
editMenu.add_command(label="Cut", command=doNothing)
editMenu.add_separator()
editMenu.add_command(label="Restart", command=doNothing)

lykaMenu = Menu(menu, tearoff=0)
menu.add_cascade(label="Lyka", menu=lykaMenu)
lykaMenu.add_command(label="Love ko!", command=doNothing)
lykaMenu.add_command(label="Baby kooo!", command=doNothing)
lykaMenu.add_command(label="Mahal na mahal koooo.", command=doNothing)
lykaMenu.add_separator()
lykaMenu.add_command(label="I LOVE YOU!", command=doNothing)

#time/date of the day
localTime = time.asctime(time.localtime(time.time()))

#global variables
textInput = StringVar()
operator = ""

Top = Frame(root, width=1600, height=50, relief=SUNKEN)
Top.pack(side=TOP)

#main app
frame1 = Frame(root, width=800, height=700, relief=SUNKEN)
frame1.pack(side=LEFT)
frame2 = Frame(root, width=300, height=700, relief=SUNKEN)
frame2.pack(side=RIGHT)


#title of the program
#time of the program
programTitle = Label(Top, font=("arial", 50, "bold"), text="Fred's Iron Works System", fg="Steel Blue", bd=10, anchor="w")
programTitle.grid(row=0, column=0)

programTime = Label(Top, font=("arial", 20, "bold"), text=localTime, fg="Steel Blue", bd=10, anchor="w")
programTime.grid(row=1, column=0)

#===========================================CALCULATOR GUI=====================================================

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

def btnTotal():
    randomReference = random.randint(1, 58796086786)
    referenceNumber = str(randomReference)
    randomNumber.set(referenceNumber)

    costOfFries = float(fries.get())
    costOfBurger = float(burger.get())
    costOfFillet = float(fillet.get())
    costOfChicken = float(chicken.get())
    costOfCheese = float(cheese.get())
    costOfDrinks = float(drinks.get())

    priceOfFries = costOfFries * 36
    priceOfBurger = costOfBurger * 30
    priceOfFillet = costOfFillet * 59
    priceOfChicken = costOfChicken * 89
    priceOfCheese = costOfCheese * 10
    priceOfDrinks = costOfDrinks * 25

    totalMeal = "P", str("%.2f" % (priceOfFries + priceOfBurger + priceOfFillet + priceOfChicken + priceOfCheese + priceOfDrinks))

    totalTax = (priceOfFries + priceOfBurger + priceOfFillet + priceOfChicken + priceOfCheese + priceOfDrinks) * 0.2

    sumOfTheCost = (priceOfFries + priceOfBurger + priceOfFillet + priceOfChicken + priceOfCheese + priceOfDrinks)

    totalServiceCharge = (priceOfFries + priceOfBurger + priceOfFillet + priceOfChicken + priceOfCheese + priceOfDrinks) / 99

    Service = "P", str("%.2f" % totalServiceCharge)

    overAllCost = "P", ("%.2f" % (totalTax + sumOfTheCost + totalServiceCharge))

    paidTax = "P", str("%.2f" % totalTax)

    costOfMeal.set(totalMeal)
    serviceCharge.set(Service)
    stateTax.set(paidTax)
    subTotal.set(totalMeal)
    totalCost.set(overAllCost)

def btnReset():
    randomNumber.set("")
    fries.set("0")
    burger.set("0")
    fillet.set("0")
    chicken.set("0")
    cheese.set("0")
    drinks.set("0")
    costOfMeal.set("")
    serviceCharge.set("")
    stateTax.set("")
    subTotal.set("")
    totalCost.set("")

def btnExit():
    root.destroy()

displayText = Entry(frame2, font=("arial", 20, "bold"), textvariable=textInput, bd=30, insertwidth=4, \
                    bg="powder blue", justify="right")
displayText.grid(columnspan=4)


#buttons for calculator

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

#===============================================================================================================

# For System GUI
randomNumber = StringVar()
fries = StringVar()
burger = StringVar()
fillet = StringVar()
chicken = StringVar()
cheese = StringVar()

drinks = StringVar()
costOfMeal = StringVar()
serviceCharge = StringVar()
stateTax = StringVar()
subTotal = StringVar()
totalCost = StringVar()

fries.set("0")
burger.set("0")
fillet.set("0")
chicken.set("0")
cheese.set("0")

drinks.set("0")

#========================================FRED'S IRON WORKS SHOP INFO 1============================================
Reference = Label(frame1, font=("arial", 16, "bold"), text="Reference #", bd=16, anchor="w")
Reference.grid(row=0, column=0)
textboxReference = Entry(frame1, font=("arial", 16, "bold"), textvariable=randomNumber, bd=10, insertwidth=4, justify="left")
textboxReference.grid(row=0, column=1)


Fries = Label(frame1, font=("arial", 16, "bold"), text="Large Fries", bd=16, anchor="w")
Fries.grid(row=1, column=0)
textboxFries = Entry(frame1, font=("arial", 16, "bold"), textvariable=fries, bd=10, insertwidth=4, bg="powder blue", justify="left")
textboxFries.grid(row=1, column=1)


Burger = Label(frame1, font=("arial", 16, "bold"), text="Burger Meal", bd=16, anchor="w")
Burger.grid(row=2, column=0)
textboxBurger = Entry(frame1, font=("arial", 16, "bold"), textvariable=burger, bd=10, insertwidth=4, bg="powder blue", justify="left")
textboxBurger.grid(row=2, column=1)


Fillet = Label(frame1, font=("arial", 16, "bold"), text="Fillet Meal", bd=16, anchor="w")
Fillet.grid(row=3, column=0)
textboxFillet = Entry(frame1, font=("arial", 16, "bold"), textvariable=fillet, bd=10, insertwidth=4, bg="powder blue", justify="left")
textboxFillet.grid(row=3, column=1)


Chicken = Label(frame1, font=("arial", 16, "bold"), text="Chicken Meal", bd=16, anchor="w")
Chicken.grid(row=4, column=0)
textboxChicken = Entry(frame1, font=("arial", 16, "bold"), textvariable=chicken, bd=10, insertwidth=4, bg="powder blue", justify="left")
textboxChicken.grid(row=4, column=1)

Cheese = Label(frame1, font=("arial", 16, "bold"), text="Cheese Meal", bd=16, anchor="w")
Cheese.grid(row=5, column=0)
textboxCheese = Entry(frame1, font=("arial", 16, "bold"), textvariable=cheese, bd=10, insertwidth=4, bg="powder blue", justify="left")
textboxCheese.grid(row=5, column=1)

#========================================FRED'S IRON WORKS SHOP INFO 2============================================

Drinks = Label(frame1, font=("arial", 16, "bold"), text="Drinks", bd=16, anchor="w")
Drinks.grid(row=0, column=2)
textboxDrinks = Entry(frame1, font=("arial", 16, "bold"), textvariable=drinks, bd=10, insertwidth=4, bg="powder blue", justify="left")
textboxDrinks.grid(row=0, column=3)


CostOfMeal = Label(frame1, font=("arial", 16, "bold"), text="Cost of Meal", bd=16, anchor="w")
CostOfMeal.grid(row=1, column=2)
textboxCostOfMeal = Entry(frame1, font=("arial", 16, "bold"), textvariable=costOfMeal, bd=10, insertwidth=4,  justify="left")
textboxCostOfMeal.grid(row=1, column=3)


ServiceCharge = Label(frame1, font=("arial", 16, "bold"), text="Service Charge", bd=16, anchor="w")
ServiceCharge.grid(row=2, column=2)
textboxServiceCharge = Entry(frame1, font=("arial", 16, "bold"), textvariable=serviceCharge, bd=10, insertwidth=4,  justify="left")
textboxServiceCharge.grid(row=2, column=3)


StateTax = Label(frame1, font=("arial", 16, "bold"), text="State Tax", bd=16, anchor="w")
StateTax.grid(row=3, column=2)
textboxStateTax = Entry(frame1, font=("arial", 16, "bold"), textvariable=stateTax, bd=10, insertwidth=4,  justify="left")
textboxStateTax.grid(row=3, column=3)


SubTotal = Label(frame1, font=("arial", 16, "bold"), text="Sub Total", bd=16, anchor="w")
SubTotal.grid(row=4, column=2)
textboxSubTotal = Entry(frame1, font=("arial", 16, "bold"), textvariable=subTotal, bd=10, insertwidth=4, justify="left")
textboxSubTotal.grid(row=4, column=3)

TotalCost = Label(frame1, font=("arial", 16, "bold"), text="Total Cost", bd=16, anchor="w")
TotalCost.grid(row=5, column=2)
textboxTotalCost = Entry(frame1, font=("arial", 16, "bold"), textvariable=totalCost, bd=10, insertwidth=4, justify="left", fg="red")
textboxTotalCost.grid(row=5, column=3)

#=======================================================BUTTONS===================================================

buttonTotal = Button(frame1, padx=16, pady=8, bd=16, fg="black", font=("arial", 16, "bold"), width=10, text="Total", bg="powder blue", command=btnTotal)\
    .grid(row=7, column=1)

buttonReset = Button(frame1, padx=16, pady=8, bd=16, fg="black", font=("arial", 16, "bold"), width=10, text="Reset", bg="powder blue", command=btnReset)\
    .grid(row=7, column=2)

buttonExit = Button(frame1, padx=16, pady=8, bd=16, fg="black", font=("arial", 16, "bold"), width=10, text="Exit", bg="powder blue", command=btnExit)\
    .grid(row=7, column=3)


root.mainloop()
