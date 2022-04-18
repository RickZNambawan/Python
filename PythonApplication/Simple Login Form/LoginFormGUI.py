from tkinter import *
import tkinter.messagebox


root = Tk()
root.title("My Simple Login Form")
textUser = StringVar()
textPass = StringVar()
textInput = StringVar()
operator = ""
def btnClear():
    userName.set("")
    passWord.set("")
    messageBox.set("Input not found!")
    checkBox.set(False)
def doNothing(event):
    print("NOTHING")
    
# MENU BAR
mainMenu = Menu(root)
root.config(menu=mainMenu)

fileMenu = Menu(mainMenu, tearoff=0)
mainMenu.add_cascade(menu=fileMenu, label="File")

fileMenu.add_command(label="New", command=doNothing)
fileMenu.add_command(label="Open...")
fileMenu.add_command(label="Open As...")
fileMenu.add_command(label="Recent Files")
fileMenu.add_separator()
fileMenu.add_command(label="Save")
fileMenu.add_command(label="Save As...")
fileMenu.add_command(label="Save Copy As...")
fileMenu.add_separator()
fileMenu.add_command(label="Print Window")
fileMenu.add_separator()
fileMenu.add_command(label="Close", command=quit)
fileMenu.add_command(label="Exit", command=quit)

editMenu = Menu(mainMenu, tearoff=0)
mainMenu.add_cascade(menu=editMenu, label="Edit")

editMenu.add_command(label="Undo")
editMenu.add_command(label="Redo")
editMenu.add_separator()
editMenu.add_command(label="Cut")
editMenu.add_command(label="Copy")
editMenu.add_command(label="Paste")
editMenu.add_command(label="Select All")
editMenu.add_separator()
editMenu.add_command(label="Find...")
editMenu.add_command(label="Find Again")
editMenu.add_command(label="Find Selection")
editMenu.add_command(label="Find in Files...")
editMenu.add_command(label="Replace")
editMenu.add_command(label="Go to Line")
editMenu.add_command(label="Show Completions")
editMenu.add_command(label="Expand Word")
editMenu.add_command(label="Show call tip")
editMenu.add_command(label="Show surrounding parens")

lykaMenu = Menu(mainMenu, tearoff=0)
mainMenu.add_cascade(menu=lykaMenu, label="Lyka")


fredMenu = Menu(mainMenu, tearoff=0)
mainMenu.add_cascade(menu=lykaMenu, label="Fred")


babyMenu = Menu(mainMenu, tearoff=0)
mainMenu.add_cascade(menu=lykaMenu, label="Babyy")

cuteMenu = Menu(mainMenu, tearoff=0)
mainMenu.add_cascade(menu=lykaMenu, label="BabyKo")
#********************************************************************************
def showInput(event):

    
    print("You entered:")
    print("Username: ", str(userName.get()))
    print("Password: ", str(passWord.get()))
    print("Remember Me: ", bool(checkBox.get()))
    print("")

    if userName.get() == "pogisifred" and passWord.get() == "gwapongfred":
        print("Logged in Successfully!")
        print("Welcome back, Frederick!\n")
        prompt = "Logged in Successfully!"        
        showInfo = tkinter.messagebox.askquestion("Logged in Successfully! ", "You can close the login form window to proceed to the program..")
    elif userName.get() == "pangitlyka" and passWord.get() == "pangittalaga":
        print("Logged in Successfully!")
        print("Welcome back, Mary Lyka!\n")
        prompt = "Logged in Successfully!"
        showInfo = tkinter.messagebox.askquestion("Logged in Successfully! ", "You can close the login form window to proceed to the program..")
    elif userName.get() == "marclawrence" and passWord.get() == "castaneda":
        print("Logged in Successfully!")
        print("Welcome back, Marc Lawrence!!\n")
        prompt = "Logged in Successfully!"
        showInfo = tkinter.messagebox.askquestion("Logged in Successfully! ", "You can close the login form window to proceed to the program..")
    else:
        print("Invalid username or password")
        print("*************************************************************************\n")
        prompt = "Invalid Input!"

        
    userName.set("")
    passWord.set("")
    checkBox.set(False)

    result = str(prompt)
    messageBox.set(result)

userName = StringVar()
passWord = StringVar()
checkBox = BooleanVar()
messageBox = StringVar()

userName.set("")
passWord.set("")
messageBox.set("Input not found!")


frame1 = Frame(root)


Label(frame1, text="Username:").grid(row=0, column=0, padx=2, pady=2)
entry1 = Entry(frame1, textvariable=userName, width=20)
entry1.grid(row=0, column=1, padx=2, pady=2)
entry1.bind("<Return>", showInput)

Label(frame1, text="Password:").grid(row=1, column=0, padx=2, pady=2)
entry2 = Entry(frame1, textvariable=passWord, show="*", width=20)
entry2.grid(row=1, column=1, padx=2, pady=2)
entry2.bind("<Return>", showInput)

Label(frame1, text="Remember Me").grid(row=2, column=0)
Checkbutton(frame1, variable=checkBox).grid(row=2, columnspan=2)

loginButton = Button(frame1, text="Login Here")
loginButton.grid(row=2, column=1)
loginButton.bind("<Button-1>", showInput)

resetButton = Button(frame1, text="Reset", command=btnClear).grid(row=2, column=3)


#***********************************************************************

frame2 = Frame(root)
entry3 = Entry(frame2, width=40, textvariable=messageBox).pack(side=LEFT, fill=X, padx=10, pady=10)





frame1.pack()
frame2.pack()
root.bind_all("<KeyPress-F1>", doNothing)
root.mainloop()

