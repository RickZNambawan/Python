# import sqlite3
#
# conn = sqlite3.connect("music.sqlite")
# c = conn.cursor()
#
# # c.execute("DROP TABLE IF EXISTS Tracks")
# # c.execute("CREATE TABLE Tracks (title TEXT, plays INTEGER)")
#
# # while True:
# #     title = input("Enter title: ")
# #     if title == "done":
# #         break
# #     else:
# #         plays = int(input("Enter plays: "))
# #         print("")
# #         c.execute("INSERT INTO Tracks (title, plays) VALUES (?, ?)",
# #                   (title, plays))
#
# # c.execute("DELETE FROM Tracks WHERE title = 'fred'")
# # conn.commit()
#
# print("Tracks: ")
# c.execute("SELECT title, plays FROM Tracks")
# for row in c:
#     print(row)


# c.close()

# DROP TABLE IF EXISTS Tracks
# CREATE TABLE Tracks (title TEXT, plays INTEGER)

# INSERT INTO Tracks (title, plays) VALUES ('My Way', 15)
# SELECT * FROM Tracks WHERE title = 'My Way'
# SELECT title,plays FROM Tracks ORDER BY title
# DELETE FROM Tracks WHERE title = 'My Way'
# UPDATE Tracks SET plays = 16 WHERE title = 'My Way'
# (INSERT, SELECT, UPDATE, and DELETE)
# c.fetchall()
# c.fetchone()
# c.fetchmany()


import sqlite3


conn = sqlite3.connect(":memory:")
c = conn.cursor()

c.execute("""CREATE TABLE company (first TEXT, last TEXT, pay INTEGER)""")
# c.execute("INSERT INTO company VALUES ('Lyka', 'Agad', '18')")

c.execute("INSERT INTO company VALUES (?, ?, ?)", ("Fred", "Castaneda", 19))
c.execute("SELECT * FROM company WHERE last = 'Castaneda'")
print(c.fetchall())



conn.commit()
conn.close()































