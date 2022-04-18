import sqlite3

conn = sqlite3.connect("hotel.db")
c = conn.cursor()

c.execute("DROP TABLE IF EXISTS Hotel")
c.execute("CREATE TABLE Hotel (name TEXT, age INTEGER, date INTEGER)")


class HotelManagement:
    def __init__(self):
        pass

    def customer_detail(self, name, age, date):
        print(name, age, date)
        # for databases
        pass

    def rooms(self):
        superior_double = 10000
        superior_twin = 8000
        superior_triple = 5000
        premier = 3000
        studio = 1000


ue_branch = HotelManagement()

ue_branch.customer_detail(name="fred", age=19, date="October 11, 2018")
