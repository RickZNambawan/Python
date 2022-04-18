newNumber = 0
counter = 10
for number in range(1, 4):
    counter = counter + number
    newNumber = counter - number * number
    print(newNumber)
