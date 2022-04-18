""" List - it allows us to work with a lists of values """

""" Accessing Values """
# index
courses = ["Programming", "STS", "UTS", "P.E"]
print(courses[0])  # to access the position of the value
print(courses[1])
print(courses[-1])  # automatically access the last value
print(courses[-2])  # negative index starts at the last value

# slicing index
names = ["Fred", "Lyka", "Florante", "Clarence"]
print(names[0:3])  # starts at position 0, stops at position 3
print(names[:2])  # starts at the initial value 0
print(names[2:])  # starts at position 2 all the way up to the last value
print(names[:])  # show all the values from first value up to the last value

""" Functions of a list """
# len() function
vowels = ["a", "e", "i", "o", "u"]
print(len(vowels))  # return how many values on a list

# sorted() function
shoes = ["Nike", "Vans", "Adidas"]
sortedShoes = sorted(shoes)  # sorts the value alphabetical order without changing the list
print(sortedShoes)

# min() function
numberOne = [3, 5, 7, 9]
print(min(numberOne))  # return the lowest value of the list

# max() function
numberTwo = [5, 2, 9, 8]
print(max(numberTwo))  # return the highest value of the list

# sum() function
numberThree = [23, 55, 11, 52]
print(sum(numberThree))  # return the sum of all the values from the list

# list() function
myTuple = (1, 3, 5, 6, 7)  # tuples, sets or dictionaries
myDict = {1: 5, 2: 6}  # convert the key into a list
mySets = {1, 2, 4, 4, 6, 6, 8}
print(list(myTuple))  # to convert tuples, sets or dictionaries into list
print(list(myDict))
print(list(mySets))

""" Methods of a List """
# append() method
fruits = ["Apple", "Mango", "Berry", "Banana"]
fruits.append("Lemon")  # adds the value to the end of the list
print(fruits)

# count() method
data = ["hahha", "hahha", 2, 2, 2, 4, 6]
print(data.count(2))  # returns count of how many times item occurs

# insert() method
heroes = ["Thor", "Superman", "Ironman", "Batman"]
heroes.insert(0, "Spiderman")  # adds the value to the specific position on the list
print(heroes)

# extend() method
numsOne = [1, 2, 3, 4, 5]
numsTwo = [6, 7, 8, 9, 10]
numsOne.extend(numsTwo)  # combines another list of values to the specific list
print(numsOne)

# remove() method
books = ["NSTP BOOK", "COMP ETHICS BOOK", "UTS BOOK", "STS BOOK"]
books.remove("COMP ETHICS BOOK")  # removes values with the name of the value
print(books)

# pop() method
stacks = [5, 6, 12, 3, 7, 9]
stacks.pop()  # removes the last value of the list
popped = stacks.pop(2)  # removes the value using the position you want
print(stacks)
print(popped)  # return the removed value

# reverse() method
alphabet = ["a", "b", "c", "d"]
alphabet.reverse()  # reverses the values of list
print(alphabet)

# sort() method
ages = [19, 21, 25, 17]  # values of number
ages.sort()  # sorts the value from ascending to descending
print(ages)
ages.sort(reverse=True)  # sorts the value from descending to ascending
print(ages)

surnames = ["castaneda", "roque", "ralotin", "agad"]  # values of strings
surnames.sort()  # sorts the value alphabetical order
print(surnames)
surnames.sort(reverse=True)  # sorts the value reverse alphabetical order
print(surnames)

# index() method
shampoos = ["Palmolive", "Creamsilk", "Sunsilk", "Rejoice"]
print(shampoos.index("Sunsilk"))  # return the index position of the value

# clear() method
myList = [1, 3, 5, 2, 123, 5]
myList.clear()  # remove all the values from the list
print(myList)

# join() method
nameList = ["Frederick", "Castaneda", "Abraham", "Jr."]
fullName = " - ".join(nameList)  # join together all the values with characters seperated
print(fullName)

# split() method
newStringList = fullName.split(" - ")  # to bring back the joint list to actual list
print(newStringList)

animals = "Dog Cat Mouse Tiger".split()  # to make strings a list
print(animals)
print(animals[2])

""" Checking if the value is in the list """
# CHECKING FOR MEMBERSHIP
# Return Boolean Values
phones = ["Iphone", "Samsung", "Oppo", "Vivo"]
print("Cherry Mobile" in phones)  # return if the values are in the list
print("Samsung" in phones)

""" List using for loop """
computers = ["Asus", "Mac", "Dell", "Hp"]
for item in computers:  # loop through all the values from the list
    print(item)

# enumerate() function
bands = ["Silent Sanctuary", "Ben&Ben", "Rocksteady", "IV of Spades"]
for index, band in enumerate(bands, 2):  # get the index of all values from the list
    print(index, band)  # starts from index 2
