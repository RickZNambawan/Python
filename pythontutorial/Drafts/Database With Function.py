import sqlite3

conn = sqlite3.connect("database.db")
c = conn.cursor()

# c.execute("DROP TABLE IF EXISTS Customers")
# c.execute("CREATE TABLE Customers (name TEXT, age INTEGER, orders INTEGER)")
c.execute("ALTER TABLE Customers")
# c.execute("MODIFY name TEXT, age INTEGER, orders INTEGER, number INTEGER")

def addCustomer():
    while True:
        question = input("Want to add? (y/n): ")
        if question.lower() == "no" or question.lower() == "n":
            break
        else:
            name = input("Enter name: ")
            age = int(input("Enter your age: "))
            orders = int(input("Enter your orders: "))
            print("")
            c.execute("INSERT INTO Customers (name, age, orders) VALUES (?, ?, ?)", (name, age, orders))
            conn.commit()
    
def viewDatabase():
    c.execute("SELECT name, age, orders FROM Customers")
    for name, age, orders in c:
        print("\nName: {} \nAge: {} \nOrders: {}".format(name, age, orders))

def deleteCustomer(name):
    c.execute("DELETE FROM Customers WHERE name = ?", (name,))
    conn.commit()

def updateCustomer(orders, name):
    c.execute("UPDATE Customers SET orders = ? WHERE name = ?", (orders, name))
    conn.commit()


addCustomer()
viewDatabase()

input("")

