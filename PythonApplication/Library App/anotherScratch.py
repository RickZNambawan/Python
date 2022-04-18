# from tkinter import *
# import tkinter.messagebox
# import sqlite3
#
# conn = sqlite3.connect("library.db")
# c = conn.cursor()
#
#
# # class MainApplication(Tk):
# #     def __init__(self, *args, **kwargs):
# #         Tk.__init__(self, *args, *kwargs)
# #         self.container = Frame(self)
# #         self.container.grid()
# #         self.frames = {}
# #         # self.addingWindows()
# #         # self.showFrame(AddingBooks)
# #         AddingBooks(parent, controller)
# #     # def addingWindows(self):
# #     #     for windows in (AddingBooks, RemovingBooks, UpdatingBooks):
# #     #         frame = windows(self.container, self)
# #     #         self.frames[windows] = frame
# #     #         frame.grid(row=0, column=0, sticky="nsew")
# #
# #     # def showFrame(self, container):
# #     #     frame = self.frames[container]
# #     #     frame.tkraise()
#
#
# class AddingBooks(Frame):
#     def __init__(self, parent):  # AddingBooks(root, MainApplication)
#         Frame.__init__(self, parent)
#         self.name = StringVar()
#         self.author = StringVar()
#         self.iso = IntVar()
#         self.genre = StringVar()
#         self.position = StringVar()
#         self.createWidgets()
#         self.showDatabase()
#
#     def createWidgets(self):
#         Label(self, text="Name of the Book:", padx=70, width=12, height=3, font=("bold", 15)).grid(row=1, column=1)
#         self.nameEntry = Entry(self, width=60, textvar=self.name)
#         self.nameEntry.grid(row=1, column=2)
#
#         Label(self, text="Author of the Book:", padx=70, width=12, height=3, font=("bold", 15)).grid(row=2, column=1)
#         self.authorEntry = Entry(self, width=60, textvar=self.author)
#         self.authorEntry.grid(row=2, column=2)
#
#         Label(self, text="ISO Number:", padx=70, width=12, height=3, font=("bold", 15)).grid(row=3, column=1)
#         self.isoNumber = Entry(self, width=60, textvar=self.iso)
#         self.isoNumber.grid(row=3, column=2)
#
#         Label(self, text="Genre of the Book:", padx=70, width=12, height=3, font=("bold", 15)).grid(row=4, column=1)
#         self.genreEntry = Entry(self, width=60, textvar=self.genre)
#         self.genreEntry.grid(row=4, column=2)
#
#         Label(self, text="Position of the Book:", padx=70, width=12, height=3, font=("bold", 15)).grid(row=5, column=1)
#         self.positionEntry = Entry(self, width=60, textvar=self.position)
#         self.positionEntry.grid(row=5, column=2)
#
#         self.addButton = Button(self, text="Add Book", width=20, height=3, padx=50, command=self.addBooks).grid(row=6, column=1)
#         # self.removeButton = Button(self, text="Remove Book", width=20, height=3, padx=50, command=lambda: controller.showFrame(RemovingBooks)).grid(row=6, column=2)
#         # self.updateButton = Button(self, text="Update Book", width=20, height=3, padx=50, command=lambda: controller.showFrame(UpdatingBooks)).grid(row=6, column=3)
#         # self.refreshButton = Button(self, text="Refresh List", width=20, height=3, padx=50, command=self.showDatabase).grid(row=7, column=1)
#         self.showButton = Button(self, text="Show List of Books", width=20, height=3, padx=50, command=self.showBooks).grid(row=7, column=2)
#         self.exitButton = Button(self, text="EXIT", width=20, height=3, padx=50, command=self.exitProgram).grid(row=7, column=3)
#
#         self.textBox = Text(self, width=100, height=23, padx=15)
#         self.textBox.grid(row=8, column=1, columnspan=4)
#
#     def showDatabase(self):
#         self.textBox.delete(0.0, END)
#         self.counter = 0
#         c.execute("SELECT name, author, iso, genre, position FROM LIBRARY")
#         title = "List of Available Books: \n\n"
#         self.textBox.insert(END, title)
#         for name, author, iso, genre, position in c:
#             self.counter += 1
#             text = "{}.) Name of the Book: {} \nAuthor of the Book: {} \nISO Number: {} " \
#                    "\nGenre of the Book: {} \nPosition of the Book: {}\n\n".format(self.counter, name, author, iso, genre, position)
#             self.textBox.insert(END, text)
#
#
#     def showBooks(self):
#         db = Database()
#         db.geometry("460x900+5+60")
#         db.mainloop()
#
#     def addBooks(self):
#         c.execute("INSERT INTO LIBRARY (name, author, iso, genre, position) VALUES (?, ?, ?, ?, ?)",
#                   (self.name.get(), self.author.get(), self.iso.get(), self.genre.get(), self.position.get()))
#         conn.commit()
#
#         while True:
#             self.counter += 1
#             text = "{}.) Name of the Book: {} \nAuthor of the Book: {} \nISO Number: {} " \
#                    "\nGenre of the Book: {} \nPosition of the Book: {}\n\n"\
#                 .format(self.counter, self.name.get(), self.author.get(), self.iso.get(), self.genre.get(), self.position.get())
#             self.textBox.insert(END, text)
#             self.name.set(""), self.author.set(""), self.iso.set(0), self.genre.set(""), self.position.set("")
#             break
#
#     def exitProgram(self):
#         exitMessage = tkinter.messagebox.askquestion("Close the Program", "Do you want to Exit the Program?")
#         if exitMessage == "yes":
#             exit()
#
#
# # class RemovingBooks(Frame):
# #     def __init__(self, parent, controller):
# #         Frame.__init__(self, parent)
# #         self.name = StringVar()
# #         self.removeEntry = Entry(self, textvar=self.name).grid()
# #         self.removeButton = Button(self, text="Remove Button", command=self.removeBooks).grid()
# #         self.homeButton = Button(self, text="Back to Home", command=lambda: controller.showFrame(AddingBooks)).grid()
# #         self.doNothing = Button(self, text="Wala lang", command=lambda: print("GAGO")).grid()
# #
# #     def removeBooks(self):
# #         c.execute("DELETE FROM LIBRARY WHERE name = ?", (self.name.get(),))
# #         conn.commit()
# #
# #
# # class UpdatingBooks(Frame):
# #     def __init__(self, parent):
# #         Frame.__init__(self, parent)
# #         self.name = StringVar()
# #         self.author = StringVar()
# #
# #         Label(self, text="Name of the Book").grid()
# #         self.nameEntry = Entry(self, textvar=self.name).grid()
# #
# #         Label(self, text="Author of the Book").grid()
# #         self.authorEntry = Entry(self, textvar=self.author).grid()
# #         self.updateButton = Button(self, text="Update", command=self.updateBooks).grid()
# #
# #         self.homeButton = Button(self, text="Back to Home", command=lambda: controller.showFrame(AddingBooks)).grid()
# #
# #         self.textBox = Text(self, width=100, height=23, padx=15)
# #         self.textBox.grid(row=8, column=1, columnspan=4)
# #
# #         self.showDatabase()
# #
# #     def updateBooks(self):
# #         if self.name.get():
# #             c.execute("UPDATE LIBRARY SET name = ? WHERE author = ?", (self.name.get(), self.author.get()))
# #             conn.commit()
# #             self.textBox.delete(0.0, END)
# #             self.showDatabase()
# #         elif self.author.get():
# #             c.execute("UPDATE LIBRARY SET author = ? WHERE name = ?", (self.author.get(), self.name.get()))
# #             conn.commit()
# #             self.textBox.delete(0.0, END)
# #             self.showDatabase()
# #
# #     def showDatabase(self):
# #         self.counter = 0
# #         c.execute("SELECT name, author, iso, genre, position FROM LIBRARY")
# #         title = "List of Available Books: \n\n"
# #         self.textBox.insert(END, title)
# #         for name, author, iso, genre, position in c:
# #             self.counter += 1
# #             text = "{}.) Name of the Book: {} \nAuthor of the Book: {} \nISO Number: {} " \
# #                    "\nGenre of the Book: {} \nPosition of the Book: {}\n\n".format(self.counter, name, author, iso, genre, position)
# #             self.textBox.insert(END, text)
#
# class Database(Tk):
#     def __init__(self, *args, **kwargs):
#         Tk.__init__(self, *args, **kwargs)
#         Label(self, text="LIST OF AVAILABLE BOOKS", font=("bold", 15)).pack(pady=40)
#         self.textBox = Text(self, width=54, height=40, padx=2)
#         self.textBox.pack(padx=10, pady=40)
#         self.refreshButton = Button(self, text="Refresh List", command=self.listOfBooks).pack()
#         self.listOfBooks()
#     def listOfBooks(self):
#         self.textBox.delete(0.0, END)
#         self.counter = 0
#         c.execute("SELECT name, author, iso, genre, position FROM LIBRARY")
#         title = "List of Available Books: \n\n"
#         self.textBox.insert(END, title)
#         for name, author, iso, genre, position in c:
#             self.counter += 1
#             text = "{}.) Name of the Book: {} \nAuthor of the Book: {} \nISO Number: {} " \
#                    "\nGenre of the Book: {} \nPosition of the Book: {}\n\n".format(self.counter, name, author, iso, genre, position)
#             self.textBox.insert(END, text)
#
#
# # app = MainApplication()
# # app.title("Library Application")
# # app.geometry("900x900+480+60")
# # app.mainloop()
#
# root = Tk()
# root.geometry("900x900+480+60")
# mainFrame = AddingBooks(root)
# mainFrame.grid()
# mainFrame.mainloop()


