anotherNumber = 5
for number in range(1, 5):  # 1 # 2
    counter = 3
    while counter >= 0:
        anotherNumber = anotherNumber + 5 - number  # 9 # 13 # 17        # 8
        newNumber = anotherNumber * counter + counter  # 30 # 28 # 18
        print(newNumber)  # 30 # 28 # 18
        counter -= 1

# anotherNumber = 21
# number = 2
# counter = 3
# while counter >= 0:
#     anotherNumber = anotherNumber + 5 - number
#     newNumber = anotherNumber * counter + counter
#     print(newNumber)
#     counter -= 1
