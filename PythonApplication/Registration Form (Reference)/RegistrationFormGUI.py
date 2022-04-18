from tkinter import *
import sqlite3

root = Tk()
root.geometry("500x500")
root.title("Registration Form")

# name = StringVar()
# mail = StringVar()
# var = IntVar()
# c = StringVar()
# var1 = IntVar()
# var2 = IntVar()
# def database():
#     fullname = name.get()
#     email = mail.get()
#     gender = var.get()
#     country = c.get()
#     prog = var1.get()
#     conn = sqlite3.connect("Form.db")
#     with conn:
#         cursor = conn.cursor()
#     cursor.execute("CREATE TABLE IF NOT EXISTS Student (Fullname TEXT, Email TEXT, Gender TEXT, Country TEXT, Programming TEXT)")
#     cursor.execute("INSERT INTO Student (Fullname, Email, Gender, Country, Programming) VALUES (?, ?, ?, ?, ?)"), (fullname, email, gender, country, prog)
#     conn.commit()


Label(root, text="Registration Form", width=20, font=("bold", 20)).place(x=90, y=53)

Label(root, text="Fullname", width=20, font=("bold", 10)).place(x=80, y=130)
entryName = Entry(root)
entryName.place(x=240, y=130)

Label(root, text="Email", width=20, font=("bold", 10)).place(x=68, y=180)
entryMail = Entry(root)
entryMail.place(x=240, y=180)

Label(root, text="Gender", width=20, font=("bold", 10)).place(x=70, y=230)
Radiobutton(root, text="Male", padx=5, value=1).place(x=235, y=230)
Radiobutton(root, text="Female", padx=20, value=2).place(x=290, y=230)

Label(root, text="Country", width=20, font=("bold", 10)).place(x=70, y=280)

myList = ["Canada", "India", "UK", "Philippines", "Iceland", "South Africa"]
countries = StringVar()
countries.set("Select Your Country")
countryList = OptionMenu(root, countries, *myList)
countryList.place(x=240, y=280)
countryList.configure(width=15)

Label(root, text="Programming", width=20, font=("bold", 10)).place(x=85, y=330)
Checkbutton(root, text="Java").place(x=235, y=330)
Checkbutton(root, text="Python").place(x=290, y=330)

Button(root, text="Submit", width=20, bg="brown", fg="white").place(x=180, y=380)

root.mainloop()