###############################################################################################################################################

from tkinter import *
import tkinter.messagebox
import sqlite3

conn = sqlite3.connect("library.db")
c = conn.cursor()

# c.execute("CREATE TABLE LIBRARY (name TEXT, author TEXT, iso INTEGER, genre TEXT, position TEXT)")

class AddingBooks(Frame):
    def __init__(self, parent):  # AddingBooks(root, MainApplication)
        Frame.__init__(self, parent)
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
        # self.removeButton = Button(self, text="Remove Book", width=20, height=3, padx=50, command=lambda: controller.showFrame(RemovingBooks)).grid(row=6, column=2)
        # self.updateButton = Button(self, text="Update Book", width=20, height=3, padx=50, command=lambda: controller.showFrame(UpdatingBooks)).grid(row=6, column=3)
        # self.refreshButton = Button(self, text="Refresh List", width=20, height=3, padx=50, command=self.showDatabase).grid(row=7, column=1)
        self.showButton = Button(self, text="Show List of Books", width=20, height=3, padx=50, command=self.showBooks).grid(row=7, column=2)
        self.exitButton = Button(self, text="EXIT", width=20, height=3, padx=50, command=self.exitProgram).grid(row=7, column=3)

        self.textBox = Text(self, width=100, height=23, padx=15)
        self.textBox.grid(row=8, column=1, columnspan=4)

    def showDatabase(self):
        self.textBox.delete(0.0, END)
        self.counter = 0
        c.execute("SELECT name, author, iso, genre, position FROM LIBRARY")
        title = "List of Available Books: \n\n"
        self.textBox.insert(END, title)
        for name, author, iso, genre, position in c:
            self.counter += 1
            text = "{}.) Name of the Book: {} \nAuthor of the Book: {} \nISO Number: {} " \
                   "\nGenre of the Book: {} \nPosition of the Book: {}\n\n".format(self.counter, name, author, iso, genre, position)
            self.textBox.insert(END, text)


    def showBooks(self):
        db = Database()
        db.geometry("460x900+5+60")
        db.mainloop()

    def addBooks(self):
        c.execute("INSERT INTO LIBRARY (name, author, iso, genre, position) VALUES (?, ?, ?, ?, ?)",
                  (self.name.get(), self.author.get(), self.iso.get(), self.genre.get(), self.position.get()))
        conn.commit()

        while True:
            self.counter += 1
            text = "{}.) Name of the Book: {} \nAuthor of the Book: {} \nISO Number: {} " \
                   "\nGenre of the Book: {} \nPosition of the Book: {}\n\n"\
                .format(self.counter, self.name.get(), self.author.get(), self.iso.get(), self.genre.get(), self.position.get())
            self.textBox.insert(END, text)
            self.name.set(""), self.author.set(""), self.iso.set(0), self.genre.set(""), self.position.set("")
            break

    def exitProgram(self):
        exitMessage = tkinter.messagebox.askquestion("Close the Program", "Do you want to Exit the Program?")
        if exitMessage == "yes":
            exit()


