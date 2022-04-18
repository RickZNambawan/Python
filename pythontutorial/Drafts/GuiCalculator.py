from tkinter import*

def doNothing():
    print("Easy breezy!")

def closeApp():
    print("Closing Windows")
    exit()

root = Tk()
root.config(background = "#e1f4ff")
root.geometry("213x264+0+0")

root.title("Calculator")


#Menu bar

menu = Menu(root)
root.config (menu = menu)


viewMenu = Menu (menu, tearoff = 0)
editMenu = Menu (menu, tearoff = 0)
helpMenu = Menu (menu, tearoff = 0)

#Creating Menu Bar
menu.add_cascade(label = "View", menu = viewMenu)
menu.add_cascade(label = "Edit", menu = editMenu)
menu.add_cascade(label = "Help", menu = helpMenu)


viewMenu.add_command(label = "Standard                              Alt+1", command = doNothing)
viewMenu.add_command(label = "Scientific                             Alt+2")
viewMenu.add_command(label = "Programmer                       Alt+3")
viewMenu.add_command(label = "Statistics                              Alt+4")
viewMenu.add_separator()
viewMenu.add_command(label = "History                              Ctrl+H")
viewMenu.add_command(label = "Digit grouping")
viewMenu.add_separator()
viewMenu.add_command(label = "Basic                                  Ctrl+F4")
viewMenu.add_command(label = "Unit conversion                 Ctrl+U")
viewMenu.add_command(label = "Date calculation                 Ctrl+E")
viewMenu.add_command(label = "Worksheets")
viewMenu.add_command(label = "Exit", command = closeApp)

editMenu.add_command(label = "Copy                   Ctrl+C")
editMenu.add_command(label = "Paste                   Ctrl+V")
editMenu.add_separator()
editMenu.add_command(label = "History")

helpMenu.add_command(label = "View Help                             F1")
helpMenu.add_separator()
helpMenu.add_command(label = "About Calculator")

textInput = StringVar()

frame1 = Frame(root, width=192, height=50)
frame1.pack(side=TOP)

frame2 = Frame(root, width=192, height=200, relief=SUNKEN)
frame2.pack(side=BOTTOM)

Haha = Entry(frame1, font=("arial", 20, "bold"), textvariable=textInput, \
                    bg="powder blue", justify="right") 
Haha.grid(columnspan=1)

root.mainloop()
