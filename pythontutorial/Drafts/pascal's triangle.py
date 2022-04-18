row = int(input("Enter a row number: "))
answerList = [1]
answer = 1
for number in range(0, row+1):
    answer = answer * 2
    answerList.append(answer)

sumAbove = 0
for number in (answerList[0:row]):
    sumAbove += number
sumBelow = answerList[row+1]

print("The sum of numbers above row {} is {:,}. The sum of numbers in row {} is {:,}".format(row, sumAbove, row+1, sumBelow))




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
# sumBelow = answerList[row+1]
# rowBelow = rowList[row+1]
# print("The sum of numbers above row {} is {:,}. The sum of numbers in row {} is {:,}".format(row, sumAbove, rowBelow, sumBelow))


