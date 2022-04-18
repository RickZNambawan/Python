# # tuples you can add and remove but you can't change the value
# students = ("fred", "florante", "clarence", "patrick", "dianne", "shiry")
# print(students[0]) # can't change the value
# # students[0] = "HAHAHA"
# # print(students[0])
#
# # lists you can add, remove or modify
# subj = ["Math", "English", "Filipino", "MAPEH"]
# print(subj[0])
# subj[0] = "HAHA"
# print(subj[0])
#
# # dictionary you can add, remove or modify
# birthday = {"Fred": "July", "Lyka": "May"}
# print(birthday["Fred"])
# birthday ["HAHAHA"] =  "POTA"
# print(birthday["HAHAHA"])
# print(birthday)

# # def sumAll(*args):
# #     return args

# # print(sum(sumAll(5, 3, 5, 6, 7, 10)))

# def sumAll(*args):
#     sumOfAllNumbers = 0
#     for n in args:
#         sumOfAllNumbers += n
#     print(sumOfAllNumbers)
#
# listOfNumbers = []
# while True:
#     number = int(input("Enter number to add: "))
#     if number == 0:
#         break
#     else:
#         listOfNumbers.append(number)
#
# sumAll(*listOfNumbers)


# sumOfAllNumbers = 0
# while True:
#     number = int(input("Enter number to add: "))
#     if number == 0:
#         break
#     else:
#         sumOfAllNumbers += number
# print(sumOfAllNumbers)

# sumOfNumbers = 0
# while True:
#     try:
#         number = input("Enter number to add: ")
#         if number == "done":
#             break
#         else:
#             sumOfNumbers += int(number)
#     except ValueError:
#         print("Invalid Literal")
# print(sumOfNumbers)

largest = 0
for number in [4, 7, 3, 5, 6, 9, 10]:
    if number > largest:
        largest = number
    print("Smallest: {}\t\t\tLargest: {}".format(number, largest))
print("Largest: {}".format(largest))
