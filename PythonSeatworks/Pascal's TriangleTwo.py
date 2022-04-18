row = int(input("Enter a row number: "))
answerList = []
answer = 0
for number in range(0, row+2):
    answer += 2 ** number
    answerList.append(answer)
print(answerList)

sumAbove = 0
for number in answerList[0:row]:
    sumAbove += number

sumBelow = answerList[row+1]
print(f"The sum of numbers above row {row} is {sumAbove:,}. The sum of numbers in row {row+1} is {sumBelow:,}.")


# row = int(input("Enter a row number: "))
# sumAbove = 0
# for number in range(row):
#     sumAbove += 2 ** number
# for number in range(row + 2):
#     sumBelow = 2 ** number
# print(f"The sum of numbers above row {row} is {sumAbove:,}. The sum of numbers in row {row+1} is {sumBelow:,}.")










# # list = [1, 2, 4, 8 ,16, 32]
# # # for number in list:
# # #     print(number)
# # number = int(input("Enter a number: "))
# # print(list[number + 1])
#
# # number = 5
# # print(number)
#
#
#
#
#
#
#
#
#
#
#
#
#
# #
# row = int(input("Enter a row number: "))
# answerList = [1]
# rowList = []
#
# answer = 1
# for number in range(0, row+1):
#     answer = answer * 2
#     answerList.append(answer)
#
# for number in range(0, row+2):
#     rowList.append(number)
#
# sumAbove = 0
# for number in (answerList[0:row]):
#     sumAbove += number
#     print(sumAbove)
# sumBelow = answerList[row+1]
# rowBelow = rowList[row+1]
# print("The sum of numbers above row {} is {:,}. The sum of numbers in row {} is {:,}".format(row, sumAbove, rowBelow, sumBelow))