import sqlite3

conn = sqlite3.connect("sample.db")
c = conn.cursor()

# c.execute("DROP TABLE IF EXISTS Employee")
# c.execute("CREATE TABLE Employee(name TEXT, position TEXT, salary INTEGER )")


name = "Lyka"
position = "Engineer"
salary = 100000
myDict = {}

c.execute("INSERT INTO Employee(name, position, salary) VALUES (?, ?, ?)", (name, position, salary))
conn.commit()


c.execute("SELECT name, position, salary FROM Employee")


c.execute("DELETE FROM Employee WHERE name = 'Lyka'")
conn.commit()

conn.close()