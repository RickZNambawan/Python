""" Dictionary - lists of key and value pairs
    Dictionary is mutable
"""

""" Declaration """
myDict = {}
newDict = dict()

# the key is string
student = {"name": "Fred", "age": 19, "courses": ["Math", "CompSci"]}
print(student["courses"])

# the key is integer
number = {1: "uno", 2: "dos", 3: "tres", 4: "kwatro"}
print(number[2])

""" Adding keys and values of Dictionary """
phones = {1: "Iphone", 2: "Samsung", 3: "Oppo"}
phones[4] = "Vivo"

""" Updating Values of Dictionary """
mobileNum = {1: 123213, 2: 324324, 3: 21233}
mobileNum[2] = 123456
print(mobileNum)

""" Function of Dictionary """
# len() function
brand = {1: "Iphone", 2: "Samsung", 3: "Oppo"}

print(len(brand))  # return how many values are there in dictionary
""" Method of Dictionary """
# update() method
animals = {1: "Dog", 2: "Cat", 3: "Tiger"}
animals.update({2: "Mouse", 4: "Snakes", 5: "Monkey"})  # updating values and adding key and value pairs in one line
print(animals)

# get() method
employee = {"name": "Michael", "age": 19, "course": "HRM"}
print(employee.get("address"))  # check if key is in dictionary without error message, if not then print None
print(employee.get("school", "Not Found"))  # modify error message

# pop() method
classmates = {1: "Florante", 2: "Clarence", 3: "Ledesma", 4: "Nacu"}
classmates.pop(4)  # remove key and value from the dictionary
popped = classmates.pop(2)  # assign the removed value to a variable
print(classmates)
print(popped)

# keys() method
currency = {1: "peso", 2: "yen", 3: "dollar"}
print(currency.keys())  # return all the keys of a dictionary

# values() method
month = {"february": 2, "november": 11, "july": 7}
print(month.values())  # return all the values of a dictionary

# items() method
words = {"bahay": "house", "relo": "watch", "bentilador": "electricfan"}
print(words.items())  # return all the keys and values of a dictionary

""" Delete key and value of Dictionary"""
# del keyword
computers = {1: "Asus", 2: "Dell", 3: "Hp"}
del computers[2]  # delete key and value in the dictionary
print(computers)

del computers  # delete the dictionary

""" Dictionary Using For Loop with Methods """
names = {"Frederick": "Castaneda", "Lyka": "Agad", "Florante": "Ralotin"}

# using keys() method
for key in names.keys():  # to loop through the keys of the dictionary
    print(key)

# using values() method
for value in names.values():  # to loop through the values of the dictionary
    print(value)

# using items() method
for key, value in names.items():  # to loop through the key and value of the dictionary
    print(key, value)

""" Dictionary Using For Loop with Functions """
country = {"Philippines": "Pasig", "Japan": "Tokyo", "USA": "Canada"}

#  using enumerate() function
for index, value in enumerate(country, 1):  # loop values with index position
    print(index, value)

# using zip() function with lists
names = ["Peter", "Tony", "Steve", "Bruce"]
heroes = ["Spiderman", "Ironman", "Captain America", "Hulk"]
superhero = {}
for name, hero in zip(names, heroes):  # to combine 2 lists and make it a key, value pairs
    myDict[name] = hero
print(myDict)