# class RemovingBooks(Frame):
#     def __init__(self, parent, controller):
#         Frame.__init__(self, parent)
#         self.name = StringVar()
#         self.removeEntry = Entry(self, textvar=self.name).grid()
#         self.removeButton = Button(self, text="Remove Button", command=self.removeBooks).grid()
#         self.homeButton = Button(self, text="Back to Home", command=lambda: controller.showFrame(AddingBooks)).grid()
#         self.doNothing = Button(self, text="Wala lang", command=lambda: print("GAGO")).grid()
#
#     def removeBooks(self):
#         c.execute("DELETE FROM LIBRARY WHERE name = ?", (self.name.get(),))
#         conn.commit()
#
#
# class UpdatingBooks(Frame):
#     def __init__(self, parent):
#         Frame.__init__(self, parent)
#         self.name = StringVar()
#         self.author = StringVar()
#
#         Label(self, text="Name of the Book").grid()
#         self.nameEntry = Entry(self, textvar=self.name).grid()
#
#         Label(self, text="Author of the Book").grid()
#         self.authorEntry = Entry(self, textvar=self.author).grid()
#         self.updateButton = Button(self, text="Update", command=self.updateBooks).grid()
#
#         self.homeButton = Button(self, text="Back to Home", command=lambda: controller.showFrame(AddingBooks)).grid()
#
#         self.textBox = Text(self, width=100, height=23, padx=15)
#         self.textBox.grid(row=8, column=1, columnspan=4)
#
#         self.showDatabase()
#
#     def updateBooks(self):
#         if self.name.get():
#             c.execute("UPDATE LIBRARY SET name = ? WHERE author = ?", (self.name.get(), self.author.get()))
#             conn.commit()
#             self.textBox.delete(0.0, END)
#             self.showDatabase()
#         elif self.author.get():
#             c.execute("UPDATE LIBRARY SET author = ? WHERE name = ?", (self.author.get(), self.name.get()))
#             conn.commit()
#             self.textBox.delete(0.0, END)
#             self.showDatabase()
#
#     def showDatabase(self):
#         self.counter = 0
#         c.execute("SELECT name, author, iso, genre, position FROM LIBRARY")
#         title = "List of Available Books: \n\n"
#         self.textBox.insert(END, title)
#         for name, author, iso, genre, position in c:
#             self.counter += 1
#             text = "{}.) Name of the Book: {} \nAuthor of the Book: {} \nISO Number: {} " \
#                    "\nGenre of the Book: {} \nPosition of the Book: {}\n\n".format(self.counter, name, author, iso, genre, position)
#             self.textBox.insert(END, text)

class Database(Tk):
    def __init__(self, *args, **kwargs):
        Tk.__init__(self, *args, **kwargs)
        Label(self, text="LIST OF AVAILABLE BOOKS", font=("bold", 15)).pack(pady=40)
        self.textBox = Text(self, width=54, height=40, padx=2)
        self.textBox.pack(padx=10, pady=40)
        self.refreshButton = Button(self, text="Refresh List", command=lambda: AddingBooks.showDatabase(self)).pack()
        showDatabase = AddingBooks.showDatabase(self)


root = Tk()
root.geometry("900x900+480+60")
mainFrame = AddingBooks(root)
mainFrame.grid()
mainFrame.mainloop()
