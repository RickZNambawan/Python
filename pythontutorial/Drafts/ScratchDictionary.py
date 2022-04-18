# myNumber = []
# for number in range(0, 51, 1):
#     myNumber.append(number)
#
# myList = []
# for number in myNumber:
#     if (number % 2) == 1:
#         myList.append(number)
#
# for number in myList:
#     print(number)

# myNumber = [number for number in range(0, 51, 1)]
# myList = [number for number in myNumber if (number % 2) == 1]
# for i in myList:
#     print(i)

# myDict = {}
# for name, hero in zip(names, heroes):
#     myDict[name] = hero

#     print("Super Hero Name: {}\nReal Name: {}\n".format(myDict[name], name))

names = ["Peter", "Tony", "Bruce", "Steve"]
heroes = ["Spider Man", "Iron Man", "Hulk", "Captain America"]

myDict = {name: hero for name, hero in zip(names, heroes)}
for key in myDict:
    print("Super Hero: {}\nReal Name: {}\n".format(myDict[key], key))

names = ["Peter", "Tony", "Bruce"]
heroes = ["SpiderMan", "IronMan", "Hulk"]
powers = ["Web", "Robot", "Strength"]
myDict = {}
print(sep="")
for name, hero, power in zip(names, heroes, powers):
    myDict[name, hero] = power


# for name, hero in myDict.items():
#     print(name, hero)

# print(myDict["Peter", "Spiderman"] = "Tanga")

myDict["Peter", "SpiderMan"] = "Tanga"

word = "frederick"
dictLetter = {}

for c in word:
    print("Great")
    dictLetter[c] = dictLetter.get(c, 0) + 1
print(dictLetter)