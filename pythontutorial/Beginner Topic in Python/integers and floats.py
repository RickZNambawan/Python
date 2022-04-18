""" Integer and Float are data types
    Integer - whole number
    Float - real number (with decimal)
"""

""" Arithmetic Operators: """
# Addition: 3 + 2
# Subtraction: 3 - 2
# Multiplication: 3 * 2
# Division: 3 / 2           # whole number with remainder
# Floor Division: 3 // 2    # only the whole number
# Modulus: 3 % 2            # only the remainder
# Exponent: 3 ** 2

""" Highest to Lowest Precedence: """
# Highest Priority: (), *, **, /, //, %
# Lowest Priority: +, -

"""" Incrementing Number """
num = 1  # Increment
num += 2  # Decrement
num -= 3
num *= 4
num **= 5
num /= 6
num //= 7
num %= 8

""" Functions """
# abs() function
absoluteNumber = -3
print(abs(absoluteNumber))  # return a positive value of a number

# round()
roundedNumber = 1.244345435234234
print(round(roundedNumber))  # return the rounded off value of a number
print(round(roundedNumber, 3))  # return how many decimal point you need

""" Comparisons Operators: """
# Equal: 3 == 2
# Not Equal: 3 != 2
# Greater Than: 3 > 2
# Less Than: 3 < 2
# Greater Than or Equal: 3 >= 2
# Less Than or Equal: 3 <= 2

# Return Boolean Type (True or False)
numOne = 3
numTwo = 2
print(numOne == numTwo)
print(numOne != numTwo)
print(numOne > numTwo)
print(numOne < numTwo)
print(numOne >= numTwo)
print(numOne <= numTwo)

""" Converting Data Type """
# Casting / TypeCasting
anotherNumOne = "100"
anotherNumTwo = "200"
print(anotherNumOne + anotherNumTwo)  # it only concatenate because it is a string
print(int(anotherNumOne) + int(anotherNumTwo))  # convert to int using int() function
