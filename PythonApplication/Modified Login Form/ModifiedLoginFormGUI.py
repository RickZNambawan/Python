from tkinter import *

class Application(Frame):
    def __init__(self, master):
        super(Application, self).__init__(master)
        self.grid()
        self.username = StringVar()
        self.password = StringVar()
        self.checkBox = BooleanVar()
        self.messageBox = StringVar()
        self.username.set("")
        self.password.set("")
        self.checkBox.set(True)
        self.createWidgets()

    def createWidgets(self):
        Label(self, text="Username:").grid(row=0, column=0, sticky=W)
        self.usernameEntry = Entry(self, textvariable=self.username)
        self.usernameEntry.grid(row=0, column=1, sticky=W)

        Label(self, text="Pasword:").grid(row=1, column=0, sticky=W)
        self.passwordEntry = Entry(self, textvariable=self.password, show="*")
        self.passwordEntry.grid(row=1, column=1, sticky=W)

        Label(self, text="Remember Me: ").grid(row=2, column=0, sticky=W)
        Checkbutton(self, variable=self.checkBox).grid(row=2, columnspan=2)

        self.submitButton = Button(self, text="Login Here", command=self.result)
        self.submitButton.grid(row=2, column=1)

        self.resetButton = Button(self, text="Reset", command=self.clearButton)
        self.resetButton.grid(row=2, column=2)

        self.resultBox = Text(self, width=50, height=10)
        self.resultBox.grid(row=3, column=1)

    def clearButton(self):
        self.username.set("")
        self.password.set("")
        self.messageBox.set("")
        self.checkBox.set(False)

    def result(self):
        message = ""
        self.prompt()
        if self.username.get() == "rickz" and self.password.get() == "pota":
            self.prompt()
            self.resultBox.delete(0.0, END)
            message += "Logged in Successfully!"
            message += "\nWelcome back, Frederick!\n"
            self.resultBox.insert(0.0, message)

        else:
            message += "Invalid Input! Please Try again!"

        self.username.set("")
        self.password.set("")
        self.checkBox.set(False)

        self.resultBox.delete(0.0, END)
        self.resultBox.insert(0.0, message)

    def prompt(self):
        print("You entered:\n")
        print("Username: {}".format(self.username.get()))
        print("Password: {}".format(self.password.get()))
        print("Remember Me: {}".format(bool(self.checkBox.get())))
        print("")

root = Tk()
root.title("Modified Login Form")
root.geometry("550x250")
mainFrame = Application(root)
root.mainloop()

