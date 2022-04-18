from tkinter import *
import tkinter.messagebox
import sqlite3

conn = sqlite3.connect("library.db")
c = conn.cursor()

c.execute("DROP TABLE IF EXISTS LIBRARY")
c.execute("CREATE TABLE LIBRARY (name TEXT, author TEXT, iso TEXT, genre TEXT, position TEXT)")

class AddingBooks(Frame):
    def __init__(self, root):
        super().__init__(root)
        self.grid()
        self.name = StringVar()
        self.author = StringVar()
        self.iso = IntVar()
        self.genre = StringVar()
        self.position = StringVar()
        self.createWidgets()
        self.showDatabase()

    def createWidgets(self):
        Label(self, text="Name of the Book:", padx=70, width=12, height=3, font=("bold", 15)).grid(row=1, column=1)
        self.nameEntry = Entry(self, width=60, textvar=self.name)
        self.nameEntry.grid(row=1, column=2)

        Label(self, text="Author of the Book:", padx=70, width=12, height=3, font=("bold", 15)).grid(row=2, column=1)
        self.authorEntry = Entry(self, width=60, textvar=self.author)
        self.authorEntry.grid(row=2, column=2)

        Label(self, text="ISO Number:", padx=70, width=12, height=3, font=("bold", 15)).grid(row=3, column=1)
        self.isoNumber = Entry(self, width=60, textvar=self.iso)
        self.isoNumber.grid(row=3, column=2)

        Label(self, text="Genre of the Book:", padx=70, width=12, height=3, font=("bold", 15)).grid(row=4, column=1)
        self.genreEntry = Entry(self, width=60, textvar=self.genre)
        self.genreEntry.grid(row=4, column=2)

        Label(self, text="Position of the Book:", padx=70, width=12, height=3, font=("bold", 15)).grid(row=5, column=1)
        self.positionEntry = Entry(self, width=60, textvar=self.position)
        self.positionEntry.grid(row=5, column=2)

        self.addButton = Button(self, text="Add Book", width=20, height=3, padx=50, command=self.addBooks).grid(row=6, column=1)
        self.removeButton = Button(self, text="Remove Book", width=20, height=3, padx=50, command=self.removeBooks).grid(row=6, column=2)
        self.updateButton = Button(self, text="Update Book", width=20, height=3, padx=50, command=self.updateBooks).grid(row=6, column=3)
        self.exitButton = Button(self, text="EXIT", width=20, height=3, padx=50, command=self.exitProgram).grid(row=7, column=2)

        self.textBox = Text(self, width=100, height=23, padx=15)
        self.textBox.grid(row=8, column=1, columnspan=4)

    def showDatabase(self):
        c.execute("SELECT name, author, iso, genre, position FROM LIBRARY")
        self.counter = 0

        title = "List of Available Books: \n\n"
        self.textBox.insert(END, title)
        for name, author, iso, genre, position in c:
            self.counter += 1
            text = f"{self.counter}.) Name of the Book: {name} \nAuthor of the Book: {author} \nISO Number: {iso} " \
                   f"\nGenre of the Book: {genre} \nPosition of the Book: {position}\n\n"
            self.textBox.insert(END, text)

    def addBooks(self):
        c.execute("INSERT INTO LIBRARY (name, author, iso, genre, position) VALUES (?, ?, ?, ?, ?)",
                  (self.name.get(), self.author.get(), self.iso.get(), self.genre.get(), self.position.get()))
        conn.commit()

        while True:
            self.counter += 1
            text = f"{self.counter}.) Name of the Book: {self.name.get()} \nAuthor of the Book: {self.author.get()} \n" \
                   f"ISO Number: {self.iso.get()} \nGenre of the Book: {self.genre.get()} " \
                   f"\nPosition of the Book: {self.position.get()}\n\n"
            self.textBox.insert(END, text)
            self.name.set(""), self.author.set(""), self.iso.set(0), self.genre.set(""), self.position.set("")
            break

    def removeBooks(self):
        c.execute("DELETE FROM LIBRARY WHERE name = ?", (self.name.get(),))
        conn.commit()
        self.textBox.delete(0.0, END)
        self.showDatabase()


    def updateBooks(self):
        print("Update")
        if self.name.get():
            c.execute("UPDATE LIBRARY SET name = ? WHERE author = ?", (self.name.get(), self.author.get()))
            conn.commit()
            self.textBox.delete(0.0, END)
            self.showDatabase()
        elif self.author.get():
            c.execute("UPDATE LIBRARY SET author = ? WHERE name = ?", (self.author.get(), self.name.get()))
            conn.commit()
            self.textBox.delete(0.0, END)
            self.showDatabase()
        else:
            print("None")

    def exitProgram(self):
        exitMessage = tkinter.messagebox.askquestion("Close the Program", "Do you want to Exit the Program?")
        if exitMessage == "yes":
            exit()

root = Tk()
root.title("Library App")
root.geometry("900x900+480+60")
mainFrame = AddingBooks(root)
root.mainloop()


